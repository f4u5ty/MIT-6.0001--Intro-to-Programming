# Problem Set 4A
# Name: Luis Echevarria


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    if len(sequence) == 1: 
            return [sequence]
    
    """
    if sequence is a single character. There is only way one to order it.
    returns a singleton list.
    """
    """
    suppose we have a list of all permutations but the first character.
    """
    perms = get_permutations(sequence[1:])
    
    
    """
    this is our list of permutations with all but the first character. 
    now we have to insert the first character of sequence into every position for every permutation. 
    so, here we would need the length of each string.
    """
    char = sequence[0]
    """
    We need to iterate over the perms, and the iterate over the strings in perms and add the character, 
    then save the result to a list. 
    """ 
    result = []
    
    i = 0 
    while i < len(perms): #iteration over list
        i2 = 0 
        while i2 < len(perms[i])+1: #iteration over string. 
            result.append(perms[i][:i2]+char+perms[i][i2:])
            i2+=1
        i2 = 0 
        i+=1 
    
    return result


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'bri'
    print('Input', example_input) 
    print('Expected Output:', ['bri', 'rbi', 'rib', 'bir', 'ibr', 'irb'])
    
    
    example_input = 'ust'
    print('Input', example_input)
    print('Expected Output:', ['ust', 'sut', 'stu', 'uts', 'tus', 'tsu'])
    
    example_input = 'ze0' 
    print('Input', example_input) 
    print('Expected Output:', ['ze0', 'ez0', 'e0z', 'z0e', '0ze', '0ez'])
    
   
