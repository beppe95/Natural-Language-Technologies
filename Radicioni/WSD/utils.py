from pathlib import Path
import re
from Radicioni.WSD.simplified_lesk import simplified_lesk
from Radicioni.WSD.semcor import semcor_extraction
from nltk.wsd import lesk


def lesk_wsd():
    file_folder = Path.cwd() / "files"
    wsd_file = file_folder / "sentences.txt"

    file_sentences = [line for line in open(wsd_file, encoding='utf-8').read().splitlines() if line]
    for sentence in file_sentences:
        wsd_word = (re.findall('\*\*[^>]+\*\*', sentence)[0])[2:-2]
        wsd_context = sentence.replace('*', '').strip()[2:-1]

        my_best_sense = simplified_lesk(wsd_word, wsd_context)

        print(re.sub('\*\*[^>]+\*\*', ' '.join(str(lemma) for lemma in my_best_sense.lemmas()), sentence), "\n")

        '''nltk_best_sense = lesk(wsd_context.split(), wsd_word)
        print(my_best_sense.name(), my_best_sense.definition(), my_best_sense.lemmas())
        print(nltk_best_sense.name(), nltk_best_sense.definition(), nltk_best_sense.lemmas(), "\n")'''


def semcor_wsd():
    sentences, extracted = semcor_extraction()

    for i in range(0, len(sentences)):
        sense = simplified_lesk(extracted[i][0][0], sentences[i])
        print(sense, extracted[i].label())

    # print("Sinonimi:", sense.lemmas())
    # accuracy: Sensi dei sostantivi classificati bene/ Tutti i sensi delle parola nel Semcore