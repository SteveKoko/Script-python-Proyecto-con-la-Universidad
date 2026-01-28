@echo off
chcp 65001 >nul
echo ========================================
echo   Monitor de Inactividad - Instalador
echo   Instalación de Dependencias
echo ========================================
echo.

:: Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado en este sistema.
    echo.
    echo Por favor, descarga e instala Python desde:
echo https://www.python.org/downloads/
echo.
    echo IMPORTANTE: Durante la instalación, marca la opción "Add Python to PATH"
echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado:
python --version
echo.

:: Verificar si tkinter está disponible
echo Verificando tkinter...
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ADVERTENCIA] tkinter no está disponible.
    echo Intentando instalar tk...
pip install tk
echo.
) else (
    echo [OK] tkinter ya está instalado
echo.
)

:: Verificar instalación de tkinter
echo Verificando instalación final...
python -c "import tkinter; print('[OK] tkinter funciona correctamente')" 2>nul
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] No se pudo instalar tkinter correctamente.
    echo.
    echo Si estás usando Python desde python.org, tkinter debería venir incluido.
    echo Si el problema persiste, intenta reinstalar Python.
echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   ¡Instalación Completada! ✓
echo ========================================
echo.
echo Todas las dependencias están instaladas correctamente.
echo Ya puedes ejecutar el script con: python script.py
echo.
pause