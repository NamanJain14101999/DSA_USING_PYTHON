class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    # insert in sll 
    def inseetSLL(self,value,location):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index <location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode
    # traverse in sll
    def traverseSLL(self):
        if self.head is None:
            print("the SLL doesnot exits")
        else:
            tempnode=self.head
            while tempnode!=None:
                print(tempnode.value)
                tempnode=tempnode.next
    # search in sll
    def searchSLL(self,value):
        if self.head is None:
            print("sll is empty")
        else:
            tempnode=self.head
            while tempnode is not None:
                if tempnode.value==value:
                    return tempnode.value
                tempnode=tempnode.next
            return "the value does not exits"


        

singlyll=SLinkedList()
singlyll.inseetSLL(1,1)
singlyll.inseetSLL(2,1)
singlyll.inseetSLL(3,1)
singlyll.inseetSLL(4,1)
singlyll.inseetSLL(0,0)
#node1=Node(1)
#node2=Node(2)
#singlyll.head=node1
#singlyll.head.next=node2
#singlyll.tail=node2
#print([node.value for node in singlyll])
singlyll.traverseSLL()
print(singlyll.searchSLL(12))