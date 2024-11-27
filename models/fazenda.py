from models.plantacao import Plantacao
from models.recurso import Recurso
from models.loja import Loja


class Fazenda:
    def __init__(self):
        self.recursos = Recurso(agua=150, dinheiro=50)
        self.plantacoes = []
        self.loja = Loja()

    def plantar(self, tipo_semente):
        if self.recursos.agua >= 10 and self.recursos.tem_semente(tipo_semente):
            nova_plantacao = Plantacao("trigo", agua_necessaria=2)
            self.plantacoes.append(nova_plantacao)  # Adiciona nova plantacao
            print(f"Plantação adicionada: {nova_plantacao.tipo}, Estágio: {nova_plantacao.estagio}")
            self.recursos.gastar_agua(5)
            self.recursos.remover_semente(tipo_semente)
        else:
            print("Recursos insuficientes!")

    def colher(self):
        colhidos = []
        for plantacao in self.plantacoes:
            resultado = plantacao.colher()
            if resultado:  # Apenas adiciona se não for `None`
                colhidos.append(resultado)

        # Remove plantações colhidas
        self.plantacoes = [p for p in self.plantacoes if not p.colhido]
        return colhidos

    def atualizar(self):
        for plantacao in self.plantacoes:
            plantacao.atualizar()
