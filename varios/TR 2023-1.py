from tkinter import *
from tkinter import ttk

def btnNuevo_Click() :
    txtCodigo.config(state='normal')
    txtCodigo.focus()

def txtCodigo_Enter(*args) :
    txtCantidad.config(state='normal')
    txtCantidad.focus()
    #Buscar en archivo de texto el producto

def txtCantidad_Enter(*args) :
    tblDetalle.insert('', END, text=svCodigo.get(), values=( '','','',svCantidad.get(),''))
    

    txtCodigo.config(state='disabled')
    txtCantidad.config(state='disabled')
    svCodigo.set('')
    svCantidad.set('')


window = Tk()
window.title("Ferreteria el Tornillo Feliz")
window.resizable(0,0)
#window.iconbitmap("logo.ico")

frame = Frame(window, width=600, height=400 )
frame.pack()

Label(frame, text='Dni : ', anchor=W).place(x=30, y=30, width=80, height=25)
txtDni = Entry(frame)
txtDni.place(x=120, y=30, width=80, height=25)

Label(frame, text='Apellidos : ', anchor=W).place(x=30, y=60, width=80, height=25)
txtApellidos = Entry(frame)
txtApellidos.place(x=120, y=60, width=120, height=25)

Label(frame, text='Nombres : ', anchor=W).place(x=250, y=60, width=80, height=25)
txtNombres = Entry(frame)
txtNombres.place(x=340, y=60, width=120, height=25)

Label(frame, text='Dirección : ', anchor=W).place(x=30, y=90, width=80, height=25)
txtDireccion = Entry(frame)
txtDireccion.place(x=120, y=90, width=150, height=25)

Label(frame, text='Telefóno : ', anchor=W).place(x=30, y=120, width=80, height=25)
txtTelefono = Entry(frame)
txtTelefono.place(x=120, y=120, width=100, height=25)

svCodigo = StringVar()
Label(frame, text='Código : ', anchor=W).place(x=30, y=180, width=50, height=25)
txtCodigo = Entry(frame)
txtCodigo.config(state='disabled', textvariable=svCodigo)
txtCodigo.place(x=90, y=180, width=50, height=25)
txtCodigo.bind("<Return>", txtCodigo_Enter)

lblProducto = StringVar()
Label(frame, textvariable=lblProducto, anchor=W).place(x=150, y=180, width=200, height=25)

svCantidad = StringVar()
Label(frame, text='Cantidad : ', anchor=W).place(x=360, y=180, width=60, height=25)
txtCantidad = Entry(frame)
txtCantidad.config(state='disabled', textvariable=svCantidad)
txtCantidad.place(x=430, y=180, width=50, height=25)
txtCantidad.bind("<Return>", txtCantidad_Enter)

btnNuevo = Button(frame, text='Nuevo', command=btnNuevo_Click, cursor='hand2').place(x=500, y=180, width=80, height=25)

tblDetalle = ttk.Treeview(frame, columns=('id','Descripcion','Unidad','Cantidad','Precio','SubTotal'))
tblDetalle.place(x=20, y=220, width=550, height=300)
tblDetalle.column('#0', width=50)
tblDetalle.column('#1', width=150)
tblDetalle.column('#2', width=50)
tblDetalle.column('#3', width=50)
tblDetalle.column('#4', width=80)
tblDetalle.column('#5', width=80)

tblDetalle.heading('#1', text='Descripción')
tblDetalle.heading('#2', text='Unidad')
tblDetalle.heading('#3', text='Cantidad')
tblDetalle.heading('#4', text='Precio')
tblDetalle.heading('#5', text='SubTotal')

#lblTotal = Label(frame, text='Total = S/', anchor=W).place(x=300, y=280, height=25)


window.mainloop()
