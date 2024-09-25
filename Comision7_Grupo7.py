import tkinter as tk
from tkinter import messagebox


# Funciones para agregar, eliminar, editar y buscar contactos
# Funcion para agregar contacto
def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    direccion = entry_direccion.get()

    if nombre and telefono:
        contactos.append([nombre, telefono, correo, direccion])
        actualizar_lista()
    
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
    else:
        tk.messagebox.showerror("Error", "Debe ingresar nombre y teléfono.")
    


# Funcion para eliminar contacto
def eliminar_contacto():
    selected = listbox_contactos.curselection()
    if selected:
        contactos.pop(selected[0])
        actualizar_lista()


# Funcion para editar un contacto
def editar_contacto():
    selected = listbox_contactos.curselection()
    if selected:
        contactos[selected[0]] = [entry_nombre.get(), entry_telefono.get(), entry_correo.get(), entry_direccion.get()]
        actualizar_lista()


def buscar_contacto():
    busqueda = entry_buscar.get().lower()
    resultado = [c for c in contactos if busqueda in c[0].lower()]  # Buscar en el nombre del contacto
    listbox_contactos.delete(0, tk.END)  # Limpiar la lista de contactos actual
    for contacto in resultado:
        listbox_contactos.insert(tk.END, f"{contacto[0]} - {contacto[1]}")

# Funcion para actualizar lista de contactos
def actualizar_lista():
    listbox_contactos.delete(0, tk.END)
    for contacto in contactos:
        listbox_contactos.insert(tk.END, f"{contacto[0]} - {contacto[1]}")



# Configuracion de la ventana
root = tk.Tk()
root.title("Agenda de Contactos")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="#c4d4ab")

# Fuente
fuente = ("Verdana", 10, "bold")

# Scrollbar para lista de contactos
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de contactos
listbox_contactos = tk.Listbox(root, font=fuente, width=10, height=5, yscrollcommand=scrollbar.set)
listbox_contactos.pack(padx=10, pady=30, fill=tk.BOTH,expand=True)

scrollbar.config(command=listbox_contactos.yview)


contactos = []

# Nombre de contacto
label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()

entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack(pady=5)


# Telefono de contacto
label_telefono = tk.Label(root, text="Teléfono:")
label_telefono.pack()

entry_telefono = tk.Entry(root, width=40)
entry_telefono.pack(pady=5)


# Correo electronico de contacto
label_correo = tk.Label(root, text="Correo electrónico:")
label_correo.pack()

entry_correo = tk.Entry(root, width=40)
entry_correo.pack(pady=5)


# Dirección de contacto:
label_direccion = tk.Label(root, text="Dirección:")
label_direccion.pack()

entry_direccion = tk.Entry(root, width=40)
entry_direccion.pack(pady=5)


# Botones de funcionalidad
# Boton agregar contacto
btn_agregar = tk.Button(root, text="Agregar", bg="#87b091", fg="#eff0d5", font=("Verdana", 10), width=10, height=1, command=agregar_contacto)
btn_agregar.pack()

# Boton eliminar contacto
btn_eliminar = tk.Button(root, text="Eliminar", bg="#87b091", fg="#eff0d5", font=("Verdana", 10), width=10, height=1, command=eliminar_contacto)
btn_eliminar.pack()

# Boton editar contacto
btn_editar = tk.Button(root, text="Editar", bg="#87b091", fg="#eff0d5", font=("Verdana", 10), width=10, height=1, command=editar_contacto)
btn_editar.pack()


# Buscar contacto
label_buscar = tk.Label(root, text="Buscar:")
label_buscar.pack()

entry_buscar = tk.Entry(root, width=40)
entry_buscar.pack(pady=5)


btn_buscar = tk.Button(root, text="Buscar", bg="#87b091", fg="#eff0d5", font=("Verdana", 10), width=15, height=2, command=buscar_contacto)
btn_buscar.pack()

actualizar_lista()

root.mainloop()