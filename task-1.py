class Program:

    def __init__(self, function, args):
        self.function = function
        self.args = args

    def __call__(self, *args, **kwargs):
        return self.function(self.args)


class Superposition(Program):

    def __call__(self, *args, **kwargs):
        result_list = []
        for arg_func in self.args:
            result = arg_func()
            result_list.append(result)
        self.function(*result_list)


args = [5, 4, 3, 2, 1]
program_list = []
for func in [min, max, sum]:
    program_list.append(Program(func, args=args))

result_list = []
superposition = Superposition(function=print, args=program_list)  # <- Create superposition.
superposition()
