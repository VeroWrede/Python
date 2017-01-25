# rock > scissor > paper > rock

class Node:
    def __init__(self, value, node):
        self.value = value
        self.child = node
    def dist(self, node):
        if node.value == self.value:
            return 0
        else:
            return self.child.dist(node) + 1 

rock = Node('rock', None)

paper = Node('paper', rock)

scissors = Node('scissors', paper)

rock.child = scissors

def figureWhoWins(thing1, thing2):
    return thing1 if thing2.dist(thing1) > thing1.dist(thing2) else thing2

print figureWhoWins(rock, scissors).value