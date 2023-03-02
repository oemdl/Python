from tkinter import *
from tkinter import ttk

producto_descripcion = ""
producto_unidad = ""
producto_precio = 0.0
producto_cantidad = 0
total = 0.0


def btnNuevo_Click() :
    txtCodigo.config(state='normal')
    txtCodigo.focus()

def txtCodigo_Enter(*args) :
    global producto_descripcion, producto_unidad
    global producto_precio, producto_cantidad, total

    txtCantidad.config(state='normal')
    txtCantidad.focus()
    
    productos = open ('varios\productos.txt','r')
    for linea in productos.readlines() :
        producto = linea.split(',')
        producto_descripcion = producto[1]
        producto_unidad = producto[2]
        producto_precio = producto[3]
        producto_cantidad = producto[4]

        if txtCodigo.get() == producto[0] :
            lblProducto.set( f"Producto : {producto_descripcion}\nPrecio : S/ { producto_precio }" )
            break
    else : productos.close()


def txtCantidad_Enter(*args) :
    global producto_descripcion, producto_unidad
    global producto_precio, producto_cantidad, total

    subTotal = float(producto_precio) * int(svCantidad.get())
    total += subTotal
    svTotal.set(f"Total : S/ { format(total,'.2f') }")    
    tblDetalle.insert('', END, text=svCodigo.get(), values=( producto_descripcion,producto_unidad,svCantidad.get(),producto_precio, format(subTotal,'.2f') ) )

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
tblDetalle.place(x=20, y=220, width=550, height=150)
tblDetalle.column('#0', width=50)
tblDetalle.column('#1', width=150)
tblDetalle.column('#2', width=100)
tblDetalle.column('#3', width=80)
tblDetalle.column('#4', width=80)
tblDetalle.column('#5', width=80)

tblDetalle.heading('#0', text='ID')
tblDetalle.heading('#1', text='Descripción')
tblDetalle.heading('#2', text='Unidad')
tblDetalle.heading('#3', text='Cantidad')
tblDetalle.heading('#4', text='Precio')
tblDetalle.heading('#5', text='SubTotal')

scroll = ttk.Scrollbar(frame, orient='vertical', command=tblDetalle.yview )
scroll.place(x=570, y=220, width=15, height=150 )
tblDetalle.configure( yscrollcommand=scroll.set )

svTotal = StringVar()
Label(frame, textvariable=svTotal, anchor=W).place(x=450, y=370, height=25)

window.mainloop()
