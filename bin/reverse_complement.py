import sys

def reverse_complement(seq):
    complement = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
    return ''.join(complement.get(b,'N') for b in reversed(seq.upper()))

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('>'):
            print(line.strip() + '_RC')
        else:
            print(reverse_complement(line.strip()))
