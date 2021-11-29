Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # classe calcolo combinatorio

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)
        self.__anagrammi = anagrammi(self.__stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        
        self.__stringa = str
        self.stringalist = list(str)
        
        return 0

    def charRipetuti(self):
        
        print (stella)
        stella = { "s":0, "t":0, "e":0, "l":2, "a":0}
        print ("stella: ",stella,'\n' )

        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''

    def cerca(str):
        
        open words.italian.txt
        if self.__stringa in words.italian.txt:
            print("la parola esiste")
        if self.__stringa not in word.italian.txt:
            print("la parola non esiste")
        
        pass

    'Rosaria = calcComb("Rosaria studia")'
    'print(Rosaria.permutazioni(3))'
    'print(Rosaria.stringa)'
    'print(Rosaria.getStringa())'
    'Rosaria.setStringa("stella")'
    'print(Rosaria.stringa)'
    'print(Rosaria.stringalist)'

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        questo metodo può essere omessa se si utilizza un metodo built in delle
        librerie standard
        '''

    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        questo metodo può essere evitato se ri richiama una delle funzioni built in
        delle librerie standard
        '''
        pass

    def anagrammi(self):
        '''
        a partire dalla stringa (caratterizzante l'oggetto) si restituisca la lista di tutti
        gli anagrammi possibili. E' presente uno script nel repo che esegue questo compito.
        '''
        pass
    
    def confUtil(self):
        '''
        confUtil mette insieme diversi metodi basilari, lo scopo è:
        a partire dalla lista di tutti gli anagrammi, verifica parola per parola la sua
        presenza all'interno del file delle parole di senso compiuto, cancellando le altre.
        si consiglia l'utilizzo di anagrammi e cerca, presenti nel repo e da trasformare in metodi.
        è possibile in una seconda versione la ricefrca di parole in altre lingue. 
        '''
        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        return 0

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        return 0

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        return 0

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        '''
        restituire il numero delle combinazioni SENZA ripetizione
        '''
        return 0

    def nCombSemplConRip(self):
        '''
        restituire il numero delle combinazioni CON ripetizione
        '''
        return 0

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0

    # PROBABILITA'

    def probConfUtil(self):
        pass