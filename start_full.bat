@echo off
echo ========================================
echo    INICIANDO GRASS AUTOMAT
echo ========================================
echo.

cd /d "%~dp0"

echo Verificando entorno virtual...
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: No se encuentra el entorno virtual
    echo Ejecuta: python -m venv venv
    echo Luego: venv\Scripts\activate.bat
    echo Y: pip install -r requirements.txt
    pause
    exit /b 1
)

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo Verificando dependencias...
python -c "import asyncio, logging" 2>nul
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r requirements.txt
)

echo.
echo Iniciando el bot principal...
echo Para detener, presiona Ctrl+C
echo.

python main.py

pause 