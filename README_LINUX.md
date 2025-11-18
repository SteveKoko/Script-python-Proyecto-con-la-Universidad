# Monitor de Inactividad - Linux

## Requisitos previos

### Para script_linux_terminal.py
No requiere instalación adicional. Usa bibliotecas estándar de Python.

### Para script_linux_gui.py
Necesita tkinter instalado.

## Instalación de dependencias

### Ubuntu/Debian/Linux Mint:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### Fedora/RHEL/CentOS:
```bash
sudo dnf install python3-tkinter
```

### Arch Linux/Manjaro:
```bash
sudo pacman -S tk
```

### openSUSE:
```bash
sudo zypper install python3-tk
```

## Permisos necesarios

Ambos scripts necesitan **permisos de superusuario (sudo)** para apagar el sistema.

## Ejecución

### Versión Terminal (sin GUI):
```bash
sudo python3 script_linux_terminal.py
```

### Versión Gráfica (con GUI):
```bash
sudo python3 script_linux_gui.py
```

## Notas importantes

1. **Se requiere sudo** porque el comando `shutdown -h now` necesita privilegios de administrador
2. El script de terminal funciona en cualquier distribución Linux sin instalación adicional
3. El script gráfico necesita un entorno de escritorio (GNOME, KDE, XFCE, etc.)
4. Para ejecutar en segundo plano (opcional):
   ```bash
   sudo python3 script_linux_terminal.py &
   ```

## Verificar si tkinter está instalado

```bash
python3 -c "import tkinter; print('tkinter instalado correctamente')"
```

Si muestra un error, necesitas instalar python3-tk según tu distribución.
