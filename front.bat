@echo off
if "%~1"=="" (
    echo Error: Debes proporcionar la ruta al directorio.
    echo Uso: %~nx0 "ruta_al_directorio"
    pause
    exit /b 1
)

cd /d "%~1"

start npm start