import aiohttp
import asyncio
import random
import time
import logging
import json
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import requests
from fake_useragent import UserAgent
from collections import deque
from contextlib import asynccontextmanager
import yaml
import ipaddress
import os
from prometheus_client import Counter, Gauge

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/security.log'
)
logger = logging.getLogger(__name__)

# Métricas
PROXY_FAILURES = Counter('proxy_failures_total', 'Total number of proxy failures')
PROXY_SWITCHES = Counter('proxy_switches_total', 'Total number of proxy switches')
ACTIVE_PROXIES = Gauge('active_proxies', 'Number of currently active proxies')

@dataclass
class ProxyConfig:
    """Configuración para un proxy"""
    address: str
    port: int
    username: Optional[str] = None
    password: Optional[str] = None
    protocol: str = 'http'
    country: Optional[str] = None
    last_used: datetime = datetime.now()
    failure_count: int = 0
    response_time: float = 0.0

class SecuritySystem:
    """Sistema de seguridad con gestión de proxy y user-agent"""

    def __init__(self, config_path: str = 'config/security_config.yaml'):
        print("Inicializando SecuritySystem...")  # Debug
        self.load_config(config_path)
        self.setup_proxies()
        self.setup_user_agents()
        print(f"SecuritySystem inicializado con {len(self.active_proxies)} proxies activos")  # Debug

    def load_config(self, config_path: str):
        """Cargar configuración desde archivo YAML"""
        try:
            print(f"Intentando cargar configuración desde: {config_path}")  # Debug
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
            print("Configuración cargada exitosamente")  # Debug
            logger.info("Configuración cargada exitosamente")
        except Exception as e:
            print(f"Error al cargar configuración: {e}")  # Debug
            logger.error(f"Error al cargar configuración: {e}")
            raise

    def setup_proxies(self):
        """Inicializar pools de proxies desde la configuración"""
        try:
            print("Configurando proxies...")  # Debug
            # Cargar pool principal de proxies
            self.main_proxy_pool = [
                ProxyConfig(**proxy) for proxy in self.config['proxies']['main']
            ]

            # Cargar pool de respaldo de proxies
            self.backup_proxy_pool = [
                ProxyConfig(**proxy) for proxy in self.config['proxies']['backup']
            ]

            # Inicializar configuración de rotación de proxies
            self.proxy_rotation_interval = self.config['proxy_settings']['rotation_interval']
            self.max_failures = self.config['proxy_settings']['max_failures']

            # Inicializar colas de proxies
            self.active_proxies = deque(self.main_proxy_pool)
            self.backup_proxies = deque(self.backup_proxy_pool)
            self.banned_proxies = set()

            ACTIVE_PROXIES.set(len(self.main_proxy_pool))
            print(f"Proxies configurados: {len(self.main_proxy_pool)} principales, {len(self.backup_proxy_pool)} de respaldo")  # Debug
            logger.info(f"Proxies configurados: {len(self.main_proxy_pool)} principales, {len(self.backup_proxy_pool)} de respaldo")
        except Exception as e:
            print(f"Error al configurar proxies: {e}")  # Debug
            logger.error(f"Error al configurar proxies: {e}")
            raise

    def setup_user_agents(self):
        """Inicializar rotación de user agents"""
        try:
            print("Configurando user agents...")  # Debug
            self.user_agent = UserAgent()
            self.user_agents = deque(maxlen=100)
            self.refresh_user_agents()
            print("User agents configurados exitosamente")  # Debug
            logger.info("User agents configurados exitosamente")
        except Exception as e:
            print(f"Error al configurar user agents: {e}")  # Debug
            logger.error(f"Error al configurar user agents: {e}")
            raise

    def get_proxy_url(self, proxy: ProxyConfig) -> str:
        """Generar URL del proxy desde la configuración"""
        auth = f"{proxy.username}:{proxy.password}@" if proxy.username else ""
        return f"{proxy.protocol}://{auth}{proxy.address}:{proxy.port}"

    async def verify_proxy(self, proxy: ProxyConfig) -> bool:
        """Verificar si un proxy está funcionando"""
        try:
            print(f"Verificando proxy: {proxy.address}")  # Debug
            async with aiohttp.ClientSession() as session:
                start_time = time.time()
                async with session.get(
                    'https://api.ipify.org?format=json',
                    proxy=self.get_proxy_url(proxy),
                    timeout=10
                ) as response:
                    if response.status == 200:
                        proxy.response_time = time.time() - start_time
                        proxy.last_used = datetime.now()
                        print(f"Proxy {proxy.address} verificado exitosamente")  # Debug
                        return True
            return False
        except Exception as e:
            print(f"Error al verificar proxy {proxy.address}: {e}")  # Debug
            logger.warning(f"Error al verificar proxy {proxy.address}: {e}")
            proxy.failure_count += 1
            PROXY_FAILURES.inc()
            return False

    async def rotate_proxy(self) -> Optional[ProxyConfig]:
        """Rotar al siguiente proxy disponible"""
        try:
            print("Iniciando rotación de proxy...")  # Debug
            # Intentar obtener proxy del pool activo
            while self.active_proxies:
                proxy = self.active_proxies.popleft()
                print(f"Probando proxy activo: {proxy.address}")  # Debug
                if await self.verify_proxy(proxy):
                    self.active_proxies.append(proxy)
                    PROXY_SWITCHES.inc()
                    return proxy
                else:
                    self.handle_proxy_failure(proxy)

            # Si el pool activo está vacío, intentar con proxies de respaldo
            print("Pool activo vacío, intentando proxies de respaldo...")  # Debug
            while self.backup_proxies:
                proxy = self.backup_proxies.popleft()
                print(f"Probando proxy de respaldo: {proxy.address}")  # Debug
                if await self.verify_proxy(proxy):
                    self.active_proxies.append(proxy)
                    PROXY_SWITCHES.inc()
                    return proxy
                else:
                    self.handle_proxy_failure(proxy)

            # Si todos los proxies fallaron, activar protocolo de emergencia
            print("Todos los proxies fallaron, activando protocolo de emergencia...")  # Debug
            return await self.emergency_proxy_protocol()

        except Exception as e:
            print(f"Error en rotación de proxy: {e}")  # Debug
            logger.error(f"Error en rotación de proxy: {e}")
            return None

    def handle_proxy_failure(self, proxy: ProxyConfig):
        """Manejar fallo de proxy"""
        proxy.failure_count += 1
        PROXY_FAILURES.inc()

        if proxy.failure_count >= self.max_failures:
            self.banned_proxies.add(proxy.address)
            print(f"Proxy {proxy.address} baneado por fallos excesivos")  # Debug
            logger.warning(f"Proxy {proxy.address} baneado por fallos excesivos")
        elif proxy.failure_count < self.max_failures:
            self.backup_proxies.append(proxy)

    async def emergency_proxy_protocol(self) -> Optional[ProxyConfig]:
        """Protocolo de emergencia cuando todos los proxies fallan"""
        print("Activando protocolo de emergencia de proxies")  # Debug
        logger.critical("Protocolo de emergencia de proxies activado - todos los proxies fallaron")

        # Esperar y reintentar todos los proxies
        await asyncio.sleep(300)  # 5 minutos de espera

        # Resetear todos los proxies e intentar de nuevo
        self.active_proxies = deque(self.main_proxy_pool)
        self.backup_proxies = deque(self.backup_proxy_pool)
        self.banned_proxies.clear()

        return await self.rotate_proxy()

    def refresh_user_agents(self):
        """Refrescar pool de user agents"""
        try:
            new_agents = [self.user_agent.random for _ in range(50)]
            self.user_agents.extend(new_agents)
            logger.info("User agents refrescados exitosamente")
        except Exception as e:
            logger.error(f"Error al refrescar user agents: {e}")

    def get_next_user_agent(self) -> str:
        """Obtener siguiente user agent de la rotación"""
        if len(self.user_agents) < 10:
            self.refresh_user_agents()
        return self.user_agents.popleft()

    @asynccontextmanager
    async def get_session(self) -> aiohttp.ClientSession:
        """Obtener sesión con proxy y user agent rotados"""
        proxy = await self.rotate_proxy()
        if not proxy:
            raise Exception("No hay proxies disponibles")

        headers = {
            'User-Agent': self.get_next_user_agent(),
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        session = aiohttp.ClientSession(
            headers=headers,
            proxy=self.get_proxy_url(proxy)
        )

        try:
            yield session
        finally:
            await session.close()

    async def make_request(self, url: str, method: str = 'GET', **kwargs) -> Tuple[int, dict]:
        """Hacer una petición segura con rotación de proxy y user agent"""
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                async with self.get_session() as session:
                    async with session.request(method, url, **kwargs) as response:
                        return response.status, await response.json()
            except Exception as e:
                retry_count += 1
                logger.warning(f"Intento de petición fallido (intento {retry_count}): {e}")
                await asyncio.sleep(2 ** retry_count)  # Retroceso exponencial

        raise Exception("Máximo de reintentos excedido")

    async def monitor_proxy_health(self):
        """Monitorear salud de los proxies en segundo plano"""
        while True:
            try:
                for proxy in list(self.active_proxies):
                    if not await self.verify_proxy(proxy):
                        self.active_proxies.remove(proxy)
                        self.handle_proxy_failure(proxy)

                ACTIVE_PROXIES.set(len(self.active_proxies))
                await asyncio.sleep(300)  # Verificar cada 5 minutos
            except Exception as e:
                logger.error(f"Error en monitoreo de salud de proxies: {e}")
                await asyncio.sleep(60)