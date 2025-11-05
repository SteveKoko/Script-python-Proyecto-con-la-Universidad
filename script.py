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
        root.withdraw()
        
        while True:
            try:
                interval = tk.simpledialog.askinteger(
                    "Configuración del Monitor de Inactividad",
                    "Ingrese el intervalo en minutos para las verificaciones de actividad:\n(ej., 15 para cada 15 minutos)",
                    minvalue=1,
                    maxvalue=1440
                )
                
                if interval is None:
                    sys.exit()
                
                self.interval_minutes = interval
                root.destroy()
                return interval
            except:
                messagebox.showerror("Error", "Por favor ingrese un número válido")
    
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
        dialog.geometry("400x200")
        dialog.attributes('-topmost', True)
        
        # Centrar la ventana
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (200 // 2)
        dialog.geometry(f"400x200+{x}+{y}")
        
        # Etiqueta de advertencia
        label = tk.Label(
            dialog,
            text="¿Sigues ahí?\n\n¡El ordenador se apagará si no respondes!",
            font=("Arial", 12),
            fg="red"
        )
        label.pack(pady=20)
        
        # Etiqueta de cuenta regresiva
        countdown_label = tk.Label(
            dialog,
            text="60",
            font=("Arial", 24, "bold"),
            fg="red"
        )
        countdown_label.pack(pady=10)
        
        # Botón de respuesta
        button = tk.Button(
            dialog,
            text="¡Sí, estoy aquí!",
            command=lambda: self.cancel_shutdown(dialog),
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            padx=20,
            pady=10
        )
        button.pack(pady=10)
        
        # Lógica de cuenta regresiva
        remaining_time = [60]  # Usar lista para permitir modificación en función anidada
        
        def update_countdown():
            if remaining_time[0] > 0 and not self.response_received:
                remaining_time[0] -= 1
                countdown_label.config(text=str(remaining_time[0]))
                dialog.after(1000, update_countdown)
            elif remaining_time[0] == 0 and not self.response_received:
                dialog.destroy()
        
        # Iniciar visualización de cuenta regresiva
        dialog.after(1000, update_countdown)
        
        # Programar apagado después de 60 segundos
        self.shutdown_timer = threading.Timer(60.0, self.shutdown_computer)
        self.shutdown_timer.start()
        
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