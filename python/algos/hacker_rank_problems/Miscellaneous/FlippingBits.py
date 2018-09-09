# Complete the flippingBits function below.
def flippingBits(n):
    a = "{0:b}".format(n)
    a = "0"*(32-len(a)) + a
    b = ""
    for i in a:
        if i == '1':
            b += "0"
        else:
            b += "1"
    return int(b, 2)
