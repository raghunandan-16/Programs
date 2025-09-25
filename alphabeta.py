class Node:
    def __init__(self, val=None, children=None, label=""):
        self.val = val
        self.llist = children if children else []
        self.label = label

def minimax(node, depth, is_maximizing, alpha, beta):
    if not node.llist:
        return node.val

    if is_maximizing:
        best_val = float('-inf')
        for child in node.llist:
            value = minimax(child, depth + 1, False, alpha, beta)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        print(f"{node.label} {best_val}")
        return best_val
    else:
        best_val = float('inf')
        for child in node.llist:
            value = minimax(child, depth + 1, True, alpha, beta)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        print(f"{node.label} {best_val}")
        return best_val

def create_tree():
    leaf1 = Node(val=1, label="112")
    leaf2 = Node(val=2, label="22")
    leaf3 = Node(val=3, label="34")
    leaf4 = Node(val=4, label="46")
    leaf5 = Node(val=5, label="58")
    leaf6 = Node(val=6, label="60")
    leaf7 = Node(val=7, label="711")
    leaf8 = Node(val=8, label="28")
    leaf9 = Node(val=9, label="59")

    childL = Node(children=[leaf9], label="L")   
    childM = Node(children=[leaf1, leaf2], label="M")
    childN = Node(children=[leaf1, leaf5, leaf9], label="N")
    childO = Node(children=[leaf2], label="O")   
    childP = Node(children=[leaf8], label="P")
    childQ = Node(children=[leaf3], label="Q")   
    childR = Node(children=[leaf9], label="R")

    childE = Node(children=[childL, childM], label="E")
    childF = Node(children=[leaf7], label="F")
    childG = Node(children=[leaf5], label="G")   
    childH = Node(children=[leaf3], label="H")
    childI = Node(children=[childN, childO], label="I")
    childJ = Node(children=[leaf6], label="J")
    childK = Node(children=[childP, childQ, childR], label="K")

    childB = Node(children=[childE, childF], label="B")
    childC = Node(children=[childG, childH], label="C")
    childD = Node(children=[childI, childJ, childK], label="D")

    root = Node(children=[childB, childC, childD], label="root")
    return root

def main():
    root = create_tree()
    result = minimax(root, 0, True, float('-inf'), float('inf'))
    print("Alpha-Beta Minimax Value:", result)

if __name__ == "__main__":
    main()

