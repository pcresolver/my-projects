## Server names
SERVERS = ['APP1', 'APP2', 'APP3', 'APP4']

# Solution 1 : using global variable (not ideal)
#number_of_servers = len(SERVERS)
#current_server = SERVERS[-1]

#def get_server():
#    # Input: none
#    # Output: Return the server name
#    # Use a loop to return the app to be used in order
#    global current_server
#    if current_server == SERVERS[-1]: #reached the end of the list
#       current_server = SERVERS[0] #loop back to the beginning
#    else:
#       current_server = SERVERS[SERVERS.index(current_server) + 1] # move on to the next server in the list
#    return current_server
#    pass

# Solution 2 using cycle in itertools module. still using global variable
#import itertools
##infinite loop iterator
#cycle = itertools.cycle(SERVERS)
#def get_server():
#    global cycle
#    return cycle.__next__()

# solution 3 Uses a generator function, yields an answer and uses 'next' to get the next result
def get_server():
    def f(): # this is a 'generator' function that changes the list - rotates the elements
        while True: # always do this:
            i = SERVERS.pop(0) # i now contains the first element and deletes from list
            SERVERS.append(i) # adds what was the old first element to the end 
            yield i # this returns 'i' and waits for the commnad 'next' to go again
    return next(f()) 
    
## Testing the function
if __name__ == '__main__' : 
    for i in range(9):
        print(get_server()) # should get App1, 2, 3 looping