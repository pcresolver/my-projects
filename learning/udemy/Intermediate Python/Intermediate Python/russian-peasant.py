## The Russian Peasant's Algorithm with testing and using CACHE to show how caching can speed up algos.
## I use recursion for fun
## Been around for a long time (1700s)

## Multiply two numbers together
## Requirements: multiply one by two and divide other by two
## Keep going til get to 1 on LHS
## Add up the RHS for all odd values on LHS

## Eg. 24 * 16
## 12 * 32
## 6 * 64
## 3 * 128
## 1 * 256 {round down}
## Add 128 and 256 to get the correct answer 384

## Input 2 numbers
## Calculate product
## Output 1 answer (the product)


import math # Used to use floor function to keep integar values
import time # We will use this to test efficiency

CACHE = {} # used to store results as they are calculated to prevent repeat calcualtions

def multiply(left, right, answer, key): # including answer so that it isn't reset when during iteration. Don't know if this is needed or best way but it works.
    if key in CACHE: # we have calculated this result before 
        print("been there done that, here is the CACHE:", CACHE)
        answer = CACHE[key] #return the answer stored in the dictionary
        return answer
    else: 
        print("OK, this is new. here is the CACHE", CACHE)
        if left == 1: # odd value on left so we add to total
            answer += right
            CACHE[key] = answer # store this in CACHE
            print(CACHE)
            return answer # we have reached end of iteration
        else:
            if left % 2 == 1: # odd value on left so we add to total
                answer += right
            left = math.floor(left/2) # requires rounding down for method to work
            return multiply(left, right * 2, answer, key) # passes right * 2 as part of the method


def test_multiply():
    left = 357
    right = 16
    key = (left, right) # used to test if we have done this before
   
    start_time = time.time()
    print(multiply(357, 16, 0, key))
    print("Multiply algorithm took {0} seconds ".format(time.time() - start_time))

    start_time = time.time() # repeat time test with same values to see if cache saved time
    print(multiply(357, 16, 0, key))
    print("Multiply algorithm took {0} seconds ".format(time.time() - start_time))

    assert multiply(357, 16, 0, key) == 5712

# print(multiply(13,13,0))
test_multiply()

