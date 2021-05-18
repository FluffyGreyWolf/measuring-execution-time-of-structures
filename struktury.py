import random
from datetime import date, datetime
import csv
from csv import writer
import array as arr

startTimeFull = datetime.now()

# towrzymy plik csv z nazwami tabel
with open("wynikstruktury.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Algorytm', 'Ilość elementów', 'Typ elementów', 'Czas wykonania'])

# zakresy liczb
zakresy = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000]


# listy na losowo generowane liczby
random2000 = []
random4000 = []
random6000 = []
random8000 = []
random10000 = []
random12000 = []
random14000 = []
random16000 = []
random18000 = []
random20000 = []

# listy na dane posortowane rosnąco
ascending2000 = []
ascending4000 = []
ascending6000 = []
ascending8000 = []
ascending10000 = []
ascending12000 = []
ascending14000 = []
ascending16000 = []
ascending18000 = []
ascending20000 = []

# listy na dane posortowane malejąco
descending2000 = []
descending4000 = []
descending6000 = []
descending8000 = []
descending10000 = []
descending12000 = []
descending14000 = []
descending16000 = []
descending18000 = []
descending20000 = []

# listy na dane V-kształtne
v2000 = []
v4000 = []
v6000 = []
v8000 = []
v10000 = []
v12000 = []
v14000 = []
v16000 = []
v18000 = []
v20000 = []

# listy na dane A-kształtne
a2000 = []
a4000 = []
a6000 = []
a8000 = []
a10000 = []
a12000 = []
a14000 = []
a16000 = []
a18000 = []
a20000 = []

# listy na dane stałe
const2000 = []
const4000 = []
const6000 = []
const8000 = []
const10000 = []
const12000 = []
const14000 = []
const16000 = []
const18000 = []
const20000 = []

# tablice losowe
randomtab2000 = arr.array('i',[])
randomtab4000 = arr.array('i',[])
randomtab6000 = arr.array('i',[])
randomtab8000 = arr.array('i',[])
randomtab10000 = arr.array('i',[])
randomtab12000 = arr.array('i',[])
randomtab14000 = arr.array('i',[])
randomtab16000 = arr.array('i',[])
randomtab18000 = arr.array('i',[])
randomtab20000 = arr.array('i',[])

# tablice rosnące
ascendingtab2000 = arr.array('i',[])
ascendingtab4000 = arr.array('i',[])
ascendingtab6000 = arr.array('i',[])
ascendingtab8000 = arr.array('i',[])
ascendingtab10000 = arr.array('i',[])
ascendingtab12000 = arr.array('i',[])
ascendingtab14000 = arr.array('i',[])
ascendingtab16000 = arr.array('i',[])
ascendingtab18000 = arr.array('i',[])
ascendingtab20000 = arr.array('i',[])

# tablice malejące
descendingtab2000 = arr.array('i',[])
descendingtab4000 = arr.array('i',[])
descendingtab6000 = arr.array('i',[])
descendingtab8000 = arr.array('i',[])
descendingtab10000 = arr.array('i',[])
descendingtab12000 = arr.array('i',[])
descendingtab14000 = arr.array('i',[])
descendingtab16000 = arr.array('i',[])
descendingtab18000 = arr.array('i',[])
descendingtab20000 = arr.array('i',[])

# tablice V-kształtne
vtab2000 = arr.array('i',[])
vtab4000 = arr.array('i',[])
vtab6000 = arr.array('i',[])
vtab8000 = arr.array('i',[])
vtab10000 = arr.array('i',[])
vtab12000 = arr.array('i',[])
vtab14000 = arr.array('i',[])
vtab16000 = arr.array('i',[])
vtab18000 = arr.array('i',[])
vtab20000 = arr.array('i',[])

# tablice A-kształtne
atab2000 = arr.array('i',[])
atab4000 = arr.array('i',[])
atab6000 = arr.array('i',[])
atab8000 = arr.array('i',[])
atab10000 = arr.array('i',[])
atab12000 = arr.array('i',[])
atab14000 = arr.array('i',[])
atab16000 = arr.array('i',[])
atab18000 = arr.array('i',[])
atab20000 = arr.array('i',[])

# tablice stałe
consttab2000 = arr.array('i',[])
consttab4000 = arr.array('i',[])
consttab6000 = arr.array('i',[])
consttab8000 = arr.array('i',[])
consttab10000 = arr.array('i',[])
consttab12000 = arr.array('i',[])
consttab14000 = arr.array('i',[])
consttab16000 = arr.array('i',[])
consttab18000 = arr.array('i',[])
consttab20000 = arr.array('i',[])

# tablice pomocnicze
randomlisty = [random2000, random4000, random6000, random8000, random10000, random12000, random14000, random16000, random18000, random20000]
ascendinglisty = [ascending2000, ascending4000, ascending6000, ascending8000, ascending10000, ascending12000, ascending14000, ascending16000, ascending18000, ascending20000]
descendinglisty = [descending2000, descending4000, descending6000, descending8000, descending10000, descending12000, descending14000, descending16000, descending18000, descending20000]
vlisty = [v2000, v4000, v6000, v8000, v10000, v12000, v14000, v16000, v18000, v20000]
alisty = [a2000, a4000, a6000, a8000, a10000, a12000, a14000, a16000, a18000, a20000]
constlisty = [const2000, const4000, const6000, const8000, const10000, const12000, const14000, const16000, const18000, const20000]

randomtabllisty = [randomtab2000, randomtab4000, randomtab6000, randomtab8000, randomtab10000, randomtab12000, randomtab14000, randomtab16000, randomtab18000, randomtab20000]
ascendingtablisty = [ascendingtab2000, ascendingtab4000, ascendingtab6000, ascendingtab8000, ascendingtab10000, ascendingtab12000, ascendingtab14000, ascendingtab16000, ascendingtab18000, ascendingtab20000]
descendingtablisty = [descendingtab2000, descendingtab4000, descendingtab6000, descendingtab8000, descendingtab10000, descendingtab12000, descendingtab14000, descendingtab16000, descendingtab18000, descendingtab20000]
vtablisty = [vtab2000, vtab4000, vtab6000, vtab8000, vtab10000, vtab12000, vtab14000, vtab16000, vtab18000, vtab20000]
atablisty = [atab2000, atab4000, atab6000, atab8000, atab10000, atab12000, atab14000, atab16000, atab18000, atab20000]
consttablisty = [consttab2000, consttab4000, consttab6000, consttab8000, consttab10000, consttab12000, consttab14000, consttab16000, consttab18000, consttab20000]

# funkcja czyszcząca listy i generująca nowe dane
def clear():
    random2000.clear()
    random4000.clear()
    random6000.clear()
    random8000.clear()
    random10000.clear()
    random12000.clear()
    random14000.clear()
    random16000.clear()
    random18000.clear()
    random20000.clear()

    ascending2000.clear()
    ascending4000.clear()
    ascending6000.clear()
    ascending8000.clear()
    ascending10000.clear()
    ascending12000.clear()
    ascending14000.clear()
    ascending16000.clear()
    ascending18000.clear()
    ascending20000.clear()

    descending2000.clear()
    descending4000.clear()
    descending6000.clear()
    descending8000.clear()
    descending10000.clear()
    descending12000.clear()
    descending14000.clear()
    descending16000.clear()
    descending18000.clear()
    descending20000.clear()

    v2000.clear()
    v4000.clear()
    v6000.clear()
    v8000.clear()
    v10000.clear()
    v12000.clear()
    v14000.clear()
    v16000.clear()
    v18000.clear()
    v20000.clear()

    a2000.clear()
    a4000.clear()
    a6000.clear()
    a8000.clear()
    a10000.clear()
    a12000.clear()
    a14000.clear()
    a16000.clear()
    a18000.clear()
    a20000.clear()

    const2000.clear()
    const4000.clear()
    const6000.clear()
    const8000.clear()
    const10000.clear()
    const12000.clear()
    const14000.clear()
    const16000.clear()
    const18000.clear()
    const20000.clear()

    generaterandom()
    generateascending()
    generatedescending()
    generatev()
    generatea()
    generateconst()

# generowanie losowych liczb
def generaterandom():
    for a in randomlisty:
        for i in range(0, zakresy[randomlisty.index(a)]):
            x = random.randint(0, 20000)
            a.append(x)

generaterandom()


# generowanie posortowanych rosnąco liczb
def generateascending():
    for a in ascendinglisty:
        x = range(0, zakresy[ascendinglisty.index(a)])
        for i in x:
            a.append(i)

generateascending()

