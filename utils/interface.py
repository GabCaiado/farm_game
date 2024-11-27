import pygame

ICONE_DIRT = pygame.image.load("assets/dirt.png")
ICONE_DIRT = pygame.transform.scale_by(ICONE_DIRT, 0.9)
ICONE_AGUA = pygame.image.load("assets/agua.png")
ICONE_DINHEIRO = pygame.image.load("assets/dinheiro.png")

def desenha_tela(tela, fazenda):
    fonte = pygame.font.SysFont(None, 24)

    # Área de informações
    pygame.draw.rect(tela, (0, 100, 0), (0, 0, 800, 100))  # Painel superior

    # icone e texto da água
    tela.blit(ICONE_AGUA, (85, 15))
    texto_agua = fonte.render(f"{fazenda.recursos.agua}", True, (255, 255, 255))
    tela.blit(texto_agua, (50, 15))

    # Ícone e texto do dinheiro
    tela.blit(ICONE_DINHEIRO, (85, 55))
    texto_dinheiro = fonte.render(f"{fazenda.recursos.dinheiro}", True, (255, 255, 255))
    tela.blit(texto_dinheiro, (50, 55))

    # Dirt field
    tela.blit(ICONE_DIRT, (250, 80))

    # Sementes no inventário
    x_semente = 120
    for tipo, qtd in fazenda.recursos.sementes.items():
        if tipo == "trigo":
            # tela.blit(ICONE_TRIGO, (x_semente, 10))
            texto_qtd = fonte.render(f"{qtd}", True, (255, 255, 255))
            tela.blit(texto_qtd, (x_semente + 40, 15))
            x_semente += 80

def desenha_plantacoes(tela, fazenda):
    # Desenha as plantações no campo com base no estágio de crescimento.
    for i, plantacao in enumerate(fazenda.plantacoes):
        x = 220  # Ajusta posição horizontal base(250, 80)
        y = 70  # Ajusta posição vertical
        #print(f"Plantação {i}: Estágio {plantacao.estagio}")

        # Verifique se o estágio está correto
        if 0 <= plantacao.estagio <= 2:
            plant = pygame.transform.scale_by(ICONE_DIRT, 1)
            plant = tela.blit(plantacao.imagens[plantacao.estagio], (x, y)) # Desenha a imagem correspondente
        else:
            print(f"Estágio inválido: {plantacao.estagio}")

