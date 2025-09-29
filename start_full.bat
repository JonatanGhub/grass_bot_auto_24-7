@echo off
echo ========================================
echo    INICIANDO BOTS CON PM2
echo ========================================
echo.

REM Ir al directorio del script
cd /d "%~dp0"

echo Verificando si los procesos ya existen...
pm2 describe grass-bot >nul 2>&1
if %errorlevel% == 0 (
    echo Reiniciando grass-bot...
    pm2 restart grass-bot
) else (
    echo Iniciando grass-bot por primera vez...
    pm2 start ecosystem.config.js --only grass-bot
)

pm2 describe grass-monitor >nul 2>&1
if %errorlevel% == 0 (
    echo Reiniciando grass-monitor...
    pm2 restart grass-monitor
) else (
    echo Iniciando grass-monitor por primera vez...
    pm2 start ecosystem.config.js --only grass-monitor
)

echo.
echo ========================================
echo    PROCESOS INICIADOS
echo ========================================
echo.
echo Para ver los logs, usa: pm2 logs
echo Para detener los bots, usa: stop_full.bat
echo.

pause
