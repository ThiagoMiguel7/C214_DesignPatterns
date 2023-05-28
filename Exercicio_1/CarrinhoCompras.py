from sorter import Sorter

class CarrinhoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def exibir_detalhes(self):
        print("Detalhes do Cliente:")
        print(self.cliente)

        print("\nProdutos no Carrinho:")
        for produto in self.produtos:
            print(produto)

        print("\nTotal da Compra: R$", round(self.calcular_total(), 2))

    # Metodo de Ordenação (Sort)
    def sortProdutos(self, sorter): 
        if isinstance(sorter, Sorter):
            self.produtos = sorter.sort(self.produtos)

