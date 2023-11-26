class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def printLL(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data) + ' --> '
            itr = itr.next

        print(liststr)

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def get_length(self):
        count =0;
        itr= self.head
        while itr:
            count+=1
            itr= itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index ==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while count<index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self,index,data):
        if index<=0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index==0:
            newNode= Node(data)
            newNode.next=self.head
            self.head= newNode
            return
        itr = self.head
        count=0
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next= node




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(98)
    ll.insert_at_begining(59)
    ll.insert_at_end(8769)
    ll.insert_at_end(876798)
    ll.insert_at_end(876578)
    ll.printLL()
    ll.remove_at(1)
    ll.printLL()

