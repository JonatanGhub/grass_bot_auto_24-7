@echo off
echo ========================================
echo    LIMPIANDO ARCHIVOS DE LOG
echo ========================================
echo.

cd /d "%~dp0"

echo Eliminando archivos de log grandes...
if exist "logs\grass_monitor.log" (
    del "logs\grass_monitor.log"
    echo Eliminado: grass_monitor.log
)

if exist "logs\security.log" (
    del "logs\security.log"
    echo Eliminado: security.log
)

if exist "security_system.log" (
    del "security_system.log"
    echo Eliminado: security_system.log
)

echo.
echo ========================================
echo    ¡LIMPIEZA COMPLETADA!
echo ========================================
echo.
echo Los archivos de log han sido eliminados.
echo Los nuevos logs se crearán automáticamente.
echo.

pause 