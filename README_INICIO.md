# 🚀 Grass Automat - Guía de Inicio

## 📋 Requisitos Previos

1. **Python 3.8+** instalado
2. **Entorno virtual** configurado
3. **Dependencias** instaladas

## 🔧 Configuración Inicial

### 1. Crear entorno virtual (si no existe)
```bash
python -m venv venv
```

### 2. Activar entorno virtual
```bash
venv\Scripts\activate.bat
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🚀 Opciones de Inicio

### Opción 1: Inicio Manual
- **Archivo**: `start_full.bat`
- **Uso**: Doble clic en el archivo
- **Descripción**: Inicia el bot con verificaciones automáticas

### Opción 2: Inicio Automático al Iniciar Sesión
- **Archivo**: `setup_autostart.bat`
- **Uso**: Ejecutar como administrador
- **Descripción**: Configura el bot para iniciar automáticamente

### Opción 3: Servicio de Windows
- **Archivo**: `install_service.bat`
- **Uso**: Ejecutar como administrador
- **Descripción**: Instala como servicio del sistema

## 📁 Archivos de Inicio Disponibles

| Archivo | Descripción |
|---------|-------------|
| `start.bat` | Inicio básico del bot |
| `start_full.bat` | Inicio completo con verificaciones |
| `start_monitor.bat` | Solo el monitor del sistema |
| `setup_autostart.bat` | Configura inicio automático |
| `disable_autostart.bat` | Desactiva inicio automático |
| `install_service.bat` | Instala como servicio |

## 🔍 Verificación

### Verificar que todo funciona:
1. Ejecuta `start_full.bat`
2. Deberías ver mensajes de inicio
3. El bot debería estar funcionando
4. Revisa los logs en la carpeta `logs/`

### Logs importantes:
- `logs/main.log` - Log principal del bot
- `logs/grass_monitor.log` - Log del monitor
- `logs/security.log` - Log del sistema de seguridad

## ⚠️ Solución de Problemas

### Error: "No se encuentra el entorno virtual"
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Error: "Módulo no encontrado"
```bash
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### Error: "Permisos insuficientes"
- Ejecuta los scripts como administrador
- O usa `setup_autostart.bat` para configuración de usuario

## 🎯 Recomendación

**Para uso diario**: Usa `setup_autostart.bat` para que el bot se inicie automáticamente cuando inicies sesión en Windows.

**Para desarrollo**: Usa `start_full.bat` para control manual.

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en la carpeta `logs/`
2. Verifica que el entorno virtual esté activado
3. Asegúrate de que todas las dependencias estén instaladas 