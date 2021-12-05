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
        '''
        modificare questo metodo in modo da verificare la coerenza delle variabili di
        istanza presenti
        '''
        return 0

    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''
        word = list("giraffa")  # in ruzzle conterrà l'attributo di istanza che contiene la lista di caratteri

carattere = {}

nCaratteri = 0
count = 0
carattereRip = {} #conterrà solo i caratteri che si ripetono


for i in word:

    if (i in carattere):  # se trova il carattere nel dictionari incrementa il suo valore
        carattere[str(i)] += 1
    else:
        carattere[str(i)] = 1 # se non lo trova lo aggiunge


for i in carattere:
    print(i)
    if carattere[i] >= 2:  # se trova il carattere nel dictionari incrementa il suo valore
        carattereRip[i] = carattere[i] # aggiunge il carattere al dictionary il carattere ripetuto



print(carattereRip)
print(carattere)
#print(nCaratteri)

    def cerca(str):
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt
        '''

str= "pop"  # nel caso di ruzzle, str deve contenere l'attributo di istanza
it = 'words.italian.txt' # è possibile aggiungere tante variabili quanti file di lingua si posseggono

f = open(it, 'r')
line = f.readline()

for line in f:  # per ogni riga del file vengono eseguite le righe di codice che seguono
#    print(str) 
    if str == line[:-1]:  #bisogna eliminare l'ultimo carattere dalla parola contenuta nella riga del file
        print("vero")
        pass

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        questo metodo può essere omessa se si utilizza un metodo built in delle
        librerie standard
        '''
strin = self_stringa

n = len(strin)

nuova_n = n-1
fatt = 0

while nuova_n>=2:
	fatt = n* nuova_n
	nuova_n = nuova_n-1

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
        #generiamo una lista a partire da una stringa
lettere = list("casa")

#generiamo tutte le possibili permutazioni e le inseriamo in una lista
permutazioni = list(permutations(lettere))

#inizializiamo una variabile stringa di appoggio e una lista dove salvarle
temp = ''
anagrammi = []

'''
 il metodo permutations genera una lista di tuple, ognu tupla è una permutazione.
 se scorriamo la lista attraverso un ciclo, possiamo scorrere gli elementi della tupla
 per ricostruire la stringa
'''
for i in permutazioni:
    for carattere in i:
        # in temp concateno tutti gli elementi della tupla così da
        # ottenere i singoli anagrammi della stringa iniziale
        temp += carattere 

    # aggiungo la parola ricostruita dalla tupla alla lista finale degli anagrammi
    anagrammi.append(temp)
    # "svuoto" la variabile temp così da ricostruire un secondo anagramma
    temp = ''

print(anagrammi)
        pass
    
    def confUtil(self):
        '''
        confUtil mette insieme diversi metodi basilari, lo scopo è:
        a partire dalla lista di tutti gli anagrammi, verifica parola per parola la sua
        presenza all'interno del file delle parole di senso compiuto, cancellando le altre.
        si consiglia l'utilizzo di anagrammi e cerca, presenti nel repo e da trasformare in metodi.
        è possibile in una seconda versione la ricefrca di parole in altre lingue. 
        '''
def confUtil(self):
	open words.italian.txt
	 if self.__stringa in words.italian.txt
	  return self.__stringa
        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        stringa = 'gloss'
        n = len(stringa)
        nuova_n = n-1
         while nuova_n=n=>2:
          permut = n*n-1
          nuova_n = nuova_n-1
        return permut 

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