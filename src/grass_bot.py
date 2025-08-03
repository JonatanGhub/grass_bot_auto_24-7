import asyncio
import logging
import os
from datetime import datetime
from typing import List
from dotenv import load_dotenv
from .security_system import SecuritySystem

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/grass_bot.log'
)
logger = logging.getLogger(__name__)

class GrassBot:
    def __init__(self, security: SecuritySystem):
        self.security = security
        self.active_tasks: List[asyncio.Task] = []
        self.running = False
        load_dotenv()
        self.wallet = os.getenv('WALLET_ADDRESS')

    async def dummy_work(self, proxy):
        """Simula trabajo con el proxy (sustituye por lógica real)."""
        while self.running:
            try:
                async with self.security.get_session() as session:
                    # Aquí irían calls reales a la dApp / smart-contract
                    logger.info(f"[{proxy.address}] ping at {datetime.now()}")
                await asyncio.sleep(300)   # 5 min
            except Exception as e:
                logger.error(f"Error con proxy {proxy.address}: {e}")
                await asyncio.sleep(60)

    async def start(self):
        self.running = True
        # 1 tarea de monitor de salud
        self.active_tasks.append(
            asyncio.create_task(self.security.monitor_proxy_health())
        )
        # 1 tarea por proxy
        for proxy in list(self.security.active_proxies):
            self.active_tasks.append(asyncio.create_task(self.dummy_work(proxy)))
            logger.info(f"Tarea iniciada con proxy {proxy.address}")

    async def stop(self):
        self.running = False
        for t in self.active_tasks:
            t.cancel()
        await asyncio.gather(*self.active_tasks, return_exceptions=True)
        self.active_tasks.clear()
        logger.info("Bot detenido")