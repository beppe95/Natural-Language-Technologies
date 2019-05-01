from nltk import Tree, Nonterminal
from Mazzei.utils import get_node_to_be_moved


def yoda_translation(root: Tree):
    """
    Provides translation from italian language to Yoda-speak language.

    It filters out from nltk tree's indices of the subtree whose label is contained in 'translation_rules'.
    Then, it sets the previously obtained subtree as the new left child of a new syntactic tree.

    :param root: the syntactic tree to be translated
    """

    sentence_vp_index = list((index for index in root.treepositions()
                              if isinstance(root[index], Tree)
                              and (root[index].label() == Nonterminal("VP") or root[index].label() == Nonterminal("AUX"))
                              and len(root[index]) == 1))

    if sentence_vp_index:
        to_be_moved = get_node_to_be_moved(sentence_vp_index[0])
        prefix = root.__getitem__(to_be_moved)
        root.__setitem__(to_be_moved, Tree("ε", []))
        root = Tree('Yoda Translation', [prefix, root])

    root.draw()
