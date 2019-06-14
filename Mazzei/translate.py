from nltk import Tree, Nonterminal
from Mazzei.utils import get_parent, get_right_child


def yoda_translation(root: Tree):
    """
    Provides translation from italian language to Yoda-speak language using a Transfer approach.

    :param root: the syntactic tree to be translated
    """

    current_index = list((index for index in root.treepositions()
                          if isinstance(root[index], Tree)
                          and root[index].label() in [Nonterminal("VP"), Nonterminal("AUX")]
                          and len(root[index]) == 1))[0]

    parent_index = get_parent(current_index)

    nodes_to_be_moved = []
    while root.__getitem__(parent_index).label() == Nonterminal("VP"):
        index_to_be_moved = get_right_child(parent_index)
        nodes_to_be_moved.append(root.__getitem__(index_to_be_moved))

        root.__setitem__(index_to_be_moved, Tree("ε", []))

        current_index = parent_index
        parent_index = get_parent(current_index)

    nodes_to_be_moved.reverse()
    for node in nodes_to_be_moved:
        root = Tree('Yoda Translation', [node, root])

    root.draw()
