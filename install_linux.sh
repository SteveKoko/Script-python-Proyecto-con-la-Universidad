#!/bin/bash

echo "=========================================="
echo "  Instalador de Monitor de Inactividad"
echo "=========================================="
echo ""

# Detectar distribución
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "No se pudo detectar la distribución"
    exit 1
fi

echo "Distribución detectada: $OS"
echo ""

# Verificar si tkinter ya está instalado
if python3 -c "import tkinter" 2>/dev/null; then
    echo "✓ tkinter ya está instalado"
else
    echo "Instalando tkinter..."
    
    case $OS in
        ubuntu|debian|linuxmint|pop)
            sudo apt-get update
            sudo apt-get install -y python3-tk
            ;;
        fedora|rhel|centos)
            sudo dnf install -y python3-tkinter
            ;;
        arch|manjaro)
            sudo pacman -S --noconfirm tk
            ;;
        opensuse*)
            sudo zypper install -y python3-tk
            ;;
        *)
            echo "Distribución no soportada automáticamente"
            echo "Por favor instala python3-tk manualmente"
            exit 1
            ;;
    esac
    
    # Verificar instalación
    if python3 -c "import tkinter" 2>/dev/null; then
        echo "✓ tkinter instalado correctamente"
    else
        echo "✗ Error al instalar tkinter"
        exit 1
    fi
fi

echo ""
echo "=========================================="
echo "  Instalación completada"
echo "=========================================="
echo ""
echo "Ahora puedes ejecutar:"
echo "  Terminal: sudo python3 script_linux_terminal.py"
echo "  Gráfico:  sudo python3 script_linux_gui.py"
echo ""
