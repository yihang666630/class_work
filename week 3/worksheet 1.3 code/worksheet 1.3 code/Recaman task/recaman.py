def recaman():
    L = int(input("Length of sequence: ")) # this should be your only input
    # Your code for the Recaman Sequence
    # You should store the sequence 
    # in an appropriate data structure named 'sequence'
    # You may wish to use further output for 
    # testing purposes while you develop your code
    sequence = []
    n = 0
    while n < L:
        if n == 0:
           sequence.append(0)
           #print(0)
        else:
            a_n = sequence[n-1] - n
            if a_n > 0 and a_n not in sequence:
                sequence.append(a_n)
            else:
                a_n = sequence[n-1] + n
                sequence.append(a_n)
        n += 1
    b = ', '.join(str(item) for item in sequence)
    return b   
# this method is reasonably independent of the choice of data structure
if __name__ == "__main__":
    print(recaman())
# The web page
#  https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 
# 80 numbers in the sequence
