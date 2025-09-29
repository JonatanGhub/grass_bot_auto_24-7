@echo off
echo ========================================
echo      DETENIENDO BOTS CON PM2
echo ========================================
echo.

cd /d "%~dp0"
pm2 stop ecosystem.config.js

echo.
echo Procesos detenidos.
echo Para iniciarlos de nuevo, usa: start_full.bat
echo.

pause
