# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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
    char_list = list(sequence)
    if len(sequence) == 1:
        return char_list
    else: 
        first = sequence[0]
        remaining = sequence[1:]
        permutations_of_rest = get_permutations(remaining)
        result = []

        for permutation in permutations_of_rest:
            for position in range(len(permutation)+1):
                new = permutation[:position] + first + permutation[position:]
                result.append(new)
        
        return result 
        
print(get_permutations("abcd"))



