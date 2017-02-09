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

# my solution
def test_brackets(string):
    ss = Stack()
    for char in string:
        if char in "{[(":
            ss.push(char)
            print(ss)
        elif char =="}" and ss.pop() == "{":
            print(ss)
        elif char ==")" and ss.pop() == "(":
            print(ss)
        elif char =="]" and ss.pop() == "[":
            print(ss)
        elif char in "]})":
            print(False)
            return False
    if len(ss) == 0:
        print(True)
        return True
    else:
        print(False)
        return False

# steve's solution
def test_brackets_steve(ss):
  opening = "([{"
  closing = ")]}"
  stack = []
  for letter in ss:
    # put all opening characters on the stack to wait to be matched.
    if letter in opening:
      stack.append(letter)
    if letter in closing:
      # grab the first thing off the stack and make sure it matches.
      first = stack.pop()
      if first == "[" and not letter == "]":
        return False
      if first == "(" and not letter == ")":
        return False
      if first == "{" and not letter == "}":
        return False

  # if there's anything left in the stack that means
  # something was left waiting to be matched.
  if len(stack) > 0:
    return False

  return True



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
