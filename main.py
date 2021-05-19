from stack import Stack


def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True
    return False


string = '{{[()]}}'


def balanced_brackets():
    stack = Stack()
    for i in string:
        if i in ['[', '{', '(']:
            stack.push(i)
        elif i in [']', '}', ')']:
            if stack.isEmpty():
                return 'Несбалансированно'
            top_element = stack.pop()
            if not compare(top_element, i):
                return 'Несбалансированно'
    if not stack.isEmpty():
        return 'Несбалансированно'

    return 'Сбалансированно'


if __name__ == "__main__":
    print(balanced_brackets())


