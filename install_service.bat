@echo off
echo ========================================
echo    INSTALANDO GRASS AUTOMAT COMO SERVICIO
echo ========================================
echo.

cd /d "%~dp0"

echo Verificando permisos de administrador...
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Permisos de administrador confirmados.
) else (
    echo ERROR: Este script requiere permisos de administrador.
    echo Ejecuta este archivo como administrador.
    pause
    exit /b 1
)

echo Verificando entorno virtual...
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: No se encuentra el entorno virtual
    echo Ejecuta: python -m venv venv
    echo Luego: venv\Scripts\activate.bat
    echo Y: pip install -r requirements.txt
    pause
    exit /b 1
)

echo Creando script de servicio...
(
echo @echo off
echo cd /d "%~dp0"
echo call venv\Scripts\activate.bat
echo python main.py
) > "grass_service.bat"

echo Instalando servicio usando NSSM...
echo.
echo Si no tienes NSSM instalado, puedes:
echo 1. Descargarlo de: https://nssm.cc/download
echo 2. O usar Task Scheduler de Windows
echo.

echo Para usar Task Scheduler:
echo 1. Abre "Programador de tareas"
echo 2. Crea una nueva tarea básica
echo 3. Nombre: "Grass Automat"
echo 4. Trigger: Al iniciar sesión
echo 5. Acción: Iniciar programa
echo 6. Programa: %~dp0start_full.bat
echo.

echo Para usar NSSM (si lo tienes instalado):
echo nssm install "Grass Automat" "%~dp0grass_service.bat"
echo nssm set "Grass Automat" AppDirectory "%~dp0"
echo nssm set "Grass Automat" Description "Grass Automat Bot Service"
echo nssm start "Grass Automat"
echo.

echo Servicio configurado. El bot se iniciará automáticamente.
pause 