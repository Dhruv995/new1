class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class doublyll():

    def __init__(self):
        self.head=None

    def insertbeg(self):
        value=int(input("Enter the value to be inserted"))
        temp=self.head
        if self.head==None:
            newNode=Node(value)
            self.head=newNode
        else:
            newNode=Node(value)
            self.head.previous=newNode
            newNode.next=self.head
            self.head=newNode

    def insertend(self):
        value=int(input("enter the value to be inserted"))
        newNode=Node(value)
        temp=self.head
        while temp is not None:
            temp=temp.next
        temp=newNode
        newNode.previous=temp
        

    def delete(self):
        value=int(input("enter the value to be deleted"))
        temp=self.head
        while(temp!=None):
            if(temp.data==value):
                self.head=temp.next
                temp.previous=None

                temp.next=None
            else:
                while(temp.next!=None):
                    if(temp.data==value):
                        break
                    temp=temp.next
                if(temp.next==value):
                    temp.previous.next=temp.next
                    temp.next.previous=temp.previous
                    temp.next=None
                    temp.previous=None
                else:
                    temp.previous.next=None
                    temp.next=None
        if (temp==None):
            print('Error 404')

    

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,'\t')
            temp=temp.next

print("Welcome to doubly linklist")
dll=doublyll()
running=True
while running:
    print("enter choice \1.insert at beginning \2.insert at end \3.delete an element \4.display an element")
    choice=int(input("enter the choice"))
    if choice==1:
        dll.insertbeg()
    elif choice==2:
        dll.insertend()
    elif choice==3:
        dll.delete()
    elif choice==4:
        dll.display()
    else:
        print("invalid choice")
        break
    choose=input("do you want to continue(y/n)")
    if choose=='n':
        running=False
        print("thank you")