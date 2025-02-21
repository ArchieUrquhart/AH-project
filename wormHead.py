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



# detects if worm head is on square with apple
def detect_eat(head,appleX,appleY):
    targNode = head
    #check if head position = apple position
    if head.getPos()[0] == appleX and head.getPos()[1] == appleY:
        #find last node in list
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
        #add a new node to end of list
        targNode.append()

        return True

    return False


# checks if player has met loss criteria
def check_loss(head):
    targNode = head.nextNode()

    #get position of head
    headX = head.getPos()[0]
    headY = head.getPos()[1]

    #check if head is out of bounds of grid
    if headX< 0 or headX>= gridWidth or headY<0 or headY>=gridHeight:
        return True
    else:
        #loop through whole worm
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
            #check if segment intersects with head
            if targNode.getPos()[0] == headX and targNode.getPos()[1] == headY:
                return True

    return False
