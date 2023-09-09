class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0

    def get_counter(self):
        return self.__count

    def pop(self):
        Stack.pop(self)
        self.__count += 1



stack_object = AddingStack()
stk = CountingStack()

for i in range(1, 6):
    stack_object.push(i)
print("Sum =", stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())

for i in range(5):
    stk.push(i)
    stk.pop()
print("Number of elements pushed and popped:", stk.get_counter())
