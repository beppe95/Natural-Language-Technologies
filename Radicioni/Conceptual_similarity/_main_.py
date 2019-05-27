import csv
from pathlib import Path
from Radicioni.Conceptual_Similarity.utils import wordnet_max_depth
import Radicioni.Conceptual_Similarity.metrics as metrics

from nltk.corpus import wordnet


def main():
    file_folder = Path.cwd() / "files"
    sim_file = file_folder / "WordSim353.csv"

    with open(sim_file, encoding='utf-8') as sim_file:
        sim_reader = csv.reader(sim_file, delimiter=' ', quotechar='|')
        next(sim_reader)

        for row in sim_reader:
            row_data = row[0].split(',')
            cs_data = (row_data[0], row_data[1], row_data[2])

            s1 = wordnet.synsets(cs_data[0])[0]
            s2 = wordnet.synsets(cs_data[1])[0]

            # MAX_DEPTH
            print(s1._needs_root())

            # LCS
            print(s1.shortest_path_distance(s2))

            break

main()
