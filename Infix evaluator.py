TOKENS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ** b,
    '**': lambda a, b: a ** b,
    '%': lambda a, b: a % b,
    'mod': lambda a, b: a % b,
    '//': lambda a, b: a // b
}

class CalculatorError(Exception):
    pass

def make_pop(stack):
    def pop():
        try:
            return stack.pop()
        except IndexError:
            raise CalculatorError('Not enough arguments for function')
    return pop

def call():
    stack = []
    pop = make_pop(stack)
    buf = []

    calculation = iter(input('> ') + ' ')

    for char in calculation:
        if char not in ' \t':
            buf.append(char)
            continue

        token = ''.join(buf)
        if not token:
            continue

        if token in TOKENS:
            a = pop()
            b = pop()
            function = TOKENS[token]
            try:
                return_value = function(b, a)
            except ZeroDivisionError:
                raise CalculatorError("Can't devide by zero")
            else:
                stack.append(return_value)
        else:
            try:
                token = float(token)
            except ValueError:
                raise CalculatorError('{!r} is not a number'.format(token))
            stack.append(token)

        buf = []

    if len(stack) > 1 or buf:
        raise CalculatorError('Invalid function, not enough operators.', stack, buf)

    if stack[0] % 1:
        print(stack[0])
    else:
        print(int(stack[0]))

def main():
    while True:
        try:
            call()
        except CalculatorError as e:
            print(e)

if __name__ == '__main__':
    print('Press ^C to exit')
    try:
        main()
    except KeyboardInterrupt:
        pass
    except EOFError:
        print()
    print('Goodbye!')