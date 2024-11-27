class Loja:
    PRECOS = {"trigo": 5}

    def comprar(self, tipo, recurso):
        preco = self.PRECOS[tipo]
        if recurso.dinheiro >= preco:
            recurso.dinheiro -= preco
            recurso.adicionar_semente(tipo, 1)

    def vender(self, tipo, recurso):
        preco = self.PRECOS[tipo]
        recurso.dinheiro += preco
