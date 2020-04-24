from first_task import Program


class Minimization(Program):

    def __call__(self, *args, **kwargs):
        value = 0

        while True:
            value += 1
            function_result = self.call_function(value)

            if function_result == 0:
                break

        return value

    def call_function(self, value):
        return self.function(self.args, value)


def subtract(left_arg, right_arg):
    return left_arg - right_arg


if __name__ == "__main__":
    argument = 10

    minimization = Minimization(function=subtract, args=argument)
    print(minimization())
