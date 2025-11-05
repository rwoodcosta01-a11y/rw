import random

def escolher_palavra():
    """Escolhe uma palavra aleatória de uma categoria."""
    
    categorias = {
        'valesafe': ['valesafe', 'equipamentos', 'loja'],
        'videogame': ['controle', 'xbox', 'playstation', 'jogos'],
        'paises': ['brasil', 'argentina', 'japao', 'alemanha', 'italia']
    }
    categoria = random.choice(list(categorias.keys()))

    palavra = random.choice(categorias[categoria])
    
    return palavra.upper(), categoria.upper()

def desenhar_forca(tentativas_erradas):
    """Retorna uma representação ASCII da forca baseada nos erros."""
    # Lista de "frames" da forca
    # Cada índice (0 a 6) representa o número de erros
    frames_forca = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return frames_forca[tentativas_erradas]

def exibir_estado_jogo(palavra_secreta, letras_corretas, letras_erradas, tentativas_erradas):
    """Mostra o estado atual do jogo para o jogador."""
    
    print(desenhar_forca(tentativas_erradas))
    print(f"Letras erradas: {' '.join(letras_erradas)}")
    print("\n")

    palavra_oculta = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            palavra_oculta += letra + " "
        else:
            palavra_oculta += "_ "
    
    print(f"Palavra: {palavra_oculta}")
    print("\n")

def jogar():
    """O loop principal do jogo da forca."""
    
    palavra_secreta, categoria = escolher_palavra()
    letras_corretas = set() 
    letras_erradas = set()
    tentativas_erradas = 0
    max_tentativas = 6 

    print("=== BEM-VINDO AO JOGO DA FORCA ===")
    print(f"Dica: A categoria é {categoria}")

    jogo_terminou = False
    while not jogo_terminou:
        
        exibir_estado_jogo(palavra_secreta, letras_corretas, letras_erradas, tentativas_erradas)

        palpite = input("Digite uma letra: ").upper()
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas UMA letra válida.")
            continue
        
        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra_secreta:
            letras_corretas.add(palpite)
            print(f"Bom palpite! A letra '{palpite}' está na palavra.")
        else:
            letras_erradas.add(palpite)
            tentativas_erradas += 1
            print(f"Que pena! A letra '{palpite}' NÃO está na palavra.")


        venceu = True
        for letra in palavra_secreta:
            if letra not in letras_corretas:
                venceu = False
                break
        
        if venceu:
            print(f"\nPARABÉNS! Você venceu! A palavra era {palavra_secreta}.")
            jogo_terminou = True
        
        if tentativas_erradas >= max_tentativas:
            exibir_estado_jogo(palavra_secreta, letras_corretas, letras_erradas, tentativas_erradas)
            print(f"\nVOCÊ PERDEU! A palavra era {palavra_secreta}.")
            jogo_terminou = True


if __name__ == "__main__":
    jogar()
    while True:
        resposta = input("\nDeseja jogar novamente? (S/N): ").upper()
        if resposta == 'S':
            jogar()
        elif resposta == 'N':
            print("Obrigado por jogar!")
            break
        else:
            print("Resposta inválida. Digite 'S' ou 'N'.")