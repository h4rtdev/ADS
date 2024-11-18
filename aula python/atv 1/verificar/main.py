frase = input("DIGITE UMA FRASE:" )

def verificar_inicio():
    if frase.startswith("Olá"):
        print("Inicia com olá")
    else:
        print("Não começa com olá")