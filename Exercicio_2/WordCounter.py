class WordCounter:
    def __init__(self, observer):
        self.observer = observer

    def count(self, words):
        allWordsCount = len(words)      #Total de palavras
        evenCharWordsCount = 0          #Total palavras com quantidade par
        startUppercaseWordsCount = 0    #Total palavras com letra maiuscula 
        for word in words:
            if len(word) % 2 == 0:
                evenCharWordsCount += 1
            if word.istitle():
                startUppercaseWordsCount += 1
        self.observer.observe(
            "\nTotal de palavras: " + str(allWordsCount) +
            "\nTotal de palavras com quantidade par de caracteres: " + str(evenCharWordsCount) +
            "\nTotal de palavras começadas com letra maiúscula: " + str(startUppercaseWordsCount)
        )
