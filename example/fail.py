def increment(index=0):
    index += 1
    return index

def get_square(numb):
    return numb * numb

def print_numb(numb):
    print("Number is {}".format(numb))

index = 0
while index < 10:
    index = increment(index)
    print_numb(get_square(index))