import Mazzei.Node as Node

def main():
    s = set()
    s.add(Node.Node("A", None, None))
    s.add(Node.Node("B", None, None))

    for elem in s:
        print(elem.data)





main()