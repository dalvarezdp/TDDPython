
class CalculatorSyntaxError(Exception):
    pass


class Calculator(object):

    ADD = "+"
    SUBTRACT = "-"
    OPERATORS = ["+", "-"]

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def eval(self, expression):
        result = None
        next_operation = None
        for item in self.parse(expression):
            if item in self.OPERATORS:
                next_operation = item
            elif result is None:
                result = item
            elif next_operation == self.ADD:
                result = self.add(result, item)
                next_operation = None
            elif next_operation == self.SUBTRACT:
                result = self.subtract(result, item)
                next_operation = None
        return result

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

