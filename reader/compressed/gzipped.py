import gzip
import sys

opener = gzip.open

if __name__ == '__main__':
    f = gzip.open(sys.argv[1], mode='rt')
    f.write(' '.join(sys.argv[2:]))
    f.close()
