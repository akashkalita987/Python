from collections import deque

# ==========================================
# 1. STACK DEMONSTRATION (LIFO: Last In, First Out)
# ==========================================
print("--- STACK DEMONSTRATION ---")

# Initialize an empty stack
stack = deque()

# Push elements onto the stack
print("Pushing elements: 'A', 'B', 'C'")
stack.append('A')
stack.append('B')
stack.append('C')
print(f"Current Stack: {list(stack)}")

# Pop elements from the stack (removes from the top/right)
print(f"Popped element: {stack.pop()}")
print(f"Popped element: {stack.pop()}")
print(f"Stack after pops: {list(stack)}")

# Peek at the top element without removing it
stack.append('D')
print(f"Added 'D'. Top element (Peek): {stack[-1]}")
print("\n" + "="*40 + "\n")


# ==========================================
# 2. QUEUE DEMONSTRATION (FIFO: First In, First Out)
# ==========================================
print("--- QUEUE DEMONSTRATION ---")

# Initialize an empty queue
queue = deque()

# Enqueue elements (add to the back/right)
print("Enqueueing elements: '1', '2', '3'")
queue.append('1')
queue.append('2')
queue.append('3')
print(f"Current Queue: {list(queue)}")

# Dequeue elements (remove from the front/left)
print(f"Dequeued element: {queue.popleft()}")
print(f"Dequeued element: {queue.popleft()}")
print(f"Queue after dequeues: {list(queue)}")

# Peek at the front element without removing it
queue.append('4')
print(f"Added '4'. Front element (Peek): {queue[0]}")