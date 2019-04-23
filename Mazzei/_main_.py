from pathlib import Path
from nltk import CFG
import numpy
from nltk import Tree, Nonterminal


def main():
    grammar_folder = Path.cwd() / "Grammar"
    grammar_file = grammar_folder / "YodaCFG.cfg"

    sentences = ["Tu avrai novecento anni di età",      #Novecento anni di età tu avrai
                 "Tu hai amici lì",                     #Amici hai tu lì
                 "Noi siamo illuminati",                #Illuminati noi siamo
                 "Tu hai molto da apprendere ancora",   #Molto da apprendere ancora tu hai
                 "Skywalker corre veloce",              #Veloce Skywalker corre
                 "Skywalker sarà tuo apprendista"]      #Tuo apprendista Skywalker sarà


    with open(grammar_file, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())

    translation_rules = [Nonterminal('ADJP'), Nonterminal('ADJ'),
                         Nonterminal('VBN'), Nonterminal('ADVP')]

    syntactic_tree = cky(sentences[0].split(), grammar)
    syntactic_tree.draw()
    yoda_translation(syntactic_tree, translation_rules)


def cky(words: list, grammar: CFG):
    table_dimension = len(words) + 1
    table = numpy.ndarray(shape=(table_dimension, table_dimension), dtype=list)

    for j in range(1, table_dimension):
        table[j - 1, j] = list()
        table[j - 1, j].append(Tree(find_head_lr(words[j - 1], grammar), [words[j - 1]]))
        for i in reversed(range(0, j - 1)):
            table[i, j] = list()
            for k in range(i + 1, j):
                if table[i, k] is not None and table[k, j] is not None:
                    table[i, j].append(Tree(find_head_gr(list(table[i, k])[0], list(table[k, j])[0], grammar),
                                            [list(table[i, k])[0], list(table[k, j])[0]]))

    return table[0, table_dimension - 1][0] if table[0, table_dimension - 1][0] != 0 \
        else Exception("Sentence not supported by written grammar!")


def find_head_lr(word: str, grammar: CFG):
    lexical_rules = list((prod for prod in grammar.productions()
                         if len(prod.rhs()) == 1 and prod.rhs()[0] == word))
    if lexical_rules:
        return lexical_rules[0].lhs()


def find_head_gr(first: Nonterminal, second: Nonterminal, grammar: CFG):
    grammar_rules = list((prod for prod in grammar.productions()
                          if len(prod.rhs()) == 2 and first.label() == prod.rhs()[0] and second.label() == prod.rhs()[1]))

    if grammar_rules:
        return grammar_rules[0].lhs()


def yoda_translation(root: Tree, translation_rules: list):
    to_be_moved = list(filter(lambda i: isinstance(root[i], Tree) and root[i].label() in translation_rules
                                     and 'put_back' not in locals(), root.treepositions()))[0] if len(root) != 0 else []

    if len(to_be_moved) != 0:
        prefix = root.__getitem__(to_be_moved)
        root.__setitem__(to_be_moved, Tree("ε", ["ε"]))
        root = Tree(Nonterminal('Yoda Translation'), [prefix, root[0], root[1]])

    root.draw()


main()


