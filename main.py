"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra, rb = foo(x-1), foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    longestRun = 0
    currentRun = 0
    for i in range(len(mylist)):
        currentRun = currentRun + 1 if mylist[i] == key else 0
        if currentRun > longestRun:
            longestRun = currentRun
    return longestRun


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    '''

    binary split lists

    if len(list) = 1:
        return Result(nLrun connecting, nRrun connecting, longest, T/F)

        (left index is key or not, right index is key or not, longest, T/F)

        if T & T
         = R(1, 1, max1 + max2, T)
        if (0, 1) (1,0)
        = if max < 2


        max(left + right, max(long1,long2))

        USE THE RESULTS TO BUILD BACK UP THE NEXT RESULTS,
        HELPER FUNCTION COMPARING THE TWO RESULTS AND RETURNING NEW RESULT

    base case:
        len(list) = 1
            --> check if key or not
            --> 111 or 000

    #TODO
    merging
    how to merge after breakdown

        tail left inherited, tail right inherited

    '''
    """
    if(len(mylist) == 1):
        return longest_run_recursive(mylist[0] = Result(1,1,1,True)) if myList[0] == key or myList[0].is_entire_range else longest_run_recursive(mylist[0] = Result(0,0,0,False))

    mid = len(mylist) // 2

    pass
    """
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        mid = len(mylist) // 2
        return compareResults(longest_run_recursive(mylist[:mid], key), longest_run_recursive(mylist[mid:], key))

def compareResults(left, right):
    #left_size  # run on left side of input
    #right_size # run on right side of input
    #longest_size  # longest run in input
    #is_entire_range
    """
    if len(list) = 1:
        return Result(nLrun connecting, nRrun connecting, longest, T/F)

        (left index is key or not, right index is key or not, longest, T/F)

        if T & T
         = R(1, 1, max1 + max2, T)
        if (0, 1) (1,0)
        = if max < 2


        max(left + right, max(long1,long2))
        """

    #Case 1: entire range is key
    if left.is_entire_range and right.is_entire_range:
        return Result(left.longest_size + right.longest_size,left.longest_size + right.longest_size,left.longest_size + right.longest_size, True)

    #Case 2: one is entire range but other isn't
    if left.is_entire_range and not right.is_entire_range:
        return Result(left.left_size + right.left_size, right.right_size, left.left_size + right.left_size, False)
    elif right.is_entire_range and not left.is_entire_range:
        return Result(left.left_size, right.left_size + left.right_size, right.left_size + left.right_size, False)

    # Case 3: rightSide of LeftRes + leftSide of RightRes
    if left.right_size > 0 and right.left_size > 0 and left.right_size + right.left_size > max(left.longest_size,right.longest_size):
        return Result(left.left_size, right.right_size, left.right_size + right.left_size, False)

    # Case 4: combining but middle is longestRun
    # left side size and right side size < longest run of left side or right side. right >=< left
    if ((left.left_size <= right.longest_size or left.left_size <= left.longest_size)
        and (right.left_size <= right.longest_size or right.left_size <= left.longest_size) and right.longest_size >= left.longest_size):
        return Result(left.left_size, right.right_size, right.longest_size, False)
    elif((left.left_size <= right.longest_size or left.left_size <= left.longest_size)
        and (right.left_size <= right.longest_size or right.left_size <= left.longest_size) and right.longest_size < left.longest_size):
        return Result(left.left_size, right.right_size, left.longest_size, False)


    """
    This is a hard corner case that requires left_size and
    right_size to be calculated correctly when only one half 
    has is_entire_range==True.

    [6 12] [12 12] [12 6] [6 6]
    """



# Feel free to add your own tests here.
def test_longest_run():
   #print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))
   assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12) == 3


