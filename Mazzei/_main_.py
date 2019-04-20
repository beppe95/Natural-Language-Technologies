from pathlib import Path
from nltk import CFG
import numpy

import Mazzei.Node as Node


def main():
    grammar_folder = Path.cwd() / "Grammar"
    grammar_file = grammar_folder / "YodaCFG.cfg"

    sentences = ["Noi siamo illuminati",
                 "Tu hai amici lì",
                 "Tu avrai novecento anni di età",
                 "Skywalker corre veloce",
                 "Il futuro di questo ragazzo è nebuloso",
                 "Tu hai molto da apprendere ancora",
                 "Frase volutamente non supportata dalla grammatica"]

    with open(grammar_file, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())

    cky(sentences[0].split(), grammar)


def cky(words: list, grammar: CFG):
    table_dimension = len(words) + 1
    table = numpy.ndarray(shape=(table_dimension, table_dimension), dtype=set)

    for j in range(1, table_dimension):
        table[j-1, j] = set()
        table[j-1, j].add(Node.Node(find_head_lr(words[j-1], grammar), None, None))
        print("Lexical rule: " + str(list(table[j-1, j])[0].data))

        for i in reversed(range(0, j - 1)):
            for k in range(i + 1, j):
                if table[i, k] is not None and table[k, j] is not None:
                    grammar_heads = find_head_gr(table[i, k], table[k, j], grammar)

                    print(list(table[i, k])[0].data, list(table[k, j])[0].data)

                '''if table[i, k] is not None and table[k, j] is not None:
                    grammar_heads = find_head_gr(table[i, k], table[k, j], grammar)
                    if not grammar_heads:
                        print("List is empty")'''


def find_head_lr(word: str, grammar: CFG):
    lexical_rules = list((prod for prod in grammar.productions()
                         if len(prod.rhs()) == 1 and prod.rhs()[0] == word))

    return lexical_rules[0].lhs()


def find_head_gr(first: set, second: set, grammar: CFG):
    grammar_rules = []
    for f in first:
        for s in second:
            grammar_rules.append(prod for prod in grammar.productions()
                                 if len(prod.rhs()) == 2
                                 and str(prod.rhs()[0]) == f.data and str(prod.rhs()[1]) == s.data)

    res = []
    for g in grammar_rules:
        for e in g:
            res.append((e.lhs(), e.rhs()[0], e.rhs()[1]))

    for elem in res:
        print(elem)

    return res


main()


