@echo off
echo ========================================
echo    DESACTIVANDO INICIO AUTOMÁTICO
echo ========================================
echo.

echo Eliminando entrada del registro...
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "Grass Automat" /f

if %errorlevel% == 0 (
    echo.
    echo ========================================
    echo    ¡DESACTIVACIÓN EXITOSA!
    echo ========================================
    echo.
    echo El bot ya no se iniciará automáticamente.
    echo.
    echo Para iniciarlo manualmente, ejecuta: start_full.bat
    echo.
) else (
    echo ERROR: No se pudo desactivar el inicio automático.
    echo La entrada podría no existir o necesitar permisos de administrador.
)

pause 