def count(a, b):
    word = False
    a = " " + a + " "
    b = " " + b + " "

    result = 0

    for i in range(len(a) - 1):
        if a[i] == " " and a[i + 1] != " ":
            word = True
            result += 1
        else:
            word = False

    for i in range(len(b) - 1):
        if b[i] == " " and b[i + 1] != " ":
            word = True
            result += 1
        else:
            word = False

    return result


if __name__ == "__main__":
       count(a,b)
count("ramzsdf", "pama")