# generowanie posortowanych malejąco liczb
def generatedescending():
    for a in descendinglisty:
        x = range(zakresy[descendinglisty.index(a)], 0, -1)
        for i in x:
            a.append(i)

generatedescending()

# generowanie V-kształtnych liczb
def generatev():
    for a in vlisty:
        x = range(zakresy[vlisty.index(a)]//2, 0 , -1)
        y = range(1, zakresy[vlisty.index(a)]//2+1)
        for i in x:
            a.append(i)
        for i in y:
            a.append(i)

generatev()

# generowanie A-kształtnych liczb
def generatea():
    for a in alisty:
        x = range(zakresy[alisty.index(a)]//2, 0 , -1)
        y = range(1, zakresy[alisty.index(a)]//2+1)
        for i in y:
            a.append(i)
        for i in x:
            a.append(i)

generatea()

# generowanie stałych liczb ( lista o długości x składająca się x z powtórzeń jednej liczby )
def generateconst():
    for a in constlisty:
        for i in range(0, zakresy[constlisty.index(a)]):
            x = random.randint(1, 1)
            a.append(x)

generateconst()

"""
print('ARRAY')
# array dodawanie (tworzenie)
def arrayAdd(listy, tablisty, typ):
    startTime = datetime.now()
    for x in listy[tablisty.index(a)]:
        a.append(x)
    time =  datetime.now() - startTime
    print(typ, len(a), time)


# losowe
for a in randomtabllisty:
    arrayAdd(randomlisty, randomtabllisty, "Losowe")
print("")


# rosnące
for a in ascendingtablisty:
    arrayAdd(ascendinglisty, ascendingtablisty, "Rosnace")
print("")

# malejące
for a in descendingtablisty:
    arrayAdd(descendinglisty, descendingtablisty, "Malejace")
print("")

# V-kształtne
for a in vtablisty:
    arrayAdd(vlisty, vtablisty, "V-ksztaltne")
print("")
    
# A-kształtne
for a in atablisty:
    arrayAdd(alisty, atablisty, "A-ksztaltne")
print("")
    
# stałe
for a in consttablisty:
    arrayAdd(constlisty, consttablisty, "Stale")
print("")




# array contains
def contains(typ):
    startTime = datetime.now()
    randomNumber = a[random.randint(0, len(a))]
    for i in a:
        if i == randomNumber:
            time =  datetime.now() - startTime
            print(typ, len(a), time, i)
            break
        else:
            pass

# losowe
for a in randomtabllisty:
    contains("Losowe znaleziono")
print("")

# rosnące
for a in ascendingtablisty:
    contains("Rosnace znaleziono")
print("")

# malejące
for a in descendingtablisty:
    contains("Malejace znaleziono")
print("")

# V-kształtne
for a in vtablisty:
    contains("V-ksztaltne znaleziono")
print("")

# A-kształtne
for a in atablisty:
    contains("A-ksztaltne znaleziono")
print("")

# stałe
for a in consttablisty:
    contains("Stale znaleziono")
print("")



# foreach
def forEach(a, typ):
    startTime = datetime.now()
    for x in a:
        x += 1
    time =  datetime.now() - startTime
    print(typ, len(a), time)

# losowe
for a in randomtabllisty:
    forEach(a, 'Losowe')
print("")

# rosnące
for a in ascendingtablisty:
    forEach(a, 'Rosnace')
print("")

# malejące
for a in descendingtablisty:
    forEach(a, 'Malejace')
print("")

# V-kształtne
for a in vtablisty:
    forEach(a, 'V-ksztaltne')
print("")

# A-kształtne
for a in atablisty:
    forEach(a, 'A-ksztaltne')
print("")

# stałe
for a in consttablisty:
    forEach(a, 'Stale')
print("")





# array odejmowanie (usuwanie)
def removeTab(a, typ):
    dlugosc = len(a)
    startTime = datetime.now()
    while len(a) > 0:
        for x in a:
            a.remove(x)
    time =  datetime.now() - startTime
    print(typ, dlugosc, time)

# losowe
for a in randomtabllisty:
    removeTab(a, 'Losowe')
print("")

# rosnące
for a in ascendingtablisty:
    removeTab(a, 'Rosnace')
print("")

# malejące
for a in descendingtablisty:
    removeTab(a, 'Malejace')
print("")

# V-kształtne
for a in vtablisty:
    removeTab(a, 'V-ksztaltne')
print("")

# A-kształtne
for a in atablisty:
    removeTab(a, 'A-ksztaltne')
print("")

# stałe
for a in consttablisty:
    removeTab(a, 'Stale')
print("")








clear()
print('LINKED LIST')

# lista jednokierunkowa
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def forList(self):
        currentNode = self.head
        while currentNode is not None:
            currentNode.value += 1
            currentNode = currentNode.nextNode
    
    def search(self, value):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                break
            currentNode = currentNode.nextNode

    def remove(self):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value:
                currentNode.value = None
            currentNode = currentNode.nextNode




# puste losowe listy jednostronne
randomll2000 = linkedList()
randomll4000 = linkedList()
randomll6000 = linkedList()
randomll8000 = linkedList()
randomll10000 = linkedList()
randomll12000 = linkedList()
randomll14000 = linkedList()
randomll16000 = linkedList()
randomll18000 = linkedList()
randomll20000 = linkedList()

# puste rosnące listy jednostronne
ascendingll2000 = linkedList()
ascendingll4000 = linkedList()
ascendingll6000 = linkedList()
ascendingll8000 = linkedList()
ascendingll10000 = linkedList()
ascendingll12000 = linkedList()
ascendingll14000 = linkedList()
ascendingll16000 = linkedList()
ascendingll18000 = linkedList()
ascendingll20000 = linkedList()

# puste malejące listy jednostronne
descendingll2000 = linkedList()
descendingll4000 = linkedList()
descendingll6000 = linkedList()
descendingll8000 = linkedList()
descendingll10000 = linkedList()
descendingll12000 = linkedList()
descendingll14000 = linkedList()
descendingll16000 = linkedList()
descendingll18000 = linkedList()
descendingll20000 = linkedList()

# puste V-kształtne listy jednostronne
vll2000 = linkedList()
vll4000 = linkedList()
vll6000 = linkedList()
vll8000 = linkedList()
vll10000 = linkedList()
vll12000 = linkedList()
vll14000 = linkedList()
vll16000 = linkedList()
vll18000 = linkedList()
vll20000 = linkedList()

# puste A-kształtne listy jednostronne
all2000 = linkedList()
all4000 = linkedList()
all6000 = linkedList()
all8000 = linkedList()
all10000 = linkedList()
all12000 = linkedList()
all14000 = linkedList()
all16000 = linkedList()
all18000 = linkedList()
all20000 = linkedList()

# puste stałe listy jednostronne
constll2000 = linkedList()
constll4000 = linkedList()
constll6000 = linkedList()
constll8000 = linkedList()
constll10000 = linkedList()
constll12000 = linkedList()
constll14000 = linkedList()
constll16000 = linkedList()
constll18000 = linkedList()
constll20000 = linkedList()

randomlllisty = [randomll2000, randomll4000, randomll6000, randomll8000, randomll10000, randomll12000, randomll14000, randomll16000, randomll18000, randomll20000]
ascendinglllisty = [ascendingll2000, ascendingll4000, ascendingll6000, ascendingll8000, ascendingll10000, ascendingll12000, ascendingll14000, ascendingll16000, ascendingll18000, ascendingll20000]
descendinglllisty = [descendingll2000, descendingll4000, descendingll6000, descendingll8000, descendingll10000, descendingll12000, descendingll14000, descendingll16000, descendingll18000, descendingll20000]
vlllisty = [vll2000, vll4000, vll6000, vll8000, vll10000, vll12000, vll14000, vll16000, vll18000, vll20000]
alllisty = [all2000, all4000, all6000, all8000, all10000, all12000, all14000, all16000, all18000, all20000]
constlllisty = [constll2000, constll4000, constll6000, constll8000, constll10000, constll12000, constll14000, constll16000, constll18000, constll20000]



# dodawanie do listy jednostronnej (tworzenie)
def createLL(a, listy, lllisty, typ):
    startTime = datetime.now()
    for x in listy[lllisty.index(a)]:
        a.insert(x)
    time =  datetime.now() - startTime
    print(typ, len(listy[lllisty.index(a)]), time)


# losowe
for a in randomlllisty:
    createLL(a, randomlisty, randomlllisty, 'Losowe')
print("")


# rosnące
for a in ascendinglllisty:
    createLL(a, ascendinglisty, ascendinglllisty, 'Rosnace')
print("")

# malejące
for a in descendinglllisty:
    createLL(a, descendinglisty, descendinglllisty, 'Malejace')
print("")

# V-kształtne
for a in vlllisty:
    createLL(a, vlisty, vlllisty, 'V-ksztaltne')
print("")

# A-kształtne
for a in alllisty:
    createLL(a, alisty, alllisty, 'A-ksztaltne')
print("")

# stałe
for a in constlllisty:
    createLL(a, constlisty, constlllisty, 'Stale')
print("")






# sprawdzanie czy lista jendokierunkowa zawiera podaną liczbę
def containsLL(a, listy, llisty, typ):
    startTime = datetime.now()
    a.search(listy[llisty.index(a)][random.randint(0, len(listy[llisty.index(a)]))])
    time =  datetime.now() - startTime
    print(typ,  len(listy[llisty.index(a)]), time)

# losowe
for a in randomlllisty:
    containsLL(a, randomlisty, randomlllisty, 'Losowe')
print("")

# rosnące
for a in ascendinglllisty:
    containsLL(a, ascendinglisty, ascendinglllisty, 'Rosnace')
print("")

# malejące
for a in descendinglllisty:
    containsLL(a, descendinglisty, descendinglllisty, 'Malejace')
print("")

# V-kształtne
for a in vlllisty:
    containsLL(a, vlisty, vlllisty, 'V-ksztaltne')
print("")

# A-kształtne
for a in alllisty:
    containsLL(a, alisty, alllisty, 'A-ksztaltne')
print("")

# stałe
for a in constlllisty:
    containsLL(a, constlisty, constlllisty, 'Stale')
print("")





# foreach
def forEach(a, listy, llisty, typ):
    startTime = datetime.now()
    a.forList()
    time =  datetime.now() - startTime
    print(typ,  len(listy[llisty.index(a)]), time)

# losowe
for a in randomlllisty:
    forEach(a, randomlisty, randomlllisty, 'Losowe')
print("")

# rosnące
for a in ascendinglllisty:
    forEach(a, ascendinglisty, ascendinglllisty, 'Rosnace')
print("")

# malejące
for a in descendinglllisty:
    forEach(a, descendinglisty, descendinglllisty, 'Malejace')
print("")

# V-kształtne
for a in vlllisty:
    forEach(a, vlisty, vlllisty, 'V-ksztaltne')
print("")

# A-kształtne
for a in alllisty:
    forEach(a, alisty, alllisty, 'A-ksztaltne')
print("")

# stałe
for a in constlllisty:
    forEach(a, constlisty, constlllisty, 'Stale')
print("")





# lista jednokierunkowa odejmowanie (usuwanie)
def removeList(a, listy, llisty, typ):
    startTime = datetime.now()
    a.remove()
    time =  datetime.now() - startTime
    print(typ,  len(listy[llisty.index(a)]), time)

# losowe
for a in randomlllisty:
    removeList(a, randomlisty, randomlllisty, 'Losowe')
print("")

# rosnące
for a in ascendinglllisty:
    removeList(a, ascendinglisty, ascendinglllisty, 'Rosnace')
print("")

# malejące
for a in descendinglllisty:
    removeList(a, descendinglisty, descendinglllisty, 'Malejace')
print("")

# V-kształtne
for a in vlllisty:
    removeList(a, vlisty, vlllisty, 'V-ksztaltne')
print("")

# A-kształtne
for a in alllisty:
    removeList(a, alisty, alllisty, 'A-ksztaltne')
print("")

# stałe
for a in constlllisty:
    removeList(a, constlisty, constlllisty, 'Stale')
print("")
"""



clear()
print('DRZEWO BST')

# drzewo bst
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)
    
    


# puste losowe listy jednostronne
randomtree2000 = Node()
randomtree4000 = Node()
randomtree6000 = Node()
randomtree8000 = Node()
randomtree10000 = Node()
randomtree12000 = Node()
randomtree14000 = Node()
randomtree16000 = Node()
randomtree18000 = Node()
randomtree20000 = Node()

# puste rosnące listy jednostronne
ascendingtree2000 = Node()
ascendingtree4000 = Node()
ascendingtree6000 = Node()
ascendingtree8000 = Node()
ascendingtree10000 = Node()
ascendingtree12000 = Node()
ascendingtree14000 = Node()
ascendingtree16000 = Node()
ascendingtree18000 = Node()
ascendingtree20000 = Node()

# puste malejące listy jednostronne
descendingtree2000 = Node()
descendingtree4000 = Node()
descendingtree6000 = Node()
descendingtree8000 = Node()
descendingtree10000 = Node()
descendingtree12000 = Node()
descendingtree14000 = Node()
descendingtree16000 = Node()
descendingtree18000 = Node()
descendingtree20000 = Node()

# puste V-kształtne listy jednostronne
vtree2000 = Node()
vtree4000 = Node()
vtree6000 = Node()
vtree8000 = Node()
vtree10000 = Node()
vtree12000 = Node()
vtree14000 = Node()
vtree16000 = Node()
vtree18000 = Node()
vtree20000 = Node()

# puste A-kształtne listy jednostronne
atree2000 = Node()
atree4000 = Node()
atree6000 = Node()
atree8000 = Node()
atree10000 = Node()
atree12000 = Node()
atree14000 = Node()
atree16000 = Node()
atree18000 = Node()
atree20000 = Node()

# puste stałe listy jednostronne
consttree2000 = Node()
consttree4000 = Node()
consttree6000 = Node()
consttree8000 = Node()
consttree10000 = Node()
consttree12000 = Node()
consttree14000 = Node()
consttree16000 = Node()
consttree18000 = Node()
consttree20000 = Node()

randomtreelisty = [randomtree2000, randomtree4000, randomtree6000, randomtree8000, randomtree10000, randomtree12000, randomtree14000, randomtree16000, randomtree18000, randomtree20000]
ascendingtreelisty = [ascendingtree2000, ascendingtree4000, ascendingtree6000, ascendingtree8000, ascendingtree10000, ascendingtree12000, ascendingtree14000, ascendingtree16000, ascendingtree18000, ascendingtree20000]
descendingtreelisty = [descendingtree2000, descendingtree4000, descendingtree6000, descendingtree8000, descendingtree10000, descendingtree12000, descendingtree14000, descendingtree16000, descendingtree18000, descendingtree20000]
vtreelisty = [vtree2000, vtree4000, vtree6000, vtree8000, vtree10000, vtree12000, vtree14000, vtree16000, vtree18000, vtree20000]
atreelisty = [atree2000, atree4000, atree6000, atree8000, atree10000, atree12000, atree14000, atree16000, atree18000, atree20000]
consttreelisty = [consttree2000, consttree4000, consttree6000, consttree8000, consttree10000, consttree12000, consttree14000, consttree16000, consttree18000, consttree20000]


# dodawanie
def createTree(a, listy, tlisty, typ):
    startTime = datetime.now()
    for x in listy[tlisty.index(a)]:
        a.insert(x)
    time =  datetime.now() - startTime
    print(typ, len(listy[tlisty.index(a)]), time)

# losowe
for a in randomtreelisty:
    createTree(a, randomlisty, randomtreelisty, 'Losowe')
print("")

# rosnące
for a in ascendingtreelisty:
    createTree(a, ascendinglisty, ascendingtreelisty, 'Rosnace')
print("")

# malejące
for a in descendingtreelisty:
    createTree(a, descendinglisty, descendingtreelisty, 'Malejace')
print("")

# V-kształtne
for a in vtreelisty:
    createTree(a, vlisty, vtreelisty, 'V-ksztaltne')
print("")

# A-kształtne
for a in atreelisty:
    createTree(a, alisty, atreelisty, 'A-ksztaltne')
print("")

# stałe
for a in consttreelisty:
    createTree(a, constlisty, consttreelisty, 'Stale')
print("")



"""

# sprawdzanie czy zawiera daną liczbę
def containsTree(a, listy, tlisty, typ):
    startTime = datetime.now()
    a.search(listy[tlisty.index(a)][random.randint(0, len(listy[tlisty.index(a)]))])
    time =  datetime.now() - startTime
    print(typ,  len(listy[tlisty.index(a)]), time, a.search(5))

# losowe
for a in randomtreelisty:
    containsTree(a, randomlisty, randomtreelisty, 'Losowe')
print("")

# rosnące

# malejące

# V-kształtne
for a in vtreelisty:
    containsTree(a, vlisty, vtreelisty, 'V-ksztaltne')
print("")
print(v2000)
# A-kształtne

# stałe
for a in consttreelisty:
    containsTree(a, constlisty, consttreelisty, 'Stale')
print("")

print(randomtree2000.inorder([]))
print(randomtree2000.get_max())
print(randomtree2000.get_min())
"""

