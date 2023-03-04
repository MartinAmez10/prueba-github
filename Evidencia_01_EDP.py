datos = {}
while True:
  print("Hola! selecciona una opcion que quieras realizar (escribe el numero):")
  print("[1]- Registrar nuevo ejemplar")
  print("[2]- Consultas y Reportes")
  print("[3]- Salir")
  op = int(input())
  if op == 1:
    # agrega datos
    identificador = max(datos.key,default=0)+1
    titulo.upper = input("Dame el nombre del libro: \n")
    autor.upper = input(f"Dame el autor de {titulo}: \n")
    genero.upper = input(f"Cual es el genero de {titulo}: \n")
    año_publicacion.upper = input(f"En que año se publico {titulo}: \n")
    ISBN.upper = input(f"Cual es el ISBN de {titulo}: \n")
    fecha_adquisicion.upper = input(f"Cuando se adquirio {titulo}: \n")
  if op == 2:
    # consulta los datos guardados
  if op == 3:
    break
