def max_m(node):
	if not node.llist:
		return node.val
	else:
		g_max=float('-inf')
		for child in node.llist:
			maxi=mini_m(child)
			g_max=max(maxi,g_max)
		print(node.label+" " +str(g_max))
		return g_max
def mini_m(node):
	if not node.llist:
		return node.val
	else:
		g_mini=float('inf')
		for child in node.llist:
			mini=max_m(child)
			g_mini=min(mini,g_mini)
		print(node.label+" " +str(g_mini))
		return g_mini
class Node:
    def __init__(self, val=None, children=None, label=""):
        self.val = val  # Value at this node; meaningful for leaf nodes
        self.llist = children if children else []  # List of child nodes
        self.label=label

def main():

	leaf1 = Node(val=1,label="111")
	leaf2 = Node(val=2,label="28")
	leaf3 = Node(val=3,label="75")
	leaf4 = Node(val=4,label="62")
	leaf5 = Node(val=5,label="51")
	leaf6 = Node(val=6,label="42")
	leaf7 = Node(val=7,label="324")
	leaf8 = Node(val=8,label="26")
	leaf9 = Node(val=9,label="13")
	childL = Node(children=[leaf9],label="L")   
	childM = Node(children=[leaf1, leaf2],label="M")
	childN = Node(children=[leaf1,leaf5,leaf9],label="N")
	childO = Node(children=[leaf2],label="O")   
	childP = Node(children=[leaf8],label="P")
	childQ = Node(children=[leaf3],label="Q")   
	childR = Node(children=[leaf9],label="R")

	childE = Node(children=[childL,childM],label="E")
	childF = Node(children=[leaf7],label="F")
	childG = Node(children=[leaf5],label="G")   
	childH = Node(children=[leaf3],label="H")
	childI = Node(children=[childN,childO],label="I")
	childJ = Node(children=[leaf6],label="J")
	childK = Node(children=[childP,childQ,childR],label="K")
    
	childB = Node(children=[childE,childF],label="B")
	childC = Node(children=[childG,childH],label="C")
	childD = Node(children=[childI,childJ,childK],label="D")
    
	root = Node(children=[childB,childC,childD],label="root")


	result = max_m(root)
	print("Minimax value of the tree:", result)

if __name__ == "__main__":

	main()
