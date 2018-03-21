def sumNumbers(st):
    num = ''
    runSum = 0
    for d in st:
        if d.isdigit():
            num += d
        else:
            if len(num) > 0:
                runSum += int(num)
            num = ''
    if len(num) > 0:
        runSum += int(num)
    return runSum


if __name__ == '__main__':
    print sumNumbers("abc123xyz")
    print sumNumbers("aa11b33")
    print sumNumbers("7 11")

