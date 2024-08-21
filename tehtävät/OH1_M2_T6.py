import math
import random

kolme = []
nelja = []

while(len(kolme)<3):
    kolme.append(random.randint(0,9))

while(len(nelja)<4):
    nelja.append(random.randint(1,6))

print(f"kolmenumeroinenkoodi: {kolme}\nneljänumeroinenkoodi: {nelja}")