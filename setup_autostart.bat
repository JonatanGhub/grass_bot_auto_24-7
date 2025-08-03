@echo off
echo ========================================
echo    CONFIGURANDO INICIO AUTOMÁTICO
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

echo Configurando inicio automático en el registro...
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "Grass Automat" /t REG_SZ /d "\"%~dp0start_full.bat\"" /f

if %errorlevel% == 0 (
    echo.
    echo ========================================
    echo    ¡CONFIGURACIÓN EXITOSA!
    echo ========================================
    echo.
    echo El bot se iniciará automáticamente cuando inicies sesión.
    echo.
    echo Para probar ahora, ejecuta: start_full.bat
    echo.
    echo Para desactivar el inicio automático:
    echo reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "Grass Automat" /f
    echo.
) else (
    echo ERROR: No se pudo configurar el inicio automático.
    echo Intenta ejecutar como administrador.
)

pause 