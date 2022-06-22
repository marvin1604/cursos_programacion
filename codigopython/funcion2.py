def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return print(apellido, nombre)
    else:
        return print(nombre,apellido)
    
nombre_completo("david", "rodriguez")
nombre_completo("david", "rodriguez", inverso=True)
nombre_completo(apellido="rodriguez",nombre= "david")

