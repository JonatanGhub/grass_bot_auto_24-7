@echo off
REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the monitor script
call start_monitor.bat

REM Start the main bot script
call start.bat