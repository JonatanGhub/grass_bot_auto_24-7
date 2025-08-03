# Script PowerShell para configurar inicio automático
Write-Host "========================================" -ForegroundColor Green
Write-Host "   CONFIGURANDO INICIO AUTOMÁTICO" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Verificar entorno virtual
if (Test-Path "venv\Scripts\activate.bat") {
    Write-Host "✅ Entorno virtual encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ ERROR: No se encuentra el entorno virtual" -ForegroundColor Red
    Write-Host "Ejecuta: python -m venv venv" -ForegroundColor Yellow
    Write-Host "Luego: venv\Scripts\activate.bat" -ForegroundColor Yellow
    Write-Host "Y: pip install -r requirements.txt" -ForegroundColor Yellow
    Read-Host "Presiona Enter para continuar"
    exit 1
}

# Configurar inicio automático
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$startScript = Join-Path $scriptPath "start_full.bat"
$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$registryName = "Grass Automat"
$registryValue = "`"$startScript`""

try {
    Set-ItemProperty -Path $registryPath -Name $registryName -Value $registryValue -Type String
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "    ¡CONFIGURACIÓN EXITOSA!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "✅ El bot se iniciará automáticamente cuando inicies sesión." -ForegroundColor Green
    Write-Host ""
    Write-Host "📁 Script de inicio: $startScript" -ForegroundColor Cyan
    Write-Host "🔧 Entrada del registro: $registryPath\$registryName" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Para probar ahora, ejecuta: .\start_full.bat" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Para desactivar el inicio automático:" -ForegroundColor Yellow
    Write-Host "Remove-ItemProperty -Path '$registryPath' -Name '$registryName'" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "❌ ERROR: No se pudo configurar el inicio automático." -ForegroundColor Red
    Write-Host "Intenta ejecutar como administrador." -ForegroundColor Yellow
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
}

Read-Host "Presiona Enter para continuar" 