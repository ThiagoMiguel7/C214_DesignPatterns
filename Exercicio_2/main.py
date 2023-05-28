from Observer import MyObserver
from WordCounter import WordCounter

if __name__ == "__main__":
    frase = input("Digite uma frase:\n")
    palavras = frase.split()
    counter = WordCounter(MyObserver())
    counter.count(palavras)
