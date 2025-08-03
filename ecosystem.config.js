// ecosystem.config.js

// --- CONFIGURACIÓN PARA WINDOWS ---
const PYTHON_INTERPRETER_WINDOWS = 'C:/Users/jonat/Desktop/grass-automat/venv/Scripts/python.exe';

// --- CONFIGURACIÓN PARA MACOS/LINUX ---
// Descomente la siguiente línea si usa macOS o Linux
// const PYTHON_INTERPRETER_MACOS_LINUX = './venv/bin/python';

module.exports = {
  apps : [{
    name   : "grass-bot",
    script : "main.py",
    interpreter: PYTHON_INTERPRETER_WINDOWS, // Cambie a PYTHON_INTERPRETER_MACOS_LINUX si es necesario
    exec_mode: "fork"
  }, {
    name   : "grass-monitor",
    script : "monitor_grass.py",
    interpreter: PYTHON_INTERPRETER_WINDOWS, // Cambie a PYTHON_INTERPRETER_MACOS_LINUX si es necesario
    exec_mode: "fork"
  }]
}