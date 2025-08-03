@echo off
echo ========================================
echo    CONFIGURANDO REPOSITORIO GIT
echo ========================================
echo.

cd /d "%~dp0"

echo Inicializando repositorio Git...
git init

echo Agregando archivos al staging...
git add .

echo Creando commit inicial...
git commit -m "Initial commit: Grass Automat Bot

- Bot automatizado para operaciones blockchain
- Sistema de seguridad integrado
- Scripts de inicio automático para Windows
- Configuración de monitoreo y logging
- Documentación completa"

echo.
echo ========================================
echo    ¡REPOSITORIO GIT CONFIGURADO!
echo ========================================
echo.
echo Para conectar con GitHub:
echo 1. Crea un repositorio en GitHub
echo 2. Ejecuta: git remote add origin https://github.com/tu-usuario/grass-automat.git
echo 3. Ejecuta: git branch -M main
echo 4. Ejecuta: git push -u origin main
echo.
echo Archivos incluidos en el repositorio:
echo - Código fuente del bot
echo - Scripts de inicio automático
echo - Documentación completa
echo - Configuración de seguridad
echo.
echo Archivos EXCLUIDOS (por seguridad):
echo - Archivos de log
echo - Variables de entorno (.env)
echo - Configuración de seguridad (security_config.yaml)
echo - Entornos virtuales
echo.

pause 