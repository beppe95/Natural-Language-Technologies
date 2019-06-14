# Natural-Language-Technologies
# Basic Italian-Yoda transfer translator

<p align="center">
  <img src="https://i.dlpng.com/static/png/173636_thumb.png"/>
</p>


# Descrizione del progetto
Il progetto consiste nell'implementazione di un **traduttore transfer IT → IT-YO** il quale prende in input una frase scritta in linguaggio italiano e fornisce, in output, la rispettiva traduzione nella caratteristica lingua parlata da Yoda, il noto Gran Maestro del Consiglio Jedi appartenente alla saga di Star Wars.

L'**algoritmo di parsing** da utilizzare e da implementare è l'algoritmo **Cocke–Kasami-Younger** (noto anche come **CKY**, or **CYK**) per grammatiche context-free il quale risulta essere basato su di un approccio di tipo bottom-up e sulla programmazione dinamica.
Anche se esistono altri algoritmi con complessità temporali migliori, CKY è l'unico tra questi che possiede una complessità temporale, nel caso peggiore, pari a ![equation](http://latex.codecogs.com/gif.latex?O%28n%5E3%5Ccdot%20%7CG%7C%29) dove ![equation](http://latex.codecogs.com/gif.latex?n) è la *lunghezza* della stringa parsificata e ![equation](http://latex.codecogs.com/gif.latex?%7CG%7C) è la *dimensione* della grammatica context-free da noi utilizzata ![equation](http://latex.codecogs.com/gif.latex?G).

L'insieme di **frasi**, e le loro **rispettive traduzioni**, da noi scelte sono le seguenti:

|               Input               |          Traduzione Yoda          |
|:---------------------------------:|:---------------------------------:|
|   Tu avrai novecento anni di età  |   Novecento anni di età tu avrai  |
|          Tu hai amici lì          |          Amici hai tu lì          |
|        Noi siamo illuminati       |        Illuminati noi siamo       |
| Tu hai molto da apprendere ancora | Molto da apprendere ancora tu hai |
|       Skywalker corre veloce      |       Veloce Skywalker corre      |
|   Skywalker sarà tuo apprendista  |   Tuo apprendista Skywalker sarà  |

## Pattern linguistici di Yoda
Yoda, Gran Maestro del Consiglio Jedi, è uno dei personaggi più iconici della saga di Star Wars creata da George Lucas.

Tale personaggio risulta essere particolarmente conosciuto per via dei suoi schemi linguistici alquanto bizzarri i quali sono stati oggetto di discussione tra i linguisti. Tali schemi risultano essere associati ad un ordine dei costituenti che prende il nome di ordine **Oggetto–Soggetto–Verbo** (**OSV**).

Quest'ultimo schema, al quale ci riferiamo generalmente con il nome di ordine **XSV**, risulta essere differente dall'ordine **Soggetto–Oggetto–Verbo** (**SOV**) che colloca qualsiasi complemento prima del soggetto e del verbo presenti all'interno della frase da noi analizzata.

Forniamo, rispettivamente, un esempio di una frase in lingua inglese avente un ordine **SOV**:
> You must seek advice!

ed un esempio utilizzando la stessa frase in lingua inglese ma avente, questa volta, un ordine **XSV**:
> Seek advice, you must! 

## Approcci alla risoluzione del problema
L'idea di scrivere un modulo di traduzione per le frasi presentate precedentemente è nata dalla ricerca di pattern ricorrenti all'interno delle stesse frasi e delle loro rispettive traduzioni.

In accordo con quanto pensato, l'ordine **XSV** espone una sorta di regola di traduzione empirica. Difatti, per la maggior parte delle frasi da noi analizzate, dobbiamo solamente spostare ciascun complemento all'inizio della frase da dover tradurre per completare, in modo coerente, il task di traduzione.

Perciò, l'idea più semplice a cui abbiamo inizialmente pensato è stata quella di creare un **insieme di regole di traduzione** progettato affinché identificasse le parti del discorso opportune da spostare all'interno delle frasi analizzate. 

Il secondo approccio, correntemente implementato all'interno del rispettivo modulo, prevede la **ricerca** ed il conseguente **spostamento** di tutti i costituenti che si presentano dopo il verbo principale della frase analizzata.

## Algoritmo CKY
Tale algoritmo, inventato da John Cocke, Daniel Younger e Tadao Kasami, effettua un **parsing bottom-up** e sfrutta un approccio basato sulla **programmazione dinamica**.

