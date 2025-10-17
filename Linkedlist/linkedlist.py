class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

A = Node(1)
B = Node(2)
C = Node(3)
A.next = B
B.next = C  

class LinkedList:
    def __init__(self):
        # Empty Linked List
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def clear(self):
        self.head = None
        self.n = 0
        
    def insert_head(self, data):
        # Create a new node
        new_node = Node(data)

        # Point new node's next to current head
        new_node.next = self.head
        # Update head to new node
        self.head = new_node
        # Increment size
        self.n += 1 

        return new_node

    def __str__(self):
        current = self.head
        result = ''
        while current:
            result += str(current.data) + ' -> '
            current = current.next
        result += 'None'
        return result
    
    def append(self, data):
        
        if self.head is None:
            return self.insert_head(data)

        new_node = Node(data)
        curr = self.head

        while curr.next != None: 
            curr = curr.next

        curr.next = new_node
        self.n += 1
        return new_node
    
    def insert_after(self, after, value):
        
        if self.head is None:
            return 'LinkedList is Empty.'
        
        if not after:
            print("The given previous node cannot be NULL")
            return
        
        new_node = Node(value)
        current = self.head
        while current!= None: 
            if current.data == after:
                break
            current = current.next

        if current != None: 
            print(current.data)
            new_node.next = current.next
            current.next = new_node
        else:
            s = f"Item {after} not found"
            print(s)
            return s

    #Challenge: what is the output of following program if head is passed as input?
    # 1->2->3->4->5
    def fun(self, head):
        if head is None:
            return
        if head.next.next is not None:
            print(head.data," ",end="")
            self.fun(head.next)
        print(head.data," ",end="")

    # Write a program to find max value and replace it with given value

    def findmax_replace(self,value):

        if self.head == None:
            return print("LL is Empty")
        
        curr = self.head
        max = curr 
        
        while curr != None:
            if curr.data > max.data:
                max = curr 
            curr = curr.next

        max.data = value    

    def odd_pos_sum(self):
        if self.head == None:
            return print(f" start Total sum:0") 
        pos = 0
        sum = 0
        curr = self.head
        while curr != None:
            if(pos % 2 != 0):
                sum = sum + curr.data
            curr = curr.next
            pos = pos + 1 
        print(f"Total sum:{sum}") 

    #In-place reverse of LinkedList
    def reverse(self):
        prev_node = None
        curr_node = self.head

                 #P.N C.N.   ->N.N  
        # Input: None 1(Head)->2->3->4->5
        # Output : None<-1<-2<-3<-4<-5(Head) 
       
        while curr_node != None:
            next_node = curr_node.next # next = 2
            curr_node.next = prev_node # 1.next = None : None<-1
            prev_node = curr_node # Now 1 is Prev_node
            curr_node = next_node # Now 2 is Curr_node
        self.head = prev_node

    def simpleprint(self):
        current = self.head
        result = ''
        while current:
            result += str(current.data) + ''
            current = current.next
        return result
            
      #input:  #An*/apple*a/day**keeps/*a//doctor*Away
      #output:   #An Apple a day Keeps A Doctor Away    
    def change_sentence(self):

        curr = self.head
        while curr != None:
            if curr.data == '/' or curr.data == '*':
                curr.data = ' '
                if curr.next.data == '*' or curr.next.data == '/':
                    curr.next.next.data = curr.next.next.data.upper()    
                    curr.next = curr.next.next                
            curr = curr.next

L = LinkedList()

L.insert_head(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6) 

Wordlist = LinkedList()

if __name__ == "__main__":
    characters = [
        'A', 'n', '*', '/', 'a', 'p', 'p', 'l', 'e', '*', 'a', '/', 'd', 'a', 'y',
        '*', '*', 'k', 'e', 'e', 'p', 's', '/', '*', 'a', '/', '/', 'd', 'o', 'c',
        't', 'o', 'r', '*', 'A', 'w', 'a', 'y'
    ]
for ch in characters:
        Wordlist.append(ch)

print(Wordlist.simpleprint())

Wordlist.change_sentence()

print(Wordlist.simpleprint())
