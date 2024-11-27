class Recurso:
    def __init__(self, agua=0, dinheiro=0):
        self.agua = agua
        self.dinheiro = dinheiro
        self.sementes = {"trigo": 0}

    def gastar_agua(self, quantidade):
        if self.agua >= quantidade:
            self.agua -= quantidade

    def adicionar_semente(self, tipo, quantidade):
        self.sementes[tipo] += quantidade

    def remover_semente(self, tipo):
        if self.sementes[tipo] > 0:
            self.sementes[tipo] -= 1

    def tem_semente(self, tipo):
        return self.sementes[tipo] > 0

    # def diminuir_colhidos(self, ):

