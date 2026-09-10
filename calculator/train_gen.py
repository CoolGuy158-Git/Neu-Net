import random

# Generate two pairs of double-digit numbers (a, b, c, d)

def gen_train(amount):
    num_list = []
    for i in range(amount):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        c = random.randint(10, 99)
        d = random.randint(10, 99)

        ans = (a + b) - (c + d)
        num_list.append(f"{a},{b},{c},{d} = {ans}")
    return num_list