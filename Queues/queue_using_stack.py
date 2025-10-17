class Node:

  def __init__(self,value):
    self.data = value
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

    
    def queue_using_stack(self, arr, pattern):
        enqueue_stack = Stack()
        dequeue_stack = Stack()
        arr_index = 0
        dequeued_items = []

        for command in pattern:
            if command == 'e':
                if arr_index < len(arr):
                    enqueue_stack.push(arr[arr_index])
                    arr_index += 1
            elif command == 'd':
                if dequeue_stack.isEmpty():
                    while not enqueue_stack.isEmpty():
                        dequeue_stack.push(enqueue_stack.pop())
                if not dequeue_stack.isEmpty():
                    dequeued_items.append(dequeue_stack.pop())
            else:
                continue
        
        print("Stage 1 enqueue_stack items:", enqueue_stack.traverse())
        print("Stage 1 dequeued_items items:", dequeued_items)

        final_queue = []
        temp_stack = Stack()

        while not dequeue_stack.isEmpty():
            value = dequeue_stack.pop()
            final_queue.append(value)
            temp_stack.push(value)

        while not temp_stack.isEmpty():
            dequeue_stack.push(temp_stack.pop())

        while not enqueue_stack.isEmpty():
            temp_stack.push(enqueue_stack.pop())

        while not temp_stack.isEmpty():
            value = temp_stack.pop()
            final_queue.append(value)
            enqueue_stack.push(value)

        print("Dequeued items:", dequeued_items)
        print("Remaining queue:", final_queue)

S = Stack()

S.queue_using_stack([1,2,3,4],"eeded")

        
