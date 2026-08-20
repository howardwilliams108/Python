def precedence(op): # return a priority of operators
    if op in ('-', '+'):
        return 1
    if op == '*':
        return 2
    return 0


def is_operator(ch): #I check if a character is an operator
    return ch in ['-', '+', '*']


def infix_to_postfix(infix: str) -> str: #converting expressons to postfix
    stack = []
    output = []

    tokens = infix.split() # splitting all input into pieces

    for token in tokens:

        if token.isdigit():
            output.append(token)
            #numbs going directly to output
        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()

        elif is_operator(token):
            while (
                stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token)
                
            ):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output) #through using other notes and practice, return will result as a string


def infix_to_prefix(infix: str) -> str:
    tokens = infix.split()[::-1]

    reversed_tokens = []
    for token in tokens:
        if token == '(':
            reversed_tokens.append(')')

        elif token == ')':
            reversed_tokens.append('(')

        else:
            reversed_tokens.append(token)


    reversed_expr = ' '.join(reversed_tokens)
  # rebuilding string and converting to postfix  
    postfix = infix_to_postfix(reversed_expr)

    return ' '.join(postfix.split()[::-1])


def evaluate_postfix(postfix: str):#computing results
    stack = []
    tokens = postfix.split()

    for token in tokens:
        if token.isdigit():
            stack.append(float(token))

        elif is_operator(token):
            b = stack.pop()
            a = stack.pop()

            if token == '+': # performing operations below
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

    return stack.pop()


def evaluate_prefix(prefix: str):
    stack = []
    tokens = prefix.split()[::-1] # reversing nu,ner

    for token in tokens:
        if token.isdigit():
            stack.append(float(token))

        elif is_operator(token):
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

    return stack.pop()



def main():
    infix = input("Enter infix expression: ")

    postfix = infix_to_postfix(infix)
    prefix = infix_to_prefix(infix)

    #evaluating postfix and prefix
    postfix_result = evaluate_postfix(postfix)

    prefix_result = evaluate_prefix(prefix)


    print("Postfix: ", postfix)
    print("Prefix :", prefix)
    print("Postfix Evaluation: ", postfix_result)
    print("Prefix Evaluation: ", prefix_result)


if __name__ == "__main__":
    main()