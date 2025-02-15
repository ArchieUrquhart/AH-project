from wormBody import Node

def move_player(head):
    #iterate through the list from the begining
    segment = head
    x = segment.getPos()[0]
    y = segment.getPos()[1]

    while segment.nextNode() is not None:
        # set the position of each node to that of the previous node    
        segment = segment.nextNode()
        
        newx = segment.getPos()[0]
        newy = segment.getPos()[1]

        segment.setPos(x,y)

        x = newx
        y = newy

