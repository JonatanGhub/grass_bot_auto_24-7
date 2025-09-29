@echo off
echo ========================================
echo      ELIMINANDO BOTS DE PM2
echo ========================================
echo.

cd /d "%~dp0"
pm2 delete ecosystem.config.js

echo.
echo Procesos eliminados de la lista de PM2.
echo.

pause
