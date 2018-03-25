def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def eval(st):
    #import pdb; pdb.set_trace()
    stack = []
    terms = st.split(' ')
    operators = ['+', '-', '*', '/']
    operatorMaping = {'+':add, '-': minus, '*': multiply , '/': divide}
    evaluated = False
    i = 0
    while i < len(terms):
        t = terms[i]
        if t in operators:
            if i >= len(terms):
                return 'Invalid'
            nextTerm = terms[i + 1]
            i += 1
            if isFloat(nextTerm):
                if len(stack) == 0:
                    return 'Invalid 1'
                val1, val2 = stack.pop(), float(nextTerm)
                stack.append(operatorMaping[t](val1, val2))
            elif nextTerm == '(':
                stack.append(t)
            else:
                return 'Invalid 2'
        elif t == ')':
            if len(stack) < 3:
                return 'Invalid 3'
            val1, op, val2 = stack.pop(), stack.pop(), stack.pop()
            stack.append(operatorMaping[op](val1, val2))
        elif t == '(':
            continue
        elif isFloat(t):
            stack.append(float(t))
        else:
            return 'Invalid 5'
        i += 1
        print stack
    print len(stack)
    return stack.pop()


print eval('1 * ( 2 + 3 ) - ( 5 + 4 )')


            


