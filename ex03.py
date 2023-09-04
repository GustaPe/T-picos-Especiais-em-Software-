
#o jogador deve adivinhar uma palavra de 5 letras. Inicialmente, uma palavra secreta é escolhida aleatoriamente. O jogador tem um número limitado de tentativas para adivinhar a palavra. O código fornece feedback, exibindo a palavra com letras corretas reveladas e letras incorretas, mas sem revelar a posição correta das letras quando erradas. O jogo continua até que o jogador adivinhe corretamente a palavra ou esgote suas tentativas. 

import random

# Função para exibir a palavra oculta com letras corretas reveladas
def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for i, letra in enumerate(palavra):
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

def main():
    # Abre o arquivo com as palavras
    with open('lista_palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.read().splitlines()

    # Filtra as palavras com 5 letras
    palavras_5_letras = [palavra for palavra in palavras if len(palavra) == 5]

    # Escolhe aleatoriamente uma palavra para o jogo
    palavra_secreta = random.choice(palavras_5_letras)

    tentativas = 6
    letras_corretas = set()  # Conjunto para evitar letras duplicadas
    letras_incorretas = []

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra de 5 letras.")

    while tentativas > 0:
        # Exibe a palavra atual com letras corretas reveladas
        palavra_exibida = mostrar_palavra(palavra_secreta, letras_corretas)
        letras_incorretas_str = ', '.join(letras_incorretas)

        print(f"Palavra atual: {palavra_exibida}")
        if letras_incorretas_str:
            print(f"Letras incorretas: {letras_incorretas_str}")

        tentativa = input("Digite uma palavra de 5 letras: ").lower()

        if len(tentativa) == 5:
            if tentativa == palavra_secreta:
                print("Parabéns! Você adivinhou a palavra corretamente.")
                break
            else:
                letras_incorretas.append(tentativa)
                tentativas -= 1

                letras_corretas_temp = set()
                for i in range(5):
                    if tentativa[i] == palavra_secreta[i]:
                        letras_corretas_temp.add(tentativa[i])
                        letras_corretas.update(letras_corretas_temp)

                if letras_corretas_temp:
                    print("Algumas letras corretas estão na resposta.")
        else:
            print("Por favor, digite uma palavra de 5 letras válida.")

    if tentativas == 0:
        print(f"Fim de jogo! A palavra correta era: {palavra_secreta}")

if __name__ == "__main__":
    main()
