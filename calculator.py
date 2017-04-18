
class CalculatorSyntaxError(Exception):
    pass


class Calculator(object):

    OPERATORS = ["+", "-"]

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def eval(self, expression):
        return 10

    def parse(self, expression):
        result = list()
        position = 0
        for item in expression.split(" "):
            if item in self.OPERATORS:
                if position % 2 != 0:   # es par
                    result.append(item)
                else:
                    raise CalculatorSyntaxError("Unexpected operator {0} found".format(item))
            else:
                try:
                    if position % 2 == 0:  # es par
                        result.append(int(item))  # convierto item en un entero
                    else:
                        raise CalculatorSyntaxError("Unexpected number {0} found".format(item))
                except ValueError:
                    raise CalculatorSyntaxError("Unknown item {0}".format(item))
            position += 1
        return result

