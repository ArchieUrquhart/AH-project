from wormBody import Node

def move_player(head):
    segment = head

    while segment.nextNode() is not None:
        x = segment.getPos()[0]
        y = segment.getPos()[1]

        segment = segment.nextNode()
        segment.setPos(x,y)

head = Node(0,0)
node = head
for i in range(10):
    node.append()
    node = node.nextNode()

node = head
for i in range(10):
    node.append()
    node = node.nextNode()