from CarrinhoCompras import CarrinhoCompras
from Cliente import Cliente
from Produto import Produto
from algoritmos.bubble_sort import BubbleSort
from algoritmos.merge_sort import MergeSort
from algoritmos.quick_sort import QuickSort

if __name__ == "__main__":

    # Criando o cliente
    cliente = Cliente(1, "Marcos jeeves", "534.492.318-04", "(99) 99999-9999", "jeeves@example.com")

    # Criando os produtos
    produto4 = Produto(4, "PS5", "Sony", 4499.99, 2)
    produto1 = Produto(1, "AirPods", "Apple", 1229.99, 32)
    produto5 = Produto(5, "Golf GTI MK8", "Volkswagen", 220000.00, 1)
    produto2 = Produto(2, "Wallet", "LV", 2359.99, 20)
    produto3 = Produto(3, "Civic SI", "Honda", 70000.00, 2)

    # Criando o carrinho de compras
    carrinho = CarrinhoCompras(cliente)

    # Adicionando produtos ao carrinho
    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    carrinho.adicionar_produto(produto3)
    carrinho.adicionar_produto(produto4)
    carrinho.adicionar_produto(produto5)

    while True:
        print("Selecione uma opção: \n")
        print("1. Ordenação - BubbleSort ")
        print("2. Ordenação - MergeSort")
        print("3. Ordenação - QuickSort")
        escolha = input("Digite o número da opção desejada: ")

        if escolha.isdigit():
            escolha = int(escolha)
            if escolha >= 1 and escolha <= 3:
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 3.")
        else:
            print("\nEntrada inválida. Por favor, digite um número.")

    if escolha == 1:
        carrinho.sortProdutos(BubbleSort())
    elif escolha == 2:
        carrinho.sortProdutos(MergeSort())
    else:
        carrinho.sortProdutos(QuickSort())

    carrinho.exibir_detalhes()