import string
import random


def get_random_strin(N):

    res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=N))

    print("The generated random string : " + str(res))

    return res

get_random_strin(10)





