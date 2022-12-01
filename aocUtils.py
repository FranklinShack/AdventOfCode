import math
import re
import operator
import functools


######################## FILE INPUT AND DATA VISUALIZATION ######################## 

#parse files
def readFile(file):
    f = open(file)
    f = f.read().splitlines()

    #make ints
    new = []
    for i in f:
        new.append(i)
    return new



######################## USEFUL CONSTS ########################

LETTERS = [x for x in 'abcdefghijklmnopqrstuvwxyz']
VOWELS = set([x for x in 'aeiou'])
CONSONANTS = set([x for x in LETTERS if x not in VOWELS])

######################## MATH STUFF ########################

def multList(lst):
    return functools.reduce(operator.mul, lst, 1)

def factors(n):
    '''Get all factors of n'''
    return list(filter(lambda x: n%x == 0, range(1,n+1)))

def gcd(x,y):
    #yes I know this is dumb but I want to just type gcd(x,y) and/or lcm(x,y) without having to do from math import gcd,lcm,etc... in my solution file.
    return math.gcd(x,y)

def lcm(x,y):
    #yes I know this is dumb but I want to just type gcd(x,y) and/or lcm(x,y) without having to do from math import gcd,lcm,etc... in my solution file.
    return math.lcm(x,y)

def gcf(x,y):
    '''Return the GCF of two numbers'''
    return max(list(set(factors(x)) & set(factors(y))))

def _sieveOfEratosthenes(n):
    '''shamelessly copied from https://github.com/iKevinY/advent/blob/master/2019/utils.py'''
    """http://stackoverflow.com/a/3941967/239076"""
    # Initialize list of primes
    _primes = [True] * n

    # Set 0 and 1 to non-prime
    _primes[0] = _primes[1] = False

    for i, is_prime in enumerate(_primes):
        if is_prime:
            yield i

            # Mark factors as non-prime
            for j in xrange(i * i, n, i):  # NOQA
                _primes[j] = False

def primes(n):
    '''Return list of all primes from [2,n)'''
    '''shamelessly copied from https://github.com/iKevinY/advent/blob/master/2019/utils.py'''
    return list(_sieveOfEratosthenes)

def minmax_lst(lst):
    '''Returns the min and max values of a given list.'''
    return [min(lst), max(lst)]

######################## MATRIX OPERATIONS ######################## 

def rotate_matrix_cw(matrix):
    '''Returns the given matrix rotated 90 deg clockwise'''
    new_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])
    for c in range(0,columns):
        new_row = []
        for r in list(range(0,rows))[::-1]:
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)
    return new_matrix

def rotate_matrix_ccw(matrix):
    '''Returns the given matrix rotated 90 deg counterclockwise'''
    new_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])
    for c in list(range(0,columns))[::-1]:
        new_row = []
        for r in list(range(0,rows)):
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)
    return new_matrix

def rotate_matrix(matrix, dir):
    '''Rotate a matrix 90 degrees either clockwise or counterclockwise.
       Use rotate_matrix(matrix, 1) for clockwise, rotate_matrix(matrix, -1) for counterclockwise'''
    return rotate_matrix_cw(matrix) if dir > 0 else rotate_matrix_ccw(matrix)

def transpose_matrix(matrix):
    '''Return the transpose of a given matrix'''
    new_matrix = []
    rows = len(matrix)
    columns = len(matrix[0])

    for c in range(0, columns):
        new_row = []
        for r in range(0, rows):
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)
    return new_matrix



######################## SETS AND UNIQUENESS ########################

def make_unique(lst):
    '''Returns a list of all unique elements in the original list'''
    return list(set(lst))

def all_unique(lst):
    '''Checks if a list contains all unique elements'''
    return len(lst) == len(set(list))