import re
import nltk


def main():
    IN = re.compile(r'.*\bin\b(?!\b.+ing)')
    for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
        for rel in nltk.sem.extract_rels('NE', 'NE', doc, corpus='ieer', pattern = IN):
           print(nltk.sem.rtuple(rel))


main()