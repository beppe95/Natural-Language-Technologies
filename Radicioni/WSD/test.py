from builtins import print

from Radicioni.WSD.utils import remove_asterisks

import re


def main():
    string = "**Arms** bend at the elbow."
    new_string = re.sub('\*\*[^>]+\*\*', "diocane", string)
    print(new_string)
main()