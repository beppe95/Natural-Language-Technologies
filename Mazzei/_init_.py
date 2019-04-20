from pathlib import Path
import nltk

grammar_folder = Path.cwd() / 'Grammar'
grammar_file = grammar_folder / "YodaCFG.cfg"

sentences = ["Noi siamo illuminati",
             "Tu hai amici lì",
             "Tu avrai novecento anni di età",
             "Skywalker corre veloce",
             "Il futuro di questo ragazzo è nebuloso",
             "Tu hai molto da apprendere ancora",
             "Frase volutamente non supportata dalla grammatica"]

'''translation_rules = [grammar.Nonterminal('ADJP'), grammar.Nonterminal('ADJ'),
                     grammar.Nonterminal('VBN'),  grammar.Nonterminal('ADVP')]'''

test_grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> DET NOUN | NOUN PP | NP PP | PRON NOUN
VP -> AUX VBN | VERB NP | VERB ADJP | VERB ADJ | VERB ADVP | VERB ADV
PP -> ADP NOUN | ADP NP | ADP VP
ADJP -> ADJ NP | ADJ PP
ADVP -> NOUN ADV
NP -> 'Tu' | 'Noi' | 'Skywalker'
AUX -> 'siamo'
VBN -> 'illuminati'
VERB -> 'hai' | 'avrai' | 'corre' | 'apprendere' | 'è'
DET -> 'Il'
ADV -> 'lì' | 'ancora'
PRON -> 'questo'
NOUN -> 'amici' | 'età' | 'anni' | 'futuro' | 'ragazzo'
ADP  -> 'di' | 'da'
ADJ  -> 'novecento' | 'veloce' | 'nebuloso' | 'molto'
""")

sent = sentences[2].split()
parser = nltk.ChartParser(test_grammar)

for tree in parser.parse(sent):
    print(tree)

