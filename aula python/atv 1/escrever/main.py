frase = input("digite a frase: " )

def escrever():
    with open("texto.txt", "w") as arquivo:
        arquivo.write(frase)
escrever()