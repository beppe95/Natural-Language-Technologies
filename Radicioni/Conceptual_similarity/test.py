from Radicioni.Conceptual_similarity.utils import read_csv_file
from pathlib import Path


def main():
    file_folder = Path.cwd() / "File"
    path_csvfile = file_folder / "WordSim353.csv"

    read = read_csv_file(path_csvfile)


main()