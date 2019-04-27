# Natural-Language-Tecnologies
# Basic Italian-Yoda transfer translator

<p align="center">
  <img src="https://i.dlpng.com/static/png/173636_thumb.png"/>
</p>

# Project Description
The project consists in the implementation of a **basic IT → IT-YO transfer translator** which takes an italian sentence, as input, and provides its traslation into Jedi Master Yoda's speech from Star Wars.

**Parsing algorithm** we need to use and to implement is **Cocke–Kasami-Younger** (alternatively called **CKY**, or **CYK**) algorithm for context-free grammars which is based on bottom-up parsing and dynamic programming.
Even if exist other algorithm with better average running time complexity, CKY is the only one that has a worst case running time complexity of ![equation](http://latex.codecogs.com/gif.latex?O%28n%5E3%5Ccdot%20%7CG%7C%29) where ![equation](http://latex.codecogs.com/gif.latex?n) is the *length* of the parsed string and ![equation](http://latex.codecogs.com/gif.latex?%7CG%7C) is the size of the CNF grammar ![equation](http://latex.codecogs.com/gif.latex?G).


The set of **sentences**, and their **respective translations**, we have chosen is the following one:

|               Input               |          Yoda Translation         |
|:---------------------------------:|:---------------------------------:|
|   Tu avrai novecento anni di età  |   Novecento anni di età tu avrai  |
|          Tu hai amici lì          |          Amici hai tu lì          |
|        Noi siamo illuminati       |        Illuminati noi siamo       |
| Tu hai molto da apprendere ancora | Molto da apprendere ancora tu hai |
|       Skywalker corre veloce      |       Veloce Skywalker corre      |
|   Skywalker sarà tuo apprendista  |   Tuo apprendista Skywalker sarà  |

## Yoda's speech patterns
Master Jedi Yoda is one of the most iconic character of the Star Wars franchise created by George Lucas.

He's particularly known because of his bizarre linguistic schemes which have been the subject of discussion among linguists. These schemes have been associated with an **Object–Subject–Verb** (**OSV**) order.

This last scheme, generally referred as **XSV** order, is different by the **Subject–Object–Verb** (**OSV**) order we are accustomed to because it puts any complement before the subject and the verb of the sentence.

An example using an english sentence with an **OSV** order:
> You must seek advice!

An example using the same english sentence but with an **XSV** order:
> Seek advice, you must! 

## Ideas
The idea we had to write the sentences module translation was born by seeking recurrent patterns within the sentences and their respective translation.

In accordance with our thoughts, **XSV** order expose a form of empirical translation rule. 
In fact, for most of the analyzed sentences, we only need to move any complement to the beginning of the sentence to be translated to complete the translation task.

Therefore, the simplest idea to make the translation possible was to create a **set of translation rules** designed to identify the parts of speech to be moved within sentences to achieve our goal.

# Requirements
1. Writing down a generic **Context-Free Grammar**, and its respective conversion to Chomsky Normal Form, able to correctly express the chosen sentences

2. Implementation of the **Cocke–Kasami-Younger** algorithm

3. **Manipulation** of the previous phase's output in order to obtain the **input translation**


# Project management

## Grammar
Context-Free Grammar we proposed inside *YodaCFG.cfg* file covers a wide type of **syntactic units** including:
- *Noun phrase* (**NP**)
- *Verbal phrase* (**VP**)
- *Propositional phrase* (**PP**)
- *Adjective phrase* (**ADJP**)
- *Adverbial phrase* (**ADVP**)

Inside the file, we also modelled the following **Part Of Speech**:
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

## Used libraries
Along the project's development, we used **nltk** and **numpy**, two of the most used Python libraries.

**nltk** library was used to **create the Context-Free Grammar** from *YodaCFG.cfg* file and to provide the **Tree data structure** to perform CKY algorithm and to **visualize** parsing and translation outputs.

**numpy** library was used to create the essential data structure to perform CKY algorithm using the built-ins `numpy.ndarray` type.

## Modules
We choose to split the project into **four modules**:
* `main` which initializes:
  * **filesystem path** to make the *YodaCFG.cfg* file available
  * a list containing the **input sentences**, named `sentences`
  * a list of **Nonterminal objects** used to make the translation task, named `translation_rules`

* `cky` which contains the CKY algorithm implementation
* `translate`which contains the translation implementation
* `utils` which contains some utils used inside CKY algorithm implementation


### `cky` module description

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


### `translate` module description

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

### `utils` module description

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


# Results

## Exceptions

*"May the Force be with you"*.

| Authors | Giacomo Costarelli <br> (<a href="giacomo.costarelli39@gmail.com">giacomo.costarelli39@gmail.com</a>) | Giuseppe Gabbia <br> (<a href="beppegabbia@gmail.com">beppegabbia@gmail.com</a>) |
| ------------- | ------------- | ------------- |
| Github URLs | <a href="https://github.com/giacomocostarelli">https://github.com/giacomocostarelli</a>  | <a href="https://github.com/beppe95">https://github.com/beppe95</a> |



