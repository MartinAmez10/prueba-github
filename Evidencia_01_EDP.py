datos = {}
while True:
  print("Hola! selecciona una opcion que quieras realizar (escribe el numero):")
  print("[1]- Registrar nuevo ejemplar")
  print("[2]- Consultas y Reportes")
  print("[3]- Salir")
  op = int(input())
  if op == 1:
    # agrega datos
    identificador = int(input("Dame la clave: \n"))
    if identificador in datos:
      print("esa clave ya existe")
      break
  if op == 2:
    # consulta los datos guardados
  if op == 3:
    break
