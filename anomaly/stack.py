stack = []

def add_digit(*digits):
    global stack
    for digit in digits:
        if len(stack) < 1: push()
        if digit != '.':
            stack[-1] += str(digit)
        elif digit == '.' and '.' not in stack[-1]:
            stack[-1] += str(digit)
        else: pass

def push(*arg):
    global stack
    for i in arg:
        stack.append(str(i))
    stack.append('')

def return_stack(n=-1):
    global stack
    try:
        return stack[n]
    except IndexError:
        return None

def pop():
    global stack
    try:
        return stack.pop()
    except:
        pass

def delete():
    global stack
    if stack[-1] != '':
        stack[-1] = stack[-1][:len(stack[-1])-1]
    else:
        pass

def clear(whole_stack=False):
    global stack
    if stack[-1] != '' or [] and whole_stack != True:
        stack[-1] = ''
    else:
        stack = []
