import tkinter as tk
from tkinter import ttk, messagebox


class login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.resizable(0, 0)

        # Configurar grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Usuario
        self.__crear__componentes()

    def __crear__componentes(self):
        userLabel = ttk.Label(self, text='Usuario:')
        userLabel.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.userEntry = ttk.Entry(self)
        self.userEntry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        passwordLabel = ttk.Label(self, text='Contraseña:')
        passwordLabel.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.passwordEntry = ttk.Entry(self, show='*')
        self.passwordEntry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        loginBoton = ttk.Button(self, text='Login', command=self._login)
        loginBoton.grid(row=3, column=0, columnspan=2)

    # Func Boton login
    def _login(self):
        messagebox.showinfo('Datos login',
                            f'usuario: {self.userEntry.get()}, contraseña: {self.passwordEntry.get()}')

if __name__ == '__main__':
    login_ventana = login()
    login_ventana.mainloop()
