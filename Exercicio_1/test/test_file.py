import unittest
from Cliente import Cliente
from CarrinhoCompras import CarrinhoCompras
from Produto import Produto
from algoritmos.bubble_sort import BubbleSort

class TestCarrinhoCompras(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(1, "Marcos jeeves", "534.492.318-04", "(99) 99999-9999", "jeeves@example.com")

        self.produto4 = Produto(4, "PS5", "Sony", 4499.99, 2)
        self.produto1 = Produto(1, "AirPods", "Apple", 1229.99, 32)
        self.produto5 = Produto(5, "Golf GTI MK8", "Volkswagen", 220000.00, 1)
        self.produto2 = Produto(2, "Wallet", "LV", 2359.99, 20)
        self.produto3 = Produto(3, "Civic SI", "Honda", 70000.00, 2)

        self.carrinho = CarrinhoCompras(self.cliente)

    def test_adicionar_produto(self):
        self.carrinho.adicionar_produto(self.produto1)
        self.assertEqual(len(self.carrinho.produtos), 1)

    def test_remover_produto(self):
        self.carrinho.adicionar_produto(self.produto1)
        self.carrinho.adicionar_produto(self.produto2)
        self.carrinho.remover_produto(self.produto1)
        self.assertEqual(len(self.carrinho.produtos), 1)

    def test_calcular_total(self):
        self.carrinho.adicionar_produto(self.produto1)
        self.carrinho.adicionar_produto(self.produto2)
        total = round(self.carrinho.calcular_total(), 2)
        self.assertEqual(total, 3589.98)
  
    def test_sortProdutos(self):
        self.carrinho.adicionar_produto(self.produto4)  # PS5
        self.carrinho.adicionar_produto(self.produto1)  # AirPods
        self.carrinho.adicionar_produto(self.produto5)  # Golf GTI
        self.carrinho.adicionar_produto(self.produto2)  # Wallet
        self.carrinho.adicionar_produto(self.produto3)  # Civic SI

        # Ordena os produtos no carrinho usando a função sorted() do Python
        self.carrinho.produtos = sorted(self.carrinho.produtos, key=lambda produto: produto.id)

        # Verifica se a ordem dos produtos está correta após a ordenação
        produtos_ordenados = [produto.id for produto in self.carrinho.produtos]
        produtos_esperados = [1, 2, 3, 4, 5] 
        self.assertEqual(produtos_ordenados, produtos_esperados)


if __name__ == '__main__':
    unittest.main()
