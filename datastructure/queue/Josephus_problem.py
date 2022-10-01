class Queue:
    def __init__(self):
        self.items = []
        self.first_index = 0
     
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if self.first_index == len(self.items):  # (1)
            print('Out of Index')
        else:
            result = self.items[self.first_index]
            self.first_index += 1
            return result

def josephus_problem(n,k):
    q = Queue()
    for i in range(1,n+1):
        q.enqueue(i)

    while not (len(q.items) - q.first_index == 1):
        for i in range(k-1):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.items[q.first_index]