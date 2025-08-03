import os
import time
import subprocess
import psutil
import logging

# Ruta al ejecutable de Grass (¡pon aquí la tuya!)
GRASS_PATH = r"C:\Program Files\Grass"
print(f"GRASS_PATH: {GRASS_PATH}")
# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/grass_monitor.log'
)

def is_grass_running():
    """Verifica si el proceso de Grass está corriendo."""
    print("Verificando si Grass está corriendo...")
    for proc in psutil.process_iter(['name', 'exe']):
        try:
            if proc.info['name'] and 'grass' in proc.info['name'].lower():
                print("Grass está corriendo.")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
        print("Grass no está corriendo.")
        
    return False

def start_grass():
    """Inicia la app de Grass."""
    print("Iniciando Grass...")
    try:
        subprocess.Popen([GRASS_PATH], shell=True)
        logging.info("Grass iniciado.")
        print("Grass iniciado.")
    except Exception as e:
        logging.error(f"Error al iniciar Grass: {e}")
        print(f"Error al iniciar Grass: {e}")

def main():
    logging.info("Monitor de Grass iniciado.")
    print("Monitor de Grass iniciado.")
    while True:
        if not is_grass_running():
            logging.warning("Grass no está corriendo. Reiniciando...")
            print("Grass no está corriendo. Reiniciando...")
            start_grass()
        else:
            logging.info("Grass está corriendo.")
            print("Grass está corriendo.")
        time.sleep(60)  # Verifica cada 60 segundos

if __name__ == "__main__":
    main()