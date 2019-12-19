class Stack:
    def __init__(self):
        self.array=[]
    def push(self,item):
        self.array.append(item)
    def pop(self):
        return self.array.pop()
    def is_empty(self):
        return len(self.array)==0

def check(exp):
    left = "{[("
    right = "}])"
    myStack = Stack()
    for ch in exp:
        if ch in left:
            myStack.push(ch)
        elif ch in right:
            if myStack.is_empty():
                return False
            if right.index(ch) != left.index(myStack.pop()):
                return False

    return myStack.is_empty()

print(check("(()"))