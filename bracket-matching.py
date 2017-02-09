class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data)>0:
            return self.data.pop()
        return None

    def size(self):
        return len(self.data)

    def __len__(self):
        return self.size()

    def __str__(self):
        return "{}".format(self.data)

def test_brackets(string):
    ss = Stack()
    for char in string:
        if char == "{" or char == "(" or char == "[":
            ss.push(char)
            print(ss)
        elif char =="}" and ss.pop() == "{":
            print(ss)
        elif char ==")" and ss.pop() == "(":
            print(ss)
        elif char =="]" and ss.pop() == "[":
            print(ss)
        elif char == "}" or char == ")" or char == "]":
            print(False)
            return False
    if len(ss) == 0:
        print(True)
        return True
    else:
        print(False)
        return False

# True
test_brackets('abc(123)')
print()

#returns True
test_brackets('a[bc(123)]')
print()

#returns True
test_brackets('a{b}{c(1[2]3)}')
print()

#returns True
test_brackets('()')
print()

#returns True -- no brackets = correctly matched
test_brackets('abc123yay')
print()

#returns False -- missing closing bracket
test_brackets('abc(123')
print()

#returns False -- inproperly nested
test_brackets('a[bc(12]3)')
print()

#returns False -- inproperly nested
test_brackets('a{b}{c(1}[2]3)')
print()
