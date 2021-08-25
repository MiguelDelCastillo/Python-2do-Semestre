import random
cartas = ['El gallo', 'El diablito', 'La dama', 'El catrin', 'el paraguas', 'la sirena',
          'La escalera', 'la botella',' el bariil', 'el arbol', 'el melon', 'el valiente',
          'El gorrito', 'la muerte', 'la pera', 'la bandera', 'el bandolon', 'el violoncello',
          'la garza', 'el pajaro', 'la mano', 'la bota', 'la luna', 'el cotorro', 'el borracho',
          'El negrito', 'el corazon', 'la sandia', 'el tambor', 'el camaron', 'las jaras', 'el musico',
          'la arania', 'El soldado', 'La estrella', 'El cazo', 'El mundo', 'El apache', 'El nopal',
          'El alacrán', 'La rosa', 'La calavera', 'La campana', 'El cantarito','El venado', 'El sol',
          'La corona', 'La chalupa','El pino','El pescado','La palma','La maceta','El arpa','La rana']
random.shuffle(cartas)

for carta in cartas:
    print(f"Corre y corre, que se va corriendo . . .: {carta}")
    respuesta = int(input("Buenas? (1:Si/0:No)"))
    if respuesta == 1:
        print("FELICIDADES!")
        break
else:
    print("Las cartas se han agrotado, hay que jugar nuevamente")
    
    