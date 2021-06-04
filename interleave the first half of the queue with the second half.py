q = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stack = []

# Insert first half of the elements to the stack
for i in range(len(q)//2):
    stack.append(q.pop(0))
# Insert first half of the elements to the stack

# Enqueue
for i in range(len(stack), 0, -1):
    q.append(stack.pop())
# Enqueue

# Dequeue and Enqueue first half of the queue
for i in range(0, len(q)//2):
    stack.append(q.pop(0))

for i in range(len(stack)):
    q.append(stack.pop(0))
# Dequeue and Enqueue first half of the queue

# Push half of the elements to the stack
for i in range(0, len(q)//2):
    stack.append(q.pop(0))
# Push half of the elements to the stack

# Alternately remove elements from stack and queue
q2 = []
for i in range(len(q)):
    q2.append(stack.pop())
    q2.append(q.pop(0))
# Alternately remove elements from stack and queue

print(q2)

# print(q)
# print(stack)
