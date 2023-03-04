datos = {}
while True:
  print("Hola! selecciona una opcion que quieras realizar (escribe el numero):")
  print("[1]- Registrar nuevo ejemplar")
  print("[2]- Consultas y Reportes")
  print("[3]- Salir")
  op_main = int(input())
  
  if op_main == 1:
    while True:
      identificador = max(datos.key,default=0)+1
      titulo.upper() = input("Dame el nombre del libro: \n")
      autor.upper() = input(f"Dame el autor de {titulo}: \n")
      genero.upper() = input(f"Cual es el genero de {titulo}: \n")
      año_publicacion.upper() = input(f"En que año se publico {titulo}: \n")
      ISBN.upper() = input(f"Cual es el ISBN de {titulo}: \n")
      fecha_adquisicion.upper() = input(f"Cuando se adquirio {titulo}: \n")
      print("Datos cargados!")
      op_registro = int(input("Deseas agregar mas?(clickea enter) \n"))
      if op_registro = "":
        break
  elif op_main == 2:
    while True:
      print("Selecciona una opcion que quieras realizar (escribe el numero):")
      print("[1]- Consulta de titulo")
      print("[2]- Reportes")
      print("[3]- Regresar al menu principal")
      op_consulta = int(input())
      if op_consulta == 1:
        while True:
          print("De que forma deseas buscar el libro?(escribe el numero):")
          print("[1]- Por titulo")
          print("[2]- Por ISBN")
          print("[3]- Regresar al menu anterior")
          op_busqueda = int(input())
          if op_busqueda == 1:

          elif op_busqueda == 2:

          elif op_busqueda == 3:
            break

  elif op_main == 3:
    # Sale del programa
    break
