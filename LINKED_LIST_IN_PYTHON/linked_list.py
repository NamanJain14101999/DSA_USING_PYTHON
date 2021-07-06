class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("ll is empty")
            return 
        itr=self.head   
        lstr=''
        while itr:
            lstr+=str(itr.data)+"==>"
            itr=itr.next
        print(lstr)    
    def insert_at_begining(self,data):
        #newnode=Node(data)
        #if self.head==None:
        #    self.head=newmode
        #else:
        #    newnode.next=self.head
        #    self.head=newnode
        newnode=Node(data,self.head)
        self.head=newnode

    def get_len(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c

    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new

    def insert_value(self,list):
        self.head=None
        for data in list:
            self.insert_at_end(data)

    def remove_first(self):
        if self.head is None:
            print("empty ll")
            return None
        self.head=self.head.next

    def remove_last(self):
        if self.head==None:
            print("empty ll")
            return
        else:
            temp=self.head
            pre=self.head
            while temp.next!=None:
                pre=temp
                temp=temp.next
            pre.next=None

    def remove_at(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return 
        temp=self.head
        pre=self.head
        i=0
        while i != index:
            pre=temp
            temp=temp.next
            i+=1
        pre.next=temp.next
        temp.next=None

    def search_in_ll(self,value):
        i=0
        temp=self.head
        while temp is not None:
            if temp.data==value:
                return i
            i+=1
            temp=temp.next
        return "not founded in ll"





if __name__ =='__main__':
    #ll=LinkedList()
    #ll.head=Node(10)
    #second=Node(20)
    #third=Node(30)

    #ll.head.next=second
    #second.next=third
    #ll.insert_at_begining(100)

    #ll.print()
    #print(ll.get_len())

    #nsert_value([1,2,3,4])
    #ll.print()

    ll=LinkedList()
    ll.insert_at_begining("RED")
    ll.insert_at_begining("BLACK")
    ll.insert_at_begining("YELLOW")
    ll.insert_at_begining("ORANGE")

    #ll.print()
    #ll.remove_first()
    #ll.print()
    #ll.remove_last()
    #ll.print()
    #ll.remove_at(2)
    #ll.print()
    ll.print()
    print(ll.search_in_ll("YELLOW"))
