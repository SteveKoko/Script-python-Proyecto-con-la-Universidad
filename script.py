import tkinter as tk
from tkinter import messagebox
import time
import os
import sys
import threading

class InactivityMonitor:
    def __init__(self):
        self.interval_minutes = 0
        self.response_received = False
        self.shutdown_timer = None
        
    def get_interval(self):
        """Pide al usuario el intervalo de verificación"""
        root = tk.Tk()
        root.title("Configuración del Monitor")
        root.geometry("450x250")
        root.configure(bg="#2b2b2b")
        root.resizable(False, False)
        
        # Centrar la ventana
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (450 // 2)
        y = (root.winfo_screenheight() // 2) - (250 // 2)
        root.geometry(f"450x250+{x}+{y}")
        
        # Borde amarillo brillante
        border_frame = tk.Frame(root, bg="#FFD700", bd=0)
        border_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        inner_frame = tk.Frame(border_frame, bg="#2b2b2b", bd=0)
        inner_frame.place(x=4, y=4, relwidth=1, relheight=1, width=-8, height=-8)
        
        # Título
        title_label = tk.Label(
            inner_frame,
            text="Configuración del Monitor de Inactividad",
            font=("Segoe UI", 14, "bold"),
            fg="#FFD700",
            bg="#2b2b2b"
        )
        title_label.pack(pady=(20, 10))
        
        # Etiqueta de instrucción
        instruction_label = tk.Label(
            inner_frame,
            text="Ingrese el intervalo en minutos para verificaciones:\n(ej., 15 para cada 15 minutos)",
            font=("Segoe UI", 10),
            fg="#e0e0e0",
            bg="#2b2b2b",
            justify="center"
        )
        instruction_label.pack(pady=10)
        
        # Frame para entrada
        entry_frame = tk.Frame(inner_frame, bg="#2b2b2b")
        entry_frame.pack(pady=10)
        
        entry_var = tk.StringVar()
        entry = tk.Entry(
            entry_frame,
            textvariable=entry_var,
            font=("Segoe UI", 12),
            width=10,
            bg="#3d3d3d",
            fg="#ffffff",
            insertbackground="#FFD700",
            relief="flat",
            justify="center"
        )
        entry.pack(pady=5)
        
        error_label = tk.Label(
            inner_frame,
            text="",
            font=("Segoe UI", 9),
            fg="#ff4444",
            bg="#2b2b2b"
        )
        error_label.pack()
        
        def validate_and_start():
            try:
                interval = int(entry_var.get())
                if 1 <= interval <= 1440:
                    self.interval_minutes = interval
                    root.destroy()
                else:
                    error_label.config(text="Por favor ingrese un número entre 1 y 1440")
            except ValueError:
                error_label.config(text="Por favor ingrese un número válido")
        
        # Frame para botones
        buttons_frame = tk.Frame(inner_frame, bg="#2b2b2b")
        buttons_frame.pack(pady=10)
        
        # Botón de confirmar
        start_button = tk.Button(
            buttons_frame,
            text="Iniciar Monitor",
            command=validate_and_start,
            font=("Segoe UI", 11, "bold"),
            bg="#FFD700",
            fg="#2b2b2b",
            activebackground="#FFC700",
            activeforeground="#2b2b2b",
            relief="flat",
            padx=30,
            pady=8,
            cursor="hand2"
        )
        start_button.pack(side="left", padx=5)
        
        # Botón de salir
        exit_button = tk.Button(
            buttons_frame,
            text="Salir",
            command=lambda: (root.destroy(), sys.exit()),
            font=("Segoe UI", 11, "bold"),
            bg="#e74c3c",
            fg="#ffffff",
            activebackground="#c0392b",
            activeforeground="#ffffff",
            relief="flat",
            padx=30,
            pady=8,
            cursor="hand2"
        )
        exit_button.pack(side="left", padx=5)
        
        entry.bind('<Return>', lambda e: validate_and_start())
        entry.focus()
        
        root.protocol("WM_DELETE_WINDOW", lambda: (root.destroy(), sys.exit()))
        root.mainloop()
        
        return self.interval_minutes
    
    def shutdown_computer(self):
        """Apaga el ordenador con Windows"""
        time.sleep(3)
        os.system("shutdown /s /t 0")
    
    def cancel_shutdown(self, dialog):
        """El usuario respondió - cancelar el apagado"""
        self.response_received = True
        if self.shutdown_timer:
            self.shutdown_timer.cancel()
        dialog.destroy()
    
    def create_activity_dialog(self):
        """Crea el diálogo de verificación de actividad"""
        self.response_received = False
        
        dialog = tk.Tk()
        dialog.title("Verificación de Actividad")
        dialog.geometry("550x480")
        dialog.configure(bg="#2b2b2b")
        dialog.attributes('-topmost', True)
        dialog.resizable(False, False)
        
        # Centrar la ventana
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (550 // 2)
        y = (dialog.winfo_screenheight() // 2) - (480 // 2)
        dialog.geometry(f"550x480+{x}+{y}")
        
        # Borde amarillo brillante
        border_frame = tk.Frame(dialog, bg="#FFD700", bd=0)
        border_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        inner_frame = tk.Frame(border_frame, bg="#2b2b2b", bd=0)
        inner_frame.place(x=4, y=4, relwidth=1, relheight=1, width=-8, height=-8)
        
        # Etiqueta de advertencia
        label = tk.Label(
            inner_frame,
            text="¿Sigues ahí?",
            font=("Segoe UI", 20, "bold"),
            fg="#FFD700",
            bg="#2b2b2b"
        )
        label.pack(pady=(35, 15))
        
        warning_label = tk.Label(
            inner_frame,
            text="¡El ordenador se apagará si no respondes!",
            font=("Segoe UI", 13),
            fg="#ff6b6b",
            bg="#2b2b2b"
        )
        warning_label.pack(pady=8)
        
        # Etiqueta de cuenta regresiva
        countdown_label = tk.Label(
            inner_frame,
            text="60",
            font=("Segoe UI", 52, "bold"),
            fg="#FFD700",
            bg="#2b2b2b"
        )
        countdown_label.pack(pady=25)
        
        # Botón principal amarillo
        button_frame = tk.Frame(inner_frame, bg="#2b2b2b")
        button_frame.pack(pady=20)
        
        response_button = tk.Button(
            button_frame,
            text="¡Sí, estoy aquí!",
            command=lambda: self.cancel_shutdown(dialog),
            font=("Segoe UI", 15, "bold"),
            bg="#FFD700",
            fg="#2b2b2b",
            activebackground="#FFC700",
            activeforeground="#2b2b2b",
            relief="raised",
            bd=3,
            cursor="hand2",
            padx=55,
            pady=18
        )
        response_button.pack()
        
        # Botón de salir
        exit_frame = tk.Frame(inner_frame, bg="#2b2b2b")
        exit_frame.pack(pady=20)
        
        def exit_program():
            self.response_received = True
            if self.shutdown_timer:
                self.shutdown_timer.cancel()
            dialog.destroy()
            sys.exit()
        
        exit_button = tk.Button(
            exit_frame,
            text="Salir",
            command=exit_program,
            font=("Segoe UI", 11, "bold"),
            bg="#e74c3c",
            fg="#ffffff",
            activebackground="#c0392b",
            activeforeground="#ffffff",
            relief="raised",
            bd=2,
            cursor="hand2",
            padx=50,
            pady=12
        )
        exit_button.pack()
        
        # Lógica de cuenta regresiva
        remaining_time = [60]
        
        def update_countdown():
            if remaining_time[0] > 0 and not self.response_received:
                remaining_time[0] -= 1
                countdown_label.config(text=str(remaining_time[0]))
                
                # Cambiar color cuando quedan menos de 10 segundos
                if remaining_time[0] <= 10:
                    countdown_label.config(fg="#ff4444")
                
                dialog.after(1000, update_countdown)
            elif remaining_time[0] == 0 and not self.response_received:
                dialog.destroy()
        
        # Iniciar visualización de cuenta regresiva
        dialog.after(1000, update_countdown)
        
        # Programar apagado después de 60 segundos
        self.shutdown_timer = threading.Timer(60.0, self.shutdown_computer)
        self.shutdown_timer.start()
        
        dialog.protocol("WM_DELETE_WINDOW", lambda: None)
        dialog.mainloop()
    
    def run(self):
        """Bucle principal de monitoreo"""
        interval = self.get_interval()
        
        try:
            while True:
                # Esperar el intervalo especificado
                time.sleep(interval * 60)
                
                # Mostrar diálogo de actividad
                self.create_activity_dialog()
                
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    import tkinter.simpledialog
    
    monitor = InactivityMonitor()
    monitor.run()