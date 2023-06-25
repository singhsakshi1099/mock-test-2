# -*- coding: utf-8 -*-
"""mock test 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NzBU-t_0QbCEdgAOmvQ6y5gWrOq0YycD
"""

#1solution

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def isEmpty(self):
        return len(self.stack) == 0

#2 solution

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def isEmpty(self):
        return len(self.queue) == 0

