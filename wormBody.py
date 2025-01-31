class Node:
    #constructor method for Node class
    def __init__(self,xPos,yPos):
        self.xPos_ = xPos
        self.yPos_ = yPos
        self.next_ = None

    #returns the x y position of a node
    def getPos(self):
        return [self.xPos_, self.yPos_]

    #returns the next node in the list
    def nextNode(self):
        return self.next_

    #changes the x,y position of a node to a given position
    def setPos(self,x,y):
        self.xPos_ = x
        self.yPos_ = y

    #sets the next pointer of a node to a new instance of the Node class 
    def append(self):
        #only adds node if the node is at the end
        if self.next_ is None:
            self.next_ = Node(xPos=self.xPos_, yPos=self.yPos_)




