import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "desenvolvimento", "inteligencia", "algoritmo"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += "_"
    return exibicao

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_da_palavra = set(palavra)
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    letras_adivinhadas = set()

    vidas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while len(letras_da_palavra) > 0 and vidas > 0:
        print(f"Você tem {vidas} vidas restantes.")
        print("Letras já usadas:", ' '.join(letras_adivinhadas))

        palavra_atual = exibir_palavra(palavra, letras_adivinhadas)
        print("Palavra atual:", ' '.join(palavra_atual))

        palpite = input("Adivinhe uma letra: ").lower()
        if palpite in alfabeto - letras_adivinhadas:
            letras_adivinhadas.add(palpite)
            if palpite in letras_da_palavra:
                letras_da_palavra.remove(palpite)
            else:
                vidas -= 1
                print("Ops! Essa letra não está na palavra.")
        elif palpite in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra!")
        else:
            print("Caractere inválido. Por favor, digite uma letra válida.")

    if vidas == 0:
        print(f"Que pena! Você perdeu. A palavra era {palavra}")
    else:
        print(f"Parabéns! Você acertou a palavra {palavra}!")

if __name__ == "__main__":
    jogo_da_forca()
