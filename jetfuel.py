import random
import jetfuel_images as jf_i

def find(usr_msg, list_of_terms):
    lot = list_of_terms
    if type(lot) == type('string'):      # Converts string to list if passed a string
        lot = [lot]
    
    for term in lot:    # Searches the usr_msg, which must be passed from JFCMSB main for the given keywords aka terms
        if term in usr_msg:
            return True


def randomeme():
    memelist_length = len(jf_i.random_memes)
    return jf_i.random_memes[random.randint(0,memelist_length)]

