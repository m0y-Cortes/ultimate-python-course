def aplicar_promocion(compras):
    clientes_con_promo = [
        cliente for cliente, monto in compras.items() 
        if monto > 1500
    ]

#MI SOLUCION 100% MIA
#    cuentas_clientes_con_promo = {}
#    nueva_cuenta = 0
#    for nombre_cliente in clientes_con_promo:
#        nueva_cuenta = compras[nombre_cliente]*0.9
#        cuentas_clientes_con_promo[nombre_cliente] = nueva_cuenta    
#La solucion mas "elegante":
    cuentas_clientes_con_promo = {
        cliente:round(monto*0.9, 2)
        for cliente, monto in compras.items()
        if monto > 1500
    }


    return [clientes_con_promo, cuentas_clientes_con_promo]

compras_clientes = {
    'Cliente1': 1801,
    'Cliente2': 1100,
    'Cliente3': 3000,
}
resultado = aplicar_promocion(compras_clientes)
print(resultado)