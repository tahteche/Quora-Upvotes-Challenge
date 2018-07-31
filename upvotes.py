'''
Calculates (non-decreasing subranges) - (non-increasing subranges)
of a given window within a list of Quora upvotes per day 
'''

def get_non_incr_subranges(start, stop, input, output = []):
    """
    Find non-increasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    # If this is the first window or the previous window had no
    # non-increasing subrange then do a fresh search for
    # non-increasing subranges 
    if output == []:
        first = last = start
        for index in xrange(start, stop):
            if input[index] <= input[last]:
                last = index
            elif last != first:
                output.append([first, last])
                first = last = index
            else:
                first = last = index
        if last != first:
            output.append([first, last])
        return output
    
    # If the previous window had non-increasing subranges use them to
    # derive the subranges for the present window
    else:
        # If the begining of the subranges of the previous window
        # overlaps with with the boundary of the present window then
        # shift it so it begins from the start of present window.
        if output[0][0] < start:
            output[0] = [start, output[0][1]]

        # Check if last two elements of present window are a 
        # non-increasing subrange. If it is merge it with the last
        # subrange of the previous window if they are a continuos
        # non-increasing subrange.
        if input[stop - 1] <= input[stop - 2]:
            if output[-1][1] == stop - 2:
                output[-1] = [output[-1][0], stop - 1]
            else:
                output.append([stop - 2, stop - 1])

        # If shifting the first subrange of the previous window makes
        # makes it have just one element then delete the subrange
        if output[0][1] - output[0][0] <= 0:
            output.pop(0)

        return output

def get_non_decr_subranges(start, stop, input, output = []):
    """
    Find non-decreasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    # If this is the first window or the previous window had no
    # non-decreasing subrange then do a fresh search for
    # non-decreasing subranges 
    if output == []:
        first = last = start
        for index in xrange(start, stop):
            if input[index] >= input[last]:
                last = index
            elif last != first:
                output.append([first, last])
                first = last = index
            else:
                first = last = index
        if last != first:
            output.append([first, last])
        return output
    
    # If the previous window had non-decreasing subranges use them to
    # derive the subranges for the present window
    else:
        # If the begining of the subranges of the previous window 
        # overlaps with with the boundary of the present window then 
        # shift it so it begins from the start of present window.
        if output[0][0] < start:
            output[0] = [start, output[0][1]]

        # Check if last two elements of present window are a 
        # non-decreasing subrange. If it is merge it with the last
        # subrange of the previous window if they are a continuos
        # non-decreasing subrange.
        if input[stop - 1] >= input[stop - 2]:
            if output[-1][1] == stop - 2:
                output[-1] = [output[-1][0], stop - 1]
            else:
                output.append([stop - 2, stop - 1])

        # If shifting the first subrange of the previous window makes
        # makes it have just one element then delete the subrange
        if output[0][1] - output[0][0] <= 0:
            output.pop(0)

        return output

def sum_subranges(subranges, sum = 0):
    '''
    Calculates the number of subranges from a list containing
    subrange groups.
    '''
    for subrange in subranges:
        if len(subrange) == 0:
            continue
        diff = subrange[1] - subrange[0]
        sum += (diff * (diff + 1)) / 2
    return sum

if __name__ == "__main__":
    N, K = raw_input().split()
    N = int(N)
    K = int(K)
    UPVOTES = raw_input().split()
    UPVOTES = [int(upvote) for upvote in UPVOTES]

    # nds = non-decreasing subranges of a given window
    nds = []

    # nis = non-increasing subranges of a given window
    nis = []

    for start in xrange(0, ((N - K) + 1)):
        stop = start + K

        # nds = non-decreasing subranges of a given window
        nds = get_non_decr_subranges(start, stop, UPVOTES, nds)
        
        # nis = non-increasing subranges of a given window
        nis = get_non_incr_subranges(start, stop, UPVOTES, nis)

        sum_nds = sum_subranges(nds)
        sum_nis = sum_subranges(nis)

        print sum_nds - sum_nis