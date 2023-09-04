#Os jogadores escolhem o tamanho do tabuleiro e se alternam em cada jogada, tentando formar uma linha, coluna ou diagonal completa com suas marcações. Eles bloqueiam o adversário e buscam oportunidades de vitória, verificando o resultado após cada jogada. O jogo continua até que alguém vença ou termine em empate.

# Função para criar um tabuleiro de tamanho especificado
def criar_tabuleiro(tamanho):
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

# Função para imprimir o tabuleiro do jogo
def imprimir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)
    for i in range(tamanho):
        # Imprime cada linha do tabuleiro com uma barra vertical (|) entre os elementos
        print(" | ".join(tabuleiro[i]))
        # Imprime uma linha horizontal para separar as linhas (exceto na última linha)
        if i < tamanho - 1:
           print("-" * (4 * tamanho - 1))

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    tamanho = len(tabuleiro)
    for i in range(tamanho):
        # Verifica se o jogador venceu em qualquer linha ou coluna
        if all(tabuleiro[i][j] == jogador for j in range(tamanho)) or all(tabuleiro[j][i] == jogador for j in range(tamanho)):
            return True
    
    # Verifica se o jogador venceu em alguma das duas diagonais
    if all(tabuleiro[i][i] == jogador for i in range(tamanho)) or all(tabuleiro[i][tamanho - 1 - i] == jogador for i in range(tamanho)):
        return True

    # Se não houver vitória, retorna False
    return False

# Função principal para o jogo da velha com tamanho variável
def jogo_da_velha(tamanho):
    tabuleiro = criar_tabuleiro(tamanho)  # Cria o tabuleiro com o tamanho especificado
    jogador_atual = "O"  # Define o jogador atual como "O"
    
    while True:
        imprimir_tabuleiro(tabuleiro)  # Imprime o tabuleiro atual
        print(f"Jogador {jogador_atual}, é sua vez.")
        
        while True:
            try:
                # Solicita a entrada do jogador para escolher a linha e a coluna
                linha, coluna = map(int, input(f"Escolha a linha e a coluna (1-{tamanho}): ").split())
                # Verifica se a entrada está dentro dos limites do tabuleiro e se a célula está vazia
                if 1 <= linha <= tamanho and 1 <= coluna <= tamanho and tabuleiro[linha - 1][coluna - 1] == " ":
                    break
                else:
                    # Caso a entrada seja inválida, exibe uma mensagem de erro
                    print("Movimento inválido! Use os números de 1 a", tamanho, "separados por espaço.")
                    print(f"Exemplo: 2 3 (para um tabuleiro {tamanho}x{tamanho})")
            except ValueError:
                # Caso a entrada não seja reconhecida como números separados por espaço, exibe um erro
                print("Movimento não reconhecido! Use dois números separados por espaço.")
                print(f"Exemplo: 2 3 (para um tabuleiro {tamanho}x{tamanho})")
                
        tabuleiro[linha - 1][coluna - 1] = jogador_atual  # Atualiza o tabuleiro com a marca do jogador atual
        
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

if __name__ == "__main__":
    # Solicita o tamanho desejado do tabuleiro ao usuário
    tamanho_tabuleiro = int(input("Informe o tamanho do tabuleiro (por exemplo, 3 para 3x3): "))
    # Chama a função do jogo com o tamanho especificado
    jogo_da_velha(tamanho_tabuleiro)
