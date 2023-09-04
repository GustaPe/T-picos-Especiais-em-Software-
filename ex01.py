
#Este código implementa um jogo da velha em um tabuleiro 4x4, onde dois jogadores se alternam fazendo jogadas. O tabuleiro é exibido após cada jogada, e as coordenadas do jogador são validadas para garantir que sejam legais. O jogo continua até que um jogador vença com 4 símbolos em linha, coluna ou diagonal ou até que o tabuleiro esteja completamente preenchido, resultando em um empate.

# Função para imprimir o tabuleiro do jogo
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        # Imprime cada linha do tabuleiro com uma barra vertical (|) entre os elementos
        print(" |  ".join(linha))
        # Imprime uma linha horizontal para separar as linhas
        print("-" * 17)

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    for i in range(4):
        # Verifica se o jogador venceu em qualquer linha ou coluna
        if all(tabuleiro[i][j] == jogador for j in range(4)) or all(tabuleiro[j][i] == jogador for j in range(4)):
            return True
    
    # Verifica se o jogador venceu em alguma das duas diagonais
    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    # Se não houver vitória, retorna False
    return False

if __name__ == "__main__":
    # Inicializa o tabuleiro com espaços em branco
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    # Define o jogador atual como "O"
    jogador_atual = "O"
    
    while True:
        # Chama a função para imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)
        # Exibe o jogador atual
        print(f"Jogador {jogador_atual}, é sua vez.")
        
        while True:
            try:
                # Solicita a entrada do jogador para escolher a linha e a coluna
                linha, coluna = map(int, input("Escolha a linha e a coluna (1-4): ").split())
                # Verifica se a entrada está dentro dos limites do tabuleiro e se a célula está vazia
                if 1 <= linha <= 4 and 1 <= coluna <= 4 and tabuleiro[linha - 1][coluna - 1] == " ":
                    break
                else:
                    # Caso a entrada seja inválida, exibe uma mensagem de erro
                    print("Movimento inválido! Use os números de 1 a 4 separados por espaço.")
                    print("Exemplo: 2 3")
            except ValueError:
                # Caso a entrada não seja reconhecida como números separados por espaço, exibe um erro
                print("Movimento não reconhecido! Use dois números separados por espaço.")
                print("Exemplo: 2 3")
                
        # Atualiza o tabuleiro com a marca do jogador atual
        tabuleiro[linha - 1][coluna - 1] = jogador_atual
        
        # Verifica se o jogador atual venceu
        if verificar_vitoria(tabuleiro, jogador_atual):
            # Se sim, exibe o tabuleiro atualizado e a mensagem de vitória
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        # Verifica se o jogo terminou em empate
        if all(" " not in linha for linha in tabuleiro):
            # Se todas as células estiverem preenchidas e nenhum jogador venceu, exibe empate
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break
        
        # Alterna o jogador atual entre "X" e "O"
        jogador_atual = "X" if jogador_atual == "O" else "O"
