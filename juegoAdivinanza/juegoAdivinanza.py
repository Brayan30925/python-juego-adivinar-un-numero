import random

def iniciarJuego():
    numeroAdivinar = random.randint(1,100)
    intentos = 0
    encontrado = False
    while not encontrado:
        intentos += 1
        numero= int(input("intente encontrar el numero"))
        if numero is numeroAdivinar:
            print(f"el numero que buscas es {numeroAdivinar} y lo encontrastes en {intentos} intentos")
            encontrado= True
        else:
           
            if numero < numeroAdivinar:
                print(f"el numero a buscar es mayor")    
            else:
                print(f"el numero adivinar es menor")    

iniciarJuego()

