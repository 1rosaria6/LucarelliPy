

class calcComb:


    def __init__(self,stringa):

        self.__stringa = stringa
        self.stringalist =list(stringa)

    def getStringa(self):
        return self.__stringa

    def getStringalist(self):
        return self.stringalist

    def setStringa(self, str):
        self.__stringa = str
        self.stringalist = list(str)

    def permutazioni(self,k):
        return len(self.__stringa)**k

    def verifica(self):
        open words.italian.txt
        if self.__stringa in words.italian.txt:
            print("la parola esiste")
        if self.stringa not in words.italian.txt:
            print("la parola non esiste")
