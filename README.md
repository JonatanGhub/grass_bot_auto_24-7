# 🌱 Grass Automat

Bot automatizado para gestión y monitoreo de operaciones blockchain con sistema de seguridad integrado.

## 🚀 Características

- **Bot Automatizado**: Ejecución continua de operaciones blockchain
- **Sistema de Seguridad**: Rotación de proxies y protección de claves
- **Monitoreo en Tiempo Real**: Logs detallados y alertas
- **Inicio Automático**: Configuración para ejecución automática en Windows
- **Gestión de Errores**: Recuperación automática y logging robusto

## 📋 Requisitos

- Python 3.8+
- Windows 10/11
- Conexión a Internet

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/grass-automat.git
cd grass-automat
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
WALLET_ADDRESS=tu_direccion_wallet
PRIVATE_KEY=tu_clave_privada
WEB3_PROVIDER_URL=tu_url_proveedor_web3
```

## 🚀 Uso

### Inicio Manual
```bash
start_full.bat
```

### Inicio Automático (Recomendado)
```bash
setup_autostart.bat
```

### Desactivar Inicio Automático
```bash
disable_autostart.bat
```

## 📁 Estructura del Proyecto

```
grass-automat/
├── src/
│   ├── grass_bot.py          # Bot principal
│   └── security_system.py    # Sistema de seguridad
├── config/
│   └── security_config.yaml  # Configuración de seguridad
├── logs/                     # Archivos de log
├── main.py                   # Punto de entrada
├── monitor_grass.py          # Monitor del sistema
├── start_full.bat           # Script de inicio completo
├── setup_autostart.bat      # Configuración de inicio automático
└── requirements.txt          # Dependencias Python
```

## 🔍 Monitoreo

### Logs Disponibles
- `logs/main.log` - Log principal del bot
- `logs/grass_monitor.log` - Log del monitor
- `logs/security.log` - Log del sistema de seguridad

### Verificar Estado
```bash
# Ver logs en tiempo real
tail -f logs/main.log
```

## ⚙️ Configuración

### Archivos de Configuración
- `config/security_config.yaml` - Configuración de seguridad
- `.env` - Variables de entorno (no incluido en el repositorio)

### Scripts de Inicio
- `start_full.bat` - Inicio manual con verificaciones
- `setup_autostart.bat` - Configurar inicio automático
- `disable_autostart.bat` - Desactivar inicio automático
- `install_service.bat` - Instalar como servicio de Windows

## 🛡️ Seguridad

- Rotación automática de proxies
- Protección de claves privadas
- Logging seguro de operaciones
- Validación de transacciones

## ⚠️ Advertencias

- **NUNCA** compartas tus claves privadas
- Mantén actualizadas las dependencias
- Revisa regularmente los logs
- Usa solo en redes de confianza

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en la carpeta `logs/`
2. Verifica la configuración en `config/`
3. Asegúrate de que las variables de entorno estén correctas
4. Abre un issue en GitHub

## 🔄 Actualizaciones

Para actualizar el proyecto:
```bash
git pull origin main
venv\Scripts\activate.bat
pip install -r requirements.txt
```

---

**⚠️ Importante**: Este bot maneja operaciones financieras. Úsalo con responsabilidad y en redes de prueba antes de usar en producción. 