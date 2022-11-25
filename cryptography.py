import numpy as np
from fractions import Fraction

# Let's define two arrays we are gonna use in the process. The first will correspond to our alphabet, and the second will be a vector that contains all the elements of Z_29.

ALPHABET = ['_', 'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.']

string = str(input("Enter the string to process: "))

# We will use different arrays that are gonna change its state along the process, in order to keep code legible, we are gonna enumerate them all right below

# The name of the arrays is easy to understand. First Bi represents the base of the vector written below, while the name says it all.

B1_INDEXVECTOR = []
B1_STRINGVECTOR = []
B2_INDEXVECTOR = []
B2_STRINGVECTOR = []

# Right below you will find the two matrix that are gonna be used. The first one represent the matrix B1 to B2,in other words, our key. While the second matrix is the one we are going to use to encrypt our message

B1_B2 = np.array([[0, 1, 0], [1, 1, 1], [28, 0, 0]])
B2_B1 = np.array([[0, 0, 28], [1, 0, 0], [28, 1, 1]])

# Now we are gonna define a couple of functions

    # This is the most important function, as we are wokring in Z_29^3 we need, always, that the lenght of our index array to be a multiple of 3, now with this fuction, if necessary,  we fill the missing spaces

def fill_missing_spaces(indexvector):
    if len(indexvector) % 3 == 1:
        indexvector.append(0)
        indexvector.append(0)

    elif len(indexvector) % 3 == 2:
        indexvector.append(0)

    # This function turns every letter of a string and turns it into the number that it represents

def string_to_index(string, indexvector, alphabetvector):
    for i in string:
        for j in range(len(alphabetvector)):
            if i == alphabetvector[j]:
                indexvector.append(j)

    # This function turns every index of a vector of index and turns it into letter of the alphaber

def index_to_string(indexvector, stringvector, alphabetvector):
    TEMPINDEXVECTOR = []
    for i in range(len(indexvector)):
        TEMPINDEXVECTOR.append(indexvector[i] % 29)
        stringvector.append(alphabetvector[TEMPINDEXVECTOR[i]])

    # It is important to keep our message protected, that's why we will define a couple of functions to do this.

    # Given the change of basis matrix, the next step is to multiply each Z_29^3 vector to our matrix. The first step is to define a new vector each three elements of the array of index. In other words, to create a vector.
    
def change_of_basis_process(indexvector, changeofbasismatrix, resultingarray):
    TEMPVECTORTOMULTIPLY = np.array([[0], [0], [0]])
    TEMPVECTORENCRYPTED = np.array([[0], [0], [0]])

    for i in range(len(indexvector)):

        # The first part of this foor loop, assigns the values of the vector that is going to be multiplied

        if i % 3 == 0:
            TEMPVECTORTOMULTIPLY[0] = indexvector[i]
        elif i % 3 == 1:
            TEMPVECTORTOMULTIPLY[1] = indexvector[i]
        elif i % 3 == 2:
            TEMPVECTORTOMULTIPLY[2] = indexvector[i]

            # Now we take the vector we filled before and make the product between this vector and the change of basis matrix

            TEMPVECTORENCRYPTED = np.matmul(changeofbasismatrix, TEMPVECTORTOMULTIPLY)
            
            # The last part of the process is to take each of the vector coordinates and append them into an array

            for i in range(3):
                tempvalue = TEMPVECTORENCRYPTED[i][0]
                resultingarray.append(tempvalue)

# Now this is pure aesthetics, this will just make the string vector look better

def prettify(stringarray):
    for i in range(len(stringarray)):
        if stringarray[i] == '_':
            stringarray[i] = ' '

condition = int(input(
    "\n\nIs the string written in normal language or is it encrypted. \n\n If it's written in natural language, type '1' \n If it's encrypted type '2' \n\n Your answer here: "))



if condition == 1:

    string_to_index(string, B1_INDEXVECTOR, ALPHABET)
    fill_missing_spaces(B1_INDEXVECTOR)
    index_to_string(B1_INDEXVECTOR, B1_STRINGVECTOR, ALPHABET)

    change_of_basis_process(B1_INDEXVECTOR, B2_B1, B2_INDEXVECTOR)
    
    index_to_string(B2_INDEXVECTOR, B2_STRINGVECTOR, ALPHABET)

    #prettify(B1_STRINGVECTOR)

    print("\n\nThe message you typed was the following:", ''.join(B1_STRINGVECTOR))
    print("\n It can also be expressed as the following array:", B1_INDEXVECTOR)

    print("\n After a hard process of encrypting your message, the resulting string of characters is the following:", ''.join(B2_STRINGVECTOR))
    print("\n Good luck to everyone trying to decrypt this array: ", B2_INDEXVECTOR)

    print("\n\n")

if condition == 2:

    string_to_index(string, B2_INDEXVECTOR, ALPHABET)
    fill_missing_spaces(B2_INDEXVECTOR)

    change_of_basis_process(B2_INDEXVECTOR, B1_B2, B1_INDEXVECTOR)
    index_to_string(B1_INDEXVECTOR, B1_STRINGVECTOR, ALPHABET)

    #prettify(B1_STRINGVECTOR)

    print("\n\nThe message you typed was the following:", ''.join(B2_STRINGVECTOR))
    print("\n After a hard process of dencrypting your message, the resulting string of characters is the following:",
          ''.join(B1_STRINGVECTOR))
    print("\n You can thank me later")

    print("\n\n")














