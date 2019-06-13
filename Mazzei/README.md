# Natural-Language-Technologies
# Basic Italian-Yoda transfer translator

<p align="center">
  <img src="https://i.dlpng.com/static/png/173636_thumb.png"/>
</p>

# Descrizione del progetto
Il progetto consiste nell'implementazione di un **traduttore di tipo transfer IT → IT-YO** il quale prende in input una frase scritta in linguaggio italiano e fornisce, in output, la rispettiva traduzione nella caratteristica lingua parlata da Yoda, il noto Gran Maestro del Consiglio Jedi appartenente alla saga di Star Wars.

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

**Metti tutte le fasi delle roba fatta!**

## Algoritmo CKY

# Requisiti
1. Scrittura di una **Grammatica-Context-Free**, e della sua rispettiva conversione in **Forma Normale di Chomsky**, in grado di generare correttamente le frasi scelte

2. Implementazione dell'algoritmo **Cocke–Kasami-Younger**

3. **Manipolazione** dell'output della fase precedente in modo tale da ottenere le **traduzioni** desiderate.

# Project management
Il linguaggio di programmazione scelto per sviluppare il seguente progetto è *Python* nella versione 3.7.x. 
La scelta, di comune accordo, è ricaduta su tale linguaggio per via dell'estrema semplicità con cui è possibile modellare task, anche abbastanza complessi, attraverso la scrittura di codice modulare ed estremamente sintetico.
Inoltre, un'altra motivazione è rappresentata dalla grande disponibilità di librerie tra cui **Natural Language ToolKit** (noto come **NLTK**) e **numpy**, utilizzate all'interno del progetto stesso e che verranno discusse in seguito.

## Grammatica
La grammatica context-free proposta all'interno del file *YodaCFG.cfg* è in grado di trattare numerose **unità sintattiche** tra cui:
- *Noun phrase* (**NP**)
- *Verbal phrase* (**VP**)
- *Propositional phrase* (**PP**)
- *Adjective phrase* (**ADJP**)
- *Adverbial phrase* (**ADVP**)

All'interno del file, sono anche modellate le seguenti **Part Of Speech**:
- *Common nouns* (**NOUN**)
- *Proper nouns and Personal pronouns* (**NP**)
- *Auxiliary verbs* (**AUX**)
- ** (**VBN**)
- ** (**VERB**)
- *Determiners* (**DET**)
- *Adverbs* (**ADV**)
- *Pronouns, excluding personal pronouns* (**PRON**)
- *Adpositions* (**ADP**)
- *Adjectives* (**ADJ**)

Di seguito riportiamo, rispettivamente le **regole grammaticali**:

<pre lang=text>
############################
# Grammar Rules
############################

S    ->  NP VP
NP   ->  DET NP | NP PP | ADJ NP
VP   ->  AUX VBN | VP NP | VP ADJP | VP ADJ | VP ADV | VP PP
PP   ->  ADP NP | ADP VP
ADJP ->  ADJ NP | ADJ PP
ADVP ->  NOUN ADV
</pre>

e le **regole lessicali** della grammatica da noi utilizzata:

<pre lang=text>
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
</pre>

## Librerie utilizzate
Come menzionato in precedenza, durante lo sviluppo del progetto abbiamo deciso di utilizzare **nltk** e **numpy** due delle librerie Python più note ed utilizzato nei vari ambienti di sviluppo.

La libreria **nltk** è stata utlizzata per **creare la Grammatica Context-Free** dal file *YodaCFG.cfg* e per fornire la **struttura dati Tree** utilizzata all'interno dell'algoritmo CKY e per **visualizzare** l'output derivante sia dall'operazione di parsing sintattico sia dall'operazione di traduzione.

La libreria **numpy** è stata utilizzata per creare la struttura dati essenziale, rappresentata da una matrice quadrata, utilizzata all'interno dell'algoritmo CKY attraverso l'utilizzo degli array n-dimensionali presenti definiti, all'interno della libreria stessa, come tipo built-in `numpy.ndarray`. **GUARDA QUI**


## Moduli python
Abbiamo deciso di suddividere il progetto in **?? moduli**:

* `main` che inizializza:
  * **filesystem path** to make the *YodaCFG.cfg* file available
  * a list containing the **input sentences** to be translated , named `sentences`

* `cky` che contiene l'implementazione dell'algoritmo CKY
* `translate` che contiene l'implementazione del metodo utilizzare per effettuare la traduzione transfer richiesta
* `utils` che contiene metodi di supporto utilizzati all'interno dell'algoritmo CKY


### Descrizione modulo `cky`
Modulo che implementa l'**algoritmo di parsing Cocke–Kasami-Younger**:
Gli input del metodo sono:
* una lista di parole, definita come `words`  
* una Grammatica Context-Free, definita come `grammar`  
  
L'algoritmo CKY costruisce una matrice, definita come `table` tipata come `numpy.ndarray`. 
Ogni elemento di tale matrice è una lista tipata come `list`, potenzialmente vuota, di `nltk.Tree`.

L'implementazione determina se esiste o meno un albero sintattico per la frase da noi considerata andando a verificare che l'elemento della matrice in posizione ![equation](https://latex.codecogs.com/gif.latex?%5B0%2C%20n-1%5D) non sia vuoto. 

Se tale elemento non risulta essere vuoto allora la lista può contenere uno o, in caso di ambiguità grammaticale, più di un albero sintattico. In entrambi i casi, l'algoritmo restituisce il primo albero sintattico disponibile.

In tutti gli altri casi viene generata un'eccezione.

Di seguito riportiamo il codice dell'algoritmo CKY:

<pre lang=python>
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
    table = numpy.ndarray(shape=(table_dimension, table_dimension), dtype=list)

    for j in range(1, table_dimension):
        table[j - 1, j] = list()
        table[j - 1, j].append(Tree(utils.find_lhs_lexical_rule(words[j - 1], grammar), [words[j - 1]]))
        for i in reversed(range(0, j - 1)):
            table[i, j] = list()
            for k in range(i + 1, j):
                if table[i, k] is not None and table[k, j] is not None:
                    table[i, j].append(Tree(utils.find_lhs_grammar_rule(list(table[i, k])[0],
                                                                        list(table[k, j])[0], grammar),
                                            [list(table[i, k])[0], list(table[k, j])[0]]))

    return table[0, table_dimension - 1][0] if table[0, table_dimension - 1][0] \
        else Exception("Sentence not supported by written grammar!")
</pre>


### Descrizione modulo `translate`
Modulo che implementa la regola di traduzione menzionata precedentemente.
Gli input del metodo sono:
* un albero, instanza di `nltk.Tree`, definito come `root`  

**SCRIVERE COSA FA IL METODO**

Di seguito riportiamo il codice che attua la traduzione di un dato albero sintattico:

<pre lang=python>
def yoda_translation(root: Tree, translation_rules: list):
    """
    Provides translation from italian language to Yoda-speak language.
    It filters out from nltk tree's indices of the subtree whose label is contained in 'translation_rules'.
    Then, it sets the previously obtained subtree as the new left child of a new syntactic tree.
    :param root: the syntactic tree to be translated
    :param translation_rules: list of Nonterminal object used to provide translation from italian to Yoda-speak language
    """

    to_be_moved = list((index for index in root.treepositions()
                        if isinstance(root[index], Tree) and root[index].label() in translation_rules))[0]

    if to_be_moved:
        prefix = root.__getitem__(to_be_moved)
        root.__setitem__(to_be_moved, Tree("ε", []))
        root = Tree('Yoda Translation', [prefix, root])

    root.draw()
 </pre>

### Descrizione modulo `utils`
Modulo che implementa alcuni metodi di supporto utilizzati all'interno del modulo `cky`.

Il primo metodo è utilizzato per ricercare l'*LHS di una regola lessicale* dati un simbolo terminale, corrispondente all'*RHS di una regola lessicale* ed una grammatica.
I suoi input sono:
* 
*   

Il suo output è:

<pre lang=python>
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
</pre>

Il primo metodo è utilizzato per ricercare l'*LHS di una regola grammatcale* dati due simboli non terminali, corrispondenti alla *prima e all'ultima metà dell'RHS di una regola grammaticale*, ed una grammatica.

I suoi input sono;
* 
* 

Il suo output è:

<pre lang=python>
def find_lhs_grammar_rule(first: Nonterminal, second: Nonterminal, grammar: CFG) -> Nonterminal:
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
</pre>


# Risultati ottenuti

## Eccezioni

*"May the Force be with you"*.

| Authors | Giacomo Costarelli <br> (<a href="giacomo.costarelli39@gmail.com">giacomo.costarelli39@gmail.com</a>) | Giuseppe Gabbia <br> (<a href="beppegabbia@gmail.com">beppegabbia@gmail.com</a>) |
| ------------- | ------------- | ------------- |
| Github URLs | <a href="https://github.com/giacomocostarelli">https://github.com/giacomocostarelli</a>  | <a href="https://github.com/beppe95">https://github.com/beppe95</a> |



