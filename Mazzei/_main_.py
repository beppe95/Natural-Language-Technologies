from pathlib import Path
from nltk import CFG, Nonterminal
import Mazzei.cky as cky_algorithm
import Mazzei.translate as translate


def main():
    grammar_folder = Path.cwd() / "Grammar"
    grammar_file = grammar_folder / "YodaCFG.cfg"

    sentences = ["Tu avrai novecento anni di età",      #Novecento anni di età tu avrai
                 "Tu hai amici lì",                     #Amici hai tu lì
                 "Noi siamo illuminati",                #Illuminati noi siamo
                 "Tu hai molto da apprendere ancora",   #Molto da apprendere ancora tu hai
                 "Skywalker corre veloce",              #Veloce Skywalker corre
                 "Skywalker sarà tuo apprendista"]      #Tuo apprendista Skywalker sarà

    translation_rules = [Nonterminal('ADJP'), Nonterminal('ADJ'),
                         Nonterminal('VBN'), Nonterminal('ADVP')]

    with open(grammar_file, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())
    file.close()

    for sent in sentences:
        syntactic_tree = cky_algorithm.cky(sent.split(), grammar)
        syntactic_tree.draw()
        translate.yoda_translation(syntactic_tree, translation_rules)


main()


