from sys import exit
from pathlib import Path
from nltk import CFG
from Mazzei.cky import cky
from Mazzei.translate import yoda_translation


def main():
    grammar_folder = Path.cwd() / "Grammar"
    grammar_file = grammar_folder / "YodaCFG.cfg"

    sentences = ["Tu avrai novecento anni di età",              #Novecento anni di età tu avrai
                 "Tu hai amici lì",                             #Amici tu hai lì
                 "Noi siamo illuminati",                        #Illuminati noi siamo
                 "Tu hai molto da apprendere ancora",           #Molto da apprendere ancora tu hai
                 "Skywalker corre velocemente",                 #Veloce(mente) Skywalker corre
                 "Il futuro di questo ragazzo è nebuloso"]      #Nebuloso il futuro di questo ragazzo è

    with open(grammar_file, encoding='utf-8') as file:
        grammar = CFG.fromstring(file.read())
    file.close()

    if grammar.is_chomsky_normal_form():
        for sent in sentences:
            syntactic_tree = cky(sent.split(), grammar)
            yoda_translation(syntactic_tree)
    else:
        exit('Grammar is not in Chomsky Normal Form!')


main()

