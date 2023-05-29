<h1 align="center"> C214 - Design Pattern </h1>
<p>
  <img src="https://img.shields.io/static/v1?label=License&message=MIT&color=00bfff&style=plastic"/>
  
  <img src="https://img.shields.io/static/v1?label=LP&message=Python&color=daa520&style=plastic"/>
  
  <img src="https://img.shields.io/static/v1?label=IDE&message=VsCode&color=9acd32&style=plastic"/>
</p>

### :books: Exercícios Práticos

- Exercício 1: Design Pattern - [Strategy](https://refactoring.guru/design-patterns/strategy)
- Exercício 2: Design Pattern - [Observer](https://refactoring.guru/design-patterns/observer)


### :point_right: Tecnologias

- Linguagem de Programação: Python
- IDE: [Visual Studio Code](https://code.visualstudio.com)

### :heavy_check_mark: Execução

Para executar os projetos, siga as instruções abaixo:

1. Certifique-se de ter o [Python](python.org) instalado em sua máquina.
2. Faça o download do código do GitHub ou clone o repositório: `git clone https://github.com/ThiagoMiguel7/C214_DesignPatterns`. Certifique-se de ter o [Git](https://git-scm.com) instalado.
3. Abra o terminal ou prompt de comando e navegue até o diretório raiz do projeto.
4. Execute o arquivo `Exercicio_1\main.py` para o [Design Pattern Strategy](https://github.com/ThiagoMiguel7/C214_DesignPatterns/blob/main/Exercicio_1/main.py) e o arquivo `Exercicio_2\main.py` para o [Design Pattern Observer](https://github.com/ThiagoMiguel7/C214_DesignPatterns/blob/main/Exercicio_2/main.py).

### :computer: Exercício 01 - Sistema de Ordenar Dados

Este projeto implementa um sistema de ordenação de dados utilizando três algoritmos diferentes: Bubble Sort, Merge Sort e Quick Sort. O sistema permite ao usuário escolher um algoritmo de ordenação e ordenar uma lista de produtos em ordem crescente com base em critérios específicos.

#### Algoritmos de Ordenação
  - Bubble Sort: O algoritmo Bubble Sort  percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem incorreta. Esse processo é repetido até que a lista esteja completamente ordenada de forma crescente.
  - Merge Sort: O algoritmo Merge Sort utiliza a abordagem de "dividir para conquistar". Ele divide a lista em duas metades, recursivamente ordena cada metade e, em seguida, mescla as duas metades em uma única lista ordenada de forma crescente.
  - Quick Sort: O algoritmo Quick Sort  também utiliza a abordagem de "dividir para conquistar". Ele escolhe um elemento pivô na lista e rearranja os elementos de forma que os elementos menores que o pivô fiquem antes dele e os elementos maiores fiquem depois. Em seguida, ele aplica recursivamente o mesmo processo nas duas sublistas resultantes.

#### Estrutura do Projeto
  - `Cliente.py`: definição da classe Cliente.
  - `CarrinhoCompras.py`: definição da classe CarrinhoCompras.
  - `Produto.py`: definição da classe Produto.
  - `sorter.py`: definição da classe abstrata Sorter.
  - `main.py`: arquivo principal que executa o sistema de ordenação.
  - `test_file.py`: arquivo de teste unitário para o sistema.

### :mag: Testes unitários

O sistema inclui testes unitários para verificar o funcionamento correto das funcionalidades.

1. test_adicionar_produto: Verifica se um produto é corretamente adicionado ao carrinho.
2. test_remover_produto: Verifica se um produto é corretamente removido do carrinho.
3. test_calcular_total: Verifica se o cálculo do valor total da compra no carrinho está correto.
4. test_sortProdutos: Verifica se os produtos no carrinho são ordenados corretamente usando um algoritmo de ordenação específico.

Para executar os [testes unitários](https://github.com/ThiagoMiguel7/C214_DesignPatterns/blob/main/Exercicio_1/test/test_file.py), vá para o arquivo `test_file.py`. No terminal ou IDE, execute o arquivo ou os testes individualmente para verificar a funcionalidade correta do sistema.

[![Python - Unittest](https://github.com/ThiagoMiguel7/C214_DesignPatterns/actions/workflows/python-app.yml/badge.svg)](https://github.com/ThiagoMiguel7/C214_DesignPatterns/actions/workflows/python-app.yml)

### :computer: Exercício 02 - Programa Frase

Este projeto implementa um sistema que recebe uma frase e conta o número total de palavras, o número de palavras com quantidade par de caracteres e o número de palavras que começam com letra maiúscula.

#### Estrutura do Projeto
  - `main.py`: Arquivo principal que executa o programa.
  - `Observer.py`: Define a classe abstrata Observer e a classe MyObserver.
  - `WordCounter.py`: Define a classe WordCounter.
  - `test_file.py`: Contém os testes unitários para a classe WordCounter.
 
### :mag: Testes unitários

O sistema inclui testes unitários para verificar o funcionamento correto das funcionalidades.

1. test_count_all_words: Verifica se as contagens são corretas para uma lista de palavras contendo todas as palavras em maiúsculas.
2. test_count_no_words: Verifica se as contagens são corretas para uma lista vazia de palavras.
3. test_count_even_char_words: Verifica se as contagens são corretas para uma lista de palavras com todas as palavras tendo um número par de caracteres.
4. test_count_start_uppercase_words: Verifica se as contagens são corretas para uma lista de palavras com todas as palavras começando com letra maiúscula.

Para executar os [testes unitários](https://github.com/ThiagoMiguel7/C214_DesignPatterns/blob/main/Exercicio_2/test/test_file.py), vá para o arquivo `test_file.py`. No terminal ou IDE, execute o arquivo ou os testes individualmente para verificar a funcionalidade correta do sistema.

[![Python - Unittest](https://github.com/ThiagoMiguel7/C214_DesignPatterns/actions/workflows/python-app.yml/badge.svg)](https://github.com/ThiagoMiguel7/C214_DesignPatterns/actions/workflows/python-app.yml)

### :mens: Autores

:link: https://github.com/Pedro-Balestra

:link: https://github.com/ThiagoMiguel7

:link: https://github.com/wesley-marcos

### :small_blue_diamond: Licença
MIT
