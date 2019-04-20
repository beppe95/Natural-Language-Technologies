import Mazzei.Node as Node

def main():
    s = set()
    s.add(Node.Node("A", None, None))
    s.add(Node.Node("B", None, None))

    n1 = Node.Node("A", None, None)
    n2 = Node.Node("A", None, None)

    print(hash(n1) == hash(n2))

    mytuple = (1, 2, 3)
    print(str(mytuple)[1:-1])

main()