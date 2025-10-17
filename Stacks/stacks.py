class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Empty Stack
        self.top = None
        self._count = 0

    def isEmpty(self):
        return self._count == 0
    
    def push(self,value):
        
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._count += 1

    def traverse(self):

        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.top.data
        
    def pop(self):

        if self.isEmpty():
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            self._count -= 1
            return data
        
    def size(self):
        return self._count

    def reverse_string(self,text):
        s = Stack()
        for i in text:
            s.push(i)
        result = ""
        while(not s.isEmpty()):
            result += s.pop()
        print(result)

    def text_editor_undo_redo(self,txt,pattern):

        s_undo = Stack()
        s_redo = Stack()

        for i in txt:
            s_undo.push(i)

        for k in pattern:
            if k == 'u':
                if not s_undo.isEmpty():
                    data = s_undo.pop()
                    s_redo.push(data)
            elif k == 'r':
                if not s_redo.isEmpty():
                    data = s_redo.pop()
                    s_undo.push(data)

        result_chars = []
        while not s_undo.isEmpty():
            result_chars.append(s_undo.pop())

        result = ''.join(reversed(result_chars))
        print(result)

    
 
S = Stack()
#S.reverse_string("Hello")
#S.text_editor_undo_redo("Kolkata","uurrurur")

L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

# Find the celebrity

def find_the_celebrity(L):
    s = Stack()

    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if L[i][j] == 0: 
            #j is no a celebrity
            s.push(i)
        else: 
            #i is not celeb
            s.push(j)

    if s.isEmpty():
        print("No celebrity")
        return

    celebrity = s.pop()

    for other in range(len(L)):
        if other == celebrity:
            continue    
        if L[celebrity][other] == 1 or L[other][celebrity] == 0:
            print("No one is celebrity.")
            return

    print("This is celebrity:",celebrity)


find_the_celebrity(L)

# Balanced bracket or the paranthesis problem
 
