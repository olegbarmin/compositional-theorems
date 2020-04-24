from first_task import Program


class Recursion(Program):

    def __init__(self, function, args, counter):
        super().__init__(function, args)
        self.counter = counter

    def __call__(self, *args, **kwargs):
        if self.counter > 0:
            recursion = Recursion(self.function, self.args + 1, self.counter - 1)
            next_iteration = InnerRecursion(self.function, self.args, self.counter - 1, recursion)

            return next_iteration()
        elif self.counter == 0:
            program = Program(function=self.function, args=self.args)
            return program()


class InnerRecursion:

    def __init__(self, function, args, counter, recursion):
        self.function = function
        self.args = args
        self.counter = counter
        self.recursion = recursion

    def __call__(self, *args, **kwargs):
        program = Program(self.function, self.args)
        program()

        return self.recursion()


if __name__ == "__main__":
    argument = 0
    counter = 9

    result = []
    recursion = Recursion(function=result.append, args=argument, counter=counter)
    recursion()

    print(result)
    assert len(result) == 10
