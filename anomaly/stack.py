class Stack():
    def __init__(self):
        self.stack = []

    def add_digit(self, *digits):
        for digit in digits:
            if len(self.stack) < 1: self.add_number()
            if digit != '.':
                self.stack[-1] = self.stack[-1]+str(digit)
            elif digit == '.' and '.' not in self.stack[-1]:
                self.stack[-1] = self.stack[-1]+str(digit)
            else: pass

    def add_number(self, *arg):
        try:
            for i in arg:
                self.stack.append(str(i))
            self.stack.append('')
        except ValueError:
            pass

    def pop(self):
        try:
            if self.stack[-1] == '': self.stack.pop()
            return self.stack.pop()
        except:
            return None

    def delete_digit(self):
        if self.stack[-1] != '':
            self.stack[-1] = self.stack[-1][:len(self.stack[-1])-1]
        else:
            pass

    def clear(self):
        try:
            if self.stack[-1] != '':
                self.stack[-1] = ''
            elif self.stack[-1] == '':
                self.stack = []
            else:
                pass
        except IndexError:
            pass