L'**assunzione principale** che facciamo all'interno del seguente algoritmo è che la grammatica context-free da noi utilizzata sia rappresentata in **Forma Normale di Chomsky** ovvero che ogni regola, presente all'interno della grammatica, possieda nella sua *Right Hand Side* o **due simboli non terminali** oppure **un unico simbolo terminale**.
Ovviamente, tale assunzione non mina la generalità dell'algoritmo in quanto qualsiasi grammatica context-free risulta essere rappresentabile in Forma Normale di Chomsky.

Per rappresentare la struttura dei possibili alberi sintattici, i quali vengono costruiti durante l'esecuzione stessa dell'algoritmo, ci serviamo di una matrice. Nello specifico, andremo ad utilizzare la **matrice triangolare superiore** di una matrice quadrata avente dimensione ![equation](http://latex.codecogs.com/gif.latex?%5Bn&plus;1%5D*%5Bn&plus;1%5D). 

![cky](https://user-images.githubusercontent.com/37592014/59519117-768b7d80-8ec7-11e9-8fdb-f45ae3367850.PNG)

Ogni **elemento** di tale matrice in **posizione ![equation](http://latex.codecogs.com/gif.latex?%5Bi%2Cj%5D)** conterrà l'insieme di simboli non terminali che rappresentano tutti i costituenti che spaziano dalla posizione *i* alla posizione *j* all'interno della frase di input da noi analizzata.

L'**intuizione** che sta alla base del funzionamento dell'algoritmo è la seguente poiché ogni cella non terminale, ovvero ogni cella che non rappresenta una foglia del nostro albero sintattico, possiede due figli, ne segue che per ogni costituente contenuto all'interno di tale cella esiste una posizione *k* tale per cui ogni costituente può essere diviso in due parti tali che ![equation](http://latex.codecogs.com/gif.latex?i%5Cleq%20k%5Cleq%20j).
Data tale posizione *k*, la prima metà del costituente sarà memorizzata in posizione ![equation](http://latex.codecogs.com/gif.latex?%5Bi%2Ck%5D) mentre la seconda metà del costituente sarà memorizzata in posizione ![equation](http://latex.codecogs.com/gif.latex?%5Bk%2Cj%5D).

Un'**osservazione** che è molto importante fare è che tale algoritmo, così presentato, risulta essere un semplice **recognizer** e non un **algoritmo di parsing**. Questo avviene in quanto lo scopo principale di CKY è quello di verificare se, data una grammatica context-free, una data frase sia grammaticale o meno.
Per effettuare la trasformazione da recognizer a parser sono sufficienti due semplici modifiche:
 1. inserire l'utilizzo dei **backtrace** per ogni simbolo non terminale presente all'interno della matrice così che ognuno di essi risulti associato all'entry della matrice da cui è stato derivato
 2. permettere l'**inserimento dello stesso simbolo non terminale** all'interno di uno stesso elemento della matrice.

Con tali modifiche, alla terminazione dell'algoritmo, la matrice conterrà tutti i possibili alberi sintattici per la frase analizzata attraverso il task di parsing sintattico.

# Requisiti
1. Scrittura di una **Grammatica-Context-Free**, e della sua rispettiva conversione in **Forma Normale di Chomsky**, in grado di generare correttamente le frasi scelte

2. Implementazione dell'algoritmo **Cocke–Kasami-Younger**

3. **Manipolazione** dell'output della fase precedente in modo tale da ottenere le **traduzioni** desiderate.

# Project management
Il linguaggio di programmazione scelto per sviluppare il seguente progetto è *Python* nella versione 3.7.x. 
La scelta, di comune accordo, è ricaduta su tale linguaggio per via dell'estrema semplicità con cui è possibile modellare task, anche abbastanza complessi, attraverso la scrittura di codice modulare ed estremamente sintetico.
Inoltre, un'altra motivazione è rappresentata dalla grande disponibilità di librerie tra cui **Natural Language ToolKit** (noto come **NLTK**) e **numpy**, utilizzate all'interno del progetto stesso e che verranno discusse in seguito.

## Grammatica
La grammatica context-free proposta all'interno del file *YodaCFG.cfg* è in grado di trattare le seguenti **unità sintattiche** tra cui:
- *Proper nouns and Personal pronouns* (**NP**)
- *Verbal phrase* (**VP**)
- *Auxiliary verbs* (**AUX**)
- *Propositional phrase* (**PP**)
- *Adjective phrase* (**ADJP**)
- *Adverbial phrase* (**ADVP**)
- *Determiners* (**DET**)
- *Adverbs* (**ADV**)
- *Adpositions* (**ADP**)
- *Adjectives* (**ADJ**)

Di seguito riportiamo, rispettivamente le **regole grammaticali**:

```
############################
# Grammar Rules
############################

S    ->  NP VP
NP   ->  DET NP | NP PP | ADJ NP
VP   ->  AUX VBN | VP NP | VP ADJP | VP ADJ | VP ADV | VP PP
PP   ->  ADP NP | ADP VP
ADJP ->  ADJ NP | ADJ PP
ADVP ->  NOUN ADV
```

e le **regole lessicali** della grammatica da noi utilizzata:

```
#############################
# Lexical Rules
#############################

NP   -> 'Tu' | 'Noi' | 'Skywalker' | 'anni' | 'età' | 'futuro' | 'ragazzo' | 'amici'
AUX  -> 'siamo'
VBN  -> 'illuminati'
VP   -> 'hai' | 'avrai' | 'corre' | 'apprendere' | 'è'
DET  -> 'Il'
ADV  -> 'lì' | 'ancora' | 'velocemente' | 'molto'
ADP  -> 'di' | 'da'
ADJ  -> 'novecento' | 'nebuloso' | 'questo'
```

## Librerie utilizzate
Come menzionato in precedenza, durante lo sviluppo del progetto abbiamo deciso di utilizzare **nltk** e **numpy** due delle librerie Python più note ed utilizzato nei vari ambienti di sviluppo.

La libreria **nltk** è stata utlizzata per **creare la Grammatica Context-Free** dal file *YodaCFG.cfg* e per fornire la **struttura dati Tree** utilizzata all'interno dell'algoritmo CKY e per **visualizzare** l'output derivante sia dall'operazione di parsing sintattico sia dall'operazione di traduzione.

La libreria **numpy** è stata utilizzata per creare la struttura dati essenziale, rappresentata da una matrice, utilizzata all'interno dell'algoritmo CKY attraverso l'utilizzo degli array n-dimensionali definiti, all'interno della libreria stessa, come tipo built-in `numpy.ndarray`. 

## Moduli python
Abbiamo deciso di suddividere il progetto in **quattro moduli** che sono rispettivamente:

* `main` che rappresenta il modulo principale del progetto
* `cky` che contiene l'implementazione dell'algoritmo CKY
* `translate` che contiene l'implementazione del metodo utilizzato per effettuare la traduzione transfer richiesta
* `utils` che contiene metodi di supporto utilizzati all'interno dei moduli `cky` e `utils`

### Descrizione modulo `main`
Questo modulo è incaricato di inizializzare rispettivamente:
  * una variabile contenente la posizione, all'interno del filesystem, del file *YodaCFG.cfg* definita come `grammar_file`
  * una lista contenente le **frasi** da dover tradurre, definita come `sentences`

Successivamente, il modulo si occupa di leggere il file *YodaCFG.cfg* e di estrarre da esso la grammatica context-free da utilizzare per il progetto. Infine, solamente se la grammatica estratta al passo precedente risulta essere espressa in **Forma Normale di Chomsky**, procediamo a richiamare l'algoritmo di parsing CKY e, solo successivamente, effettuiamo il task di traduzione transfer richiesto; altrimenti, se la grammatica **non** risulta essere in **Forma Normale di Chomsky** allora effettuiamo una `sys.exit` fornendo il seguente messaggio di errore `Grammar is not in Chomsky Normal Form!`.

Di seguito riportiamo il codice contenuto all'interno del modulo `main`:

```python
if __name__ == '__main__':
    grammar_folder = Path.cwd() / "Grammar"
    grammar_file = grammar_folder / "YodaCFG.cfg"

    sentences = ["Tu avrai novecento anni di età",             
                 "Tu hai amici lì",                             
                 "Noi siamo illuminati",                        
                 "Tu hai molto da apprendere ancora",           
                 "Skywalker corre velocemente",                 
                 "Il futuro di questo ragazzo è nebuloso"]     

    with open(grammar_file, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())

    if grammar.is_chomsky_normal_form():
        for sent in sentences:
            syntactic_tree = cky(sent.split(), grammar)
            yoda_translation(syntactic_tree)
    else:
        exit('Grammar is not in Chomsky Normal Form!')
```

### Descrizione modulo `cky`
Modulo che implementa l'**algoritmo di parsing Cocke–Kasami-Younger**:
Gli input del metodo sono:
* una lista di parole, definita come `words`  
* una Grammatica Context-Free, definita come `grammar`  
  
L'algoritmo CKY costruisce una matrice, definita all'interno del nostro metodo come `table` tipata come `numpy.ndarray`. 
Ogni elemento di tale matrice è una lista tipata come `list`, potenzialmente vuota, di `nltk.Tree`.

L'implementazione determina se esiste o meno un albero sintattico per la frase da noi considerata andando a verificare che l'elemento della matrice in posizione ![equation](https://latex.codecogs.com/gif.latex?%5B0%2C%20n-1%5D) non sia vuoto. 

Se tale elemento non risulta essere vuoto allora la lista può contenere uno o, in caso di ambiguità grammaticale, più di un albero sintattico. In entrambi i casi, l'algoritmo restituisce il primo albero sintattico disponibile il quale, ovviamente, dovrà risultare essere corretto (cioè, dovrà contenere, all'interno della radice, il simbolo non terminale corrispondente al simbolo di start relativo alla grammatica da noi scritta).

In tutti gli altri casi effettuiamo una `sys.exit` fornendo il seguente messaggio di errore: `Sentence not supported by chosen grammar!`.

Di seguito riportiamo il codice dell'algoritmo CKY:

```python
def cky(words: list, grammar: CFG) -> Tree:
    """
    The Cocke Kasami Younger Algorithm (CKY) is an efficient parsing algorithm for Context-Free grammars.

    The structure of the rules must be in Chomsky Normal Form. CNF rules' right hand side can contain:
        1 - at most 2 symbols;
        2 - a terminal;
        3 - a null string identified by ε

    Given a sentence, the algorithm builds up, via dynamic programming, a syntactic tree consistent with the CFG input
    grammar.

    :param words: sentence split into words
    :param grammar: CFG grammar
    :return: syntactic tree, instance of nltk Tree.
    """
    table_dimension = len(words) + 1
    table = ndarray(shape=(table_dimension, table_dimension), dtype=list)

    for j in range(1, table_dimension):
        table[j - 1, j] = list()
        table[j - 1, j].append(Tree(find_lhs_lexical_rule(words[j - 1], grammar), [words[j - 1]]))

        for i in reversed(range(0, j - 1)):
            table[i, j] = list()
            for k in range(i + 1, j):
                if table[i, k] is not None and len(table[i, k]) != 0 \
                        and table[k, j] is not None and len(table[k, j]) != 0:

                    current_lhs = find_lhs_grammar_rule(table[i, k][0], table[k, j][0], grammar)
                    if current_lhs is not None:
                        table[i, j].append(Tree(current_lhs, [table[i, k][0], table[k, j][0]]))

    if len(table[0, table_dimension - 1]) != 0 and table[0, table_dimension - 1][0].label() == Nonterminal("S"):
        table[0, table_dimension - 1][0].draw()
        return table[0, table_dimension - 1][0]
    else:
        exit('Sentence not supported by chosen grammar!')
```

### Descrizione modulo `translate`
Modulo che implementa la regola di traduzione menzionata precedentemente.
L'input del metodo è:
* un albero sintattico, risultato dell'applicazione dell'algoritmo di parsing CKY, istanza di `nltk.Tree`, definito come `root`

Il metodo, a partire da una lista contenente un insieme di tuple le quali, a loro volta, contengono gli indici rappresentanti la posizione dei nodi all'interno dell'albero sintattico, recuperata attraverso l'istruzione `root.treepositions()`, filtra tutti gli indici appartenenti ai nodi tali per cui questi ultimi:
* sono istanze di `ntlk.Tree`
* sono etichettati con un simbolo non terminale a scelta tra *VP* e *AUX*
* possiedono un unico figlio.

Il risultato filtrato viene memorizzato all'interno di `current_index` che rappresenta l'indice del nodo contenente il riferimento diretto al simbolo terminale corrispondente al sintagma verbale principale della frase analizzata.

Successivamente, dopo aver memorizzato all'interno di `parent_index` l'indice del nodo padre di `current_index`, procediamo alla **ricerca** ed alla **sostituzione** con il simbolo terminale **ε**, in modo iterativo, di tutti i costituenti che si presentano alla destra del verbo principale della frase analizzata i quali vengono memorizzati in una lista definita come `nodes_to_be_moved`.

Infine, per ciascuno degli elementi all'interno della lista `nodes_to_be_moved` procediamo alla costruzione di un nuovo albero, istanza di `ntlk.Tree`, avente come label la stringa *Yoda Translation*, come figlio sinistra l'elemento corrente della lista `nodes_to_be_moved` e come figlio destro il sottoalbero dell'iterazione precedente.

Con ciò, effettuiamo la ricostruzione dell'albero sintattico, coerentemente con la traduzione transfer richiesta.

Di seguito riportiamo il codice che attua la traduzione di un dato albero sintattico:

```python
def yoda_translation(root: Tree):
    """
    Provides translation from italian language to Yoda-speak language.

    It filters out from nltk tree's indices of the subtree whose label is contained in 'translation_rules'.
    Then, it sets the previously obtained subtree as the new left child of a new syntactic tree.

    :param root: the syntactic tree to be translated
    """

    current_index = list((index for index in root.treepositions()
                          if isinstance(root[index], Tree)
                          and root[index].label() in [Nonterminal("VP"), Nonterminal("AUX")]
                          and len(root[index]) == 1))[0]

    parent_index = get_parent(current_index)

    nodes_to_be_moved = []
    while root.__getitem__(parent_index).label() == Nonterminal("VP"):
        index_to_be_moved = get_right_child(parent_index)
        nodes_to_be_moved.append(root.__getitem__(index_to_be_moved))

        root.__setitem__(index_to_be_moved, Tree("ε", []))

        current_index = parent_index
        parent_index = get_parent(current_index)

    nodes_to_be_moved.reverse()
    for node in nodes_to_be_moved:
        root = Tree('Yoda Translation', [node, root])

    root.draw()
```

### Descrizione modulo `utils`
Modulo che implementa alcuni metodi di supporto utilizzati all'interno del modulo `cky`.

Il primo metodo è utilizzato per ricercare l'*LHS di una regola lessicale* dati un simbolo terminale, corrispondente all'*RHS di una regola lessicale* ed una grammatica.
I suoi input sono:
* una stringa, rappresentante l'*RHS* di una regola lessicale, definita come `word`
* una Grammatica Context-Free, definita come `grammar` 

Il metodo, a partire da una lista contenente l'insieme delle regole di produzione, contenute nella grammatica context-free utilizzata, recuperato attraverso l'istruzione `grammar.productions()`, filtra tutte le regole di produzione che possiedono una *RHS* avente un unico simbolo e tali per cui quest'ultimo risulta corrispondere al parametro di input `word`.

Fatto ciò, se la lista `lexical_rules` non è vuota allora restituiamo il primo elemento di tale lista che, come già menzionato, corrisponde all'*LHS*, se esiste, della regola lessicale ricercata altrimenti il metodo ritorna `None`.

Riportiamo di seguito il codice del suddetto metodo:

```python
def find_lhs_lexical_rule(word: str, grammar: CFG) -> Nonterminal:
    """
    Finds the LHS of a lexical rule contained in the input CFG grammar.

    :param word: the RHS of a lexical rule
    :param grammar: input CFG grammar
    :return: the LHS of a lexical rule, if it exists
    """
    lexical_rules = list((prod for prod in grammar.productions()
                         if len(prod.rhs()) == 1 and prod.rhs()[0] == word))
    if lexical_rules:
        return lexical_rules[0].lhs()
```

Il secondo metodo è utilizzato, invece, per ricercare l'*LHS di una regola grammatcale* dati due simboli non terminali, corrispondenti alla *prima e all'ultima metà dell'RHS di una regola grammaticale*, ed una grammatica.

I suoi input sono:
* un primo sottoalbero, istanza di `nltk.Tree`, la cui etichetta della radice rappresenta la prima metà dell'*RHS* di una regola grammaticale, definito come `first`
* un secondo sottoalbero, istanza di `nltk.Tree`, la cui etichetta della radice rappresenta la seconda metà dell'*RHS* di una regola grammaticale, definito come `second`
* una Grammatica Context-Free, definita come `grammar` 

Il metodo, a partire da una lista contenente l'insieme delle regole di produzione, contenute nella grammatica context-free utilizzata, recuperato attraverso l'istruzione `grammar.productions()`, filtra tutte le regole di produzione che possiedono una *RHS* avente esattamente due simboli e tali il primo simbolo corrisponde all'etichetta del sottoalbero `first` ed il secondo simbolo corrisponde all'etichetta del sottoalbero `second` passati come parametri di input.

Fatto ciò, se la lista `grammar_rules` non è vuota allora restituiamo il primo elemento di tale lista che, come già menzionato, corrisponde all'*LHS*, se esiste, della regola grammaticale ricercata altrimenti il metodo ritorna `None`.

Riportiamo di seguito il codice del suddetto metodo:

```python
def find_lhs_grammar_rule(first: Tree, second: Tree, grammar: CFG) -> Nonterminal:
    """
    Finds the LHS of a grammar rule contained in the input CFG grammar.

    :param first: first half of the grammar rule's RHS
    :param second: latter half of the grammar rule's RHS
    :param grammar: input CFG grammar
    :return: the LHS of a grammar rule, if it exists
    """
    grammar_rules = list((prod for prod in grammar.productions()
                          if len(prod.rhs()) == 2
                          and first.label() == prod.rhs()[0] and second.label() == prod.rhs()[1]))

    if grammar_rules:
        return grammar_rules[0].lhs()
```

Il terzo ed il quarto metodo contenuti all'interno di questo modulo vengono, invece, utilizzati nel modulo `translate`.

Il terzo metodo, definito come `get_parent`, prende in input una tupla contenente l'indice del nodo corrente che stiamo esaminando e restituisce in output, sempre all'interno di una tupla, l'indice corrispondente al padre del nodo corrente esaminato.

Il quarto metodo, invece, definito come `get_right_child`, prende in input una tupla contenente l'indice del nodo corrente che stiamo esaminando e restituisce in output, sempre all'interno di una tupla, l'indice corrispondente al figlio destro del nodo corrente esaminato.

Riportiamo di seguito i codici di questi ultimi metodi descritti:

```python
def get_parent(index: tuple) -> tuple:
    """
    Finds node's parent index.

    :param index: tuple which contains the node's index
    :return: index of the parent node
    """
    return index[:-1]
```

```python
def get_right_child(index: tuple) -> tuple:
    """
    Finds node's right child index.

    :param index: tuple which contains the node's index
    :return: index of the right child node
    """
    return index + (1, )
```

# Risultati ottenuti
Di seguito presentiamo sia i risultati ottenuti mediante l'applicazione dell'algoritmo CKY all'insieme di frasi da noi scelto sia i risultati ottenuti tramite l'applicazione del modulo di traduzione transfer richiesto:

![1](https://user-images.githubusercontent.com/37592014/59520022-64aada00-8ec9-11e9-98d8-c3dcbae86726.PNG)

![2](https://user-images.githubusercontent.com/37592014/59520037-6aa0bb00-8ec9-11e9-96c4-0769fc8aff68.PNG)

![3](https://user-images.githubusercontent.com/37592014/59520055-6ffe0580-8ec9-11e9-80d5-f386a627f152.PNG)

![4](https://user-images.githubusercontent.com/37592014/59520066-75f3e680-8ec9-11e9-8fd1-d3b03cde0f48.PNG)

![5](https://user-images.githubusercontent.com/37592014/59520077-7e4c2180-8ec9-11e9-9cdf-d23e65490266.PNG)

![6](https://user-images.githubusercontent.com/37592014/59520085-83a96c00-8ec9-11e9-9edb-3e380644439c.PNG)

## Eccezioni
L'unica eccezione da segnalare riguarda la modifica di una frase da noi scelta.
Nello specifico, la frase originaria in questione era "Skywalker corre veloce".

Come si può notare, la frase non risulta essere corretta poiché l'aggettivo *veloce* dovrebbe essere sostituito con l'avverbio *velocemente*. La frase originaria perciò è stata modificata in "Skywalker corre velocemente".

*"May the Force be with you"*.

| Authors | Giacomo Costarelli <br> (<a href="giacomo.costarelli39@gmail.com">giacomo.costarelli39@gmail.com</a>) | Giuseppe Gabbia <br> (<a href="beppegabbia@gmail.com">beppegabbia@gmail.com</a>) |
| ------------- | ------------- | ------------- |
| Github URLs | <a href="https://github.com/giacomocostarelli">https://github.com/giacomocostarelli</a>  | <a href="https://github.com/beppe95">https://github.com/beppe95</a> |
