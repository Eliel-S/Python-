def preparar_datos(info):
 acumulador = " " #poner un espacio para que no se vea amontonado entre ambos textos
 #corrección en el indentado
 for letra in info:
  acumulador += letra + "-"
 return acumulador[:-1]
 #corrección en el indentado
def mezcla_datos(a, b):
 if a > b:
   return a + b
 elif a == b:
   return a * 2
 else:
   return b + a
def iniciar():
 entrada1 = input("Ingresa un valor de referencia textual: ")
 entrada2 = input("Ingresa otra unidad: ")
 #cambio de variables
 a = preparar_datos(entrada1) 
 b = preparar_datos(entrada2)
 #cambio en los argumentos
 resultado = mezcla_datos(a, b)
 print("Resultado: ", resultado)
 #corrección en el indentado
 if entrada1 in entrada2:
   print("Coincidencia detectada.")
iniciar()