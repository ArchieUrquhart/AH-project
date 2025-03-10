from wormBody import Node


# FR 3.3
def move_player(head):
    # iterate through the list from the begining
    segment = head
    x = segment.getPos()[0]
    y = segment.getPos()[1]

    while segment.nextNode() is not None:
        # set the position of each node to that of the previous node
        segment = segment.nextNode()

        newx = segment.getPos()[0]
        newy = segment.getPos()[1]

        segment.setPos(x, y)

        x = newx
        y = newy


# detects if worm head is on square with apple FR 5.1 & 4.1
def detect_eat(head, appleX, appleY):
    # add new segment to the worm - FR 4.3
    targNode = head
    # check if head position = apple position
    if head.getPos()[0] == appleX and head.getPos()[1] == appleY:
        # find last node in list
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
        # add a new node to end of list
        targNode.append()

        return True

    return False


# checks if player has met loss criteria FR 6.1/6,2
def check_loss(head,grid):
    targNode = head.nextNode()

    #get position of head
    headX = head.getPos()[0]
    headY = head.getPos()[1]

    #check if head is out of bounds of grid - FR 6.1
    if headX< 0 or headX>= len(grid) or headY<0 or headY>=len(grid[0]):
        return True
    else:
        #Check if worm has hit the body - FR 6.2
        #loop through whole worm
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
            #check if segment intersects with head
            if targNode.getPos()[0] == headX and targNode.getPos()[1] == headY:
                return True

    return False
