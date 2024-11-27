import pygame

class Plantacao:
    def __init__(self, tipo, agua_necessaria):
        self.tipo = tipo
        self.agua_necessaria = agua_necessaria
        self.agua_atual = 0
        self.estagio = 0  # 0 - Semente, 1 - Broto, 2 - Crescendo
        self.tempo_necessario = 100
        self.tempo_passado = 0
        self.colhido = False  # Vai indicar se ja foi colhido

        try:
            self.imagens = {
                0: pygame.image.load("assets/semente.png"),
                1: pygame.image.load("assets/broto.png"),
                2: pygame.image.load("assets/trigo.png")
            }
        except pygame.error as e:
            print(f"Erro ao carregar imagens: {e}")

    def colher(self):
        # Colhe a plantação se ela estiver no estagio final
        if self.estagio == 2 and not self.colhido:  # so vai colher se estiver madura
            self.colhido = True
            print(f"Plantação de {self.tipo} colhida!")
            return self.tipo  # retorna o tipo
        else:
            print("A plantação ainda não está pronta para colher ou já foi colhida.")
            return None

    def regar(self):
        if self.estagio < 2:
            self.agua_atual += 1
            if self.agua_atual >= self.agua_necessaria:
                self.estagio += 1
                self.agua_atual = 0

    def atualizar(self):
        # Atualiza o estágio de crescimento baseado no tempo
            self.tempo_passado += 1
            if self.tempo_passado >= self.tempo_necessario:
                self.crescer()

    def crescer(self):
        # Avança para o próximo estágio de crescimento
        if self.estagio < 2:
            self.estagio += 1
            self.tempo_passado = 0

    def esta_pronta(self):
        return self.estagio == 2

