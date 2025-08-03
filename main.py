import asyncio
import logging
import signal
import sys
from src.security_system import SecuritySystem
from src.grass_bot import GrassBot

# Asegúrate de que existe la carpeta logs
import os
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/main.log'
)
logger = logging.getLogger(__name__)

async def run_bot():
    try:
        # Inicializar sistema de seguridad
        sec = SecuritySystem()
        bot = GrassBot(sec)

        async def shutdown():
            logger.info("Apagando...")
            await bot.stop()
            sys.exit(0)

        # Capturar Ctrl+C
        for s in (signal.SIGINT, signal.SIGTERM):
            signal.signal(s, lambda *_: asyncio.create_task(shutdown()))

        # Iniciar el bot
        await bot.start()

        # Mantener el bot corriendo
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        logger.error(f"Error en main: {e}")
        sys.exit(1)

def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.info("Bot detenido por el usuario")
    except Exception as e:
        logger.error(f"Error fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()