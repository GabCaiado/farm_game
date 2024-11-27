import pygame
from models.fazenda import Fazenda
from utils.interface import desenha_tela
from utils.interface import desenha_plantacoes


LARGURA, ALTURA = 800, 600


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Simulador de Fazenda")
    clock = pygame.time.Clock()

    fazenda = Fazenda()
    colhidos = []

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:  # Plantar trigo
                    fazenda.plantar("trigo")

                elif evento.key == pygame.K_c:  # Colher plantações prontas
                    colhidos = fazenda.colher()
                    for produto in colhidos:
                            print(f"Você colheu: {produto}")
                elif evento.key == pygame.K_b:  # Comprar semente de trigo
                    fazenda.loja.comprar("trigo", fazenda.recursos)
                elif evento.key == pygame.K_v:  # Vender produtos colhidos
                    if colhidos:
                        fazenda.loja.vender("trigo", fazenda.recursos)

                    else:
                        print("Sem plantacao para vender.")

        fazenda.atualizar()

        # Desenhar elementos na tela
        tela.fill((0, 150, 0))  # Cor de fundo
        desenha_tela(tela, fazenda)
        desenha_plantacoes(tela, fazenda)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
