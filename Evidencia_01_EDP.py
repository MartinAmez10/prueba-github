datos = {}
while True:
  print("Hola! selecciona una opcion que quieras realizar (escribe el numero):")
  print("[1]- Registrar nuevo ejemplar")
  print("[2]- Consultas y Reportes")
  print("[3]- Salir")
  op_main = int(input())
  
  if op_main == 1:
    # Registro de datos
    while True:
      identificador = max(datos, default=0)+1
      titulo = input("Dame el nombre del libro: \n").upper()
      autor = input(f"Dame el autor de {titulo}: \n").upper()
      genero = input(f"Cual es el genero de {titulo}: \n").upper()
      año_publicacion = input(f"En que año se publico {titulo}: \n").upper()
      ISBN = input(f"Cual es el ISBN de {titulo}: \n").upper()
      fecha_adquisicion = input(f"Cuando se adquirio {titulo}: \n").upper()
      print("Datos cargados!")
      op_registro = input("Deseas agregar mas?(clickea enter) \n")
      if op_registro == "":
        break
      else:
        datos[identificador] = [titulo,autor,genero,año_publicacion,ISBN,fecha_adquisicion]
  elif op_main == 2:
    # Consultas y Reportes
    while True:
      print("Selecciona una opcion que quieras realizar (escribe el numero):")
      print("[1]- Consulta de titulo")
      print("[2]- Reportes")
      print("[3]- Regresar al menu principal")
      op_consulta = int(input())
      
      # Separamos por la opción seleccionada
      if op_consulta == 1:
        # Consulta de título o ISBN
        while True:
          print("De que forma deseas buscar el libro?(escribe el numero):")
          print("[1]- Por titulo")
          print("[2]- Por ISBN")
          print("[3]- Regresar al menu anterior")
          op_busqueda = int(input())
          if op_busqueda == 1:
            for key in datos:
              print(datos[identificador])
          elif op_busqueda == 2:
            print('ISBN')
          elif op_busqueda == 3:
            break
      elif op_consulta == 2:
        # Reportes tabulados
        print('Reportes')
      elif op_consulta == 3:
        print('Volviendo al menú principal . . .')
        break

  elif op_main == 3:
    # Sale del programa
    break