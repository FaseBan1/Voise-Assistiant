import tkinter as tk
import time
import subprocess
from contextlib import redirect_stdout
import sys



class ConsoleOutput(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Вывод консоли в Tkinter")

        self.text_box = tk.Text(self)
        self.text_box.pack(expand=True, fill="both")

        # Перенаправление stdout
        self.stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, message)
        self.text_box.config(state=tk.DISABLED)
        self.text_box.see(tk.END)




def run_python_file(file):
    subprocess.Popen(['python', file])

def open_settings():
    settings_file = 'runva_settings_manager.py'
    run_python_file(settings_file)

def send_message():
    message = entry.get()
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, f"Вы: {message}\n")
    chat_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Голосовой помощник YASY")

clock_label = tk.Label(root, font=('Arial', 24))
clock_label.pack(pady=20)

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

update_clock()

settings_button = tk.Button(root, text='Настроить', command=open_settings)
settings_button.pack(side=tk.LEFT, padx=20, pady=10)

run_button = tk.Button(root, text='Запустить', command=lambda: run_python_file('runva_speechrecognition.py'))  # Укажите путь к файлу Python
run_button.pack(side=tk.RIGHT, padx=20, pady=10)

chat_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
chat_text.pack()

entry = tk.Entry(root, width=40)
entry.pack()


root.mainloop()


