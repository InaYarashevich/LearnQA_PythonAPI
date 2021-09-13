import random
import string

def get_random_string(length):
    letters = string.ascii_letters
    external_id = ''.join(random.choice(letters) for i in range(length))
    print(external_id)

get_random_string(1025)