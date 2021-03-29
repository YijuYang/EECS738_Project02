
import numpy as np
import random
import string
import HMM

NUMBER_OF_LINES = 30
MAX_NUMBER_OF_WORDS_PER_LINE = 15
end = "tokEND"

data = HMM.readFromFile()
HMM.train(data)
play = []
print("Start generating")
for i in range(0, NUMBER_OF_LINES):
    line = HMM.generateLine()
    play.append(' '.join(line))


print("Printing: \n")
i = 1
for line in play:
    print('\t',i, ": ", line,'\n')
    i += 1
