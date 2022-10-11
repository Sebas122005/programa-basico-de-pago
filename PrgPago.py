import datetime,os

print("Programa de Pago")

s_total=0
name_empleado=input("Ingresar nombre : ")
sueldo_in = float(input("Ingresar sueldo : "))
a_ingreso=int(input("Ingresar año de ingreso : "))
n_hijos= int(input("Ingresar numero de hijos : "))
a_actual = ((datetime.datetime.now()).date()).strftime("%Y")

tiempo_trabajo=int(a_actual)-a_ingreso
s_total=200*n_hijos


sueldo=sueldo_in-100

if tiempo_trabajo < 10:
    s_total=s_total+(sueldo*2)
elif tiempo_trabajo>=10 and tiempo_trabajo<=20:
    s_total=s_total+(sueldo*3)
elif tiempo_trabajo>=20:
    s_total=s_total+(sueldo*4)

print(f'''-----------------Voucher-------------------
Nombre empleado : {name_empleado}
Sueldo Ingresado: {sueldo_in}
Descuento por Vacaciones : 100
Año de Ingreso : {a_ingreso}
Hijos : {n_hijos}
Pago Total a Pagar : {s_total}
Fecha Actual : {datetime.datetime.now()}
''')

