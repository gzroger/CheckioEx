__author__ = 'zoli'
import random
if __name__ == '__main__':
    print("{0:^40}".format("A"*2))
    for i in range(1, 20):
        chars = ["."]*i+["T"]+["A"]+["M"]
        random.shuffle(chars)
        chars[i:]=[]
        print("{0:>20}{0:<20}".format(''.join(chars)))
    print("{0:^40}".format("J"*4))
