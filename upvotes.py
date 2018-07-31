'''
Calculates (non-decreasing subranges) - (non-increasing subranges)
of a given window within a list of Quora upvotes per day 
'''

def get_non_incr_subranges(start, stop, input, output = [],
    sum = None):
    """
    Find non-increasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    # If this is the first window (where sum = None and output = [])
    # do a fresh search for non-increasing subranges 
    if output == [] and sum == None:
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
        return output, sum_subranges(output)
    
    # If dealing with subsequent windows, use the previous sum and
    # subranges to calculate the new sum and subranges
    else:
        # If previous window was empty then check only the end
        # boundary for new ranges since all elements before that are
        # still the same elements that were in the previous window
        if output == []:
            if input[stop - 1] <= input[stop - 2]:
                output.append([stop - 2, stop - 1])
                sum = 1
                return output, sum
            else:
                return output, sum

        # If the begining of the subranges of the previous window
        # overlaps with with the boundary of the present window then
        # shift it so it begins from the start of present window.
        if output[0][0] < start:
            sum -= (output[0][1] - output[0][0])
            output[0][0] = start

        # Check if last two elements of present window are a 
        # non-increasing subrange. If it is merge it with the last
        # subrange of the previous window if they are a continuos
        # non-increasing subrange.
        if input[stop - 1] <= input[stop - 2]:
            if output[-1][1] == stop - 2:
                output[-1][1] = stop - 1
                diff = output[-1][1] - output[-1][0]
                sum += diff
            else:
                output.append([stop - 2, stop - 1])
                sum += 1

        # If shifting the first subrange of the previous window makes
        # makes it have just one element then delete the subrange
        if output[0][1] - output[0][0] <= 0:
            output.pop(0)

        return output, sum

def get_non_decr_subranges(start, stop, input, output = [],
    sum = None):
    """
    Find non-decreasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    # If this is the first window then do a fresh search for
    # non-decreasing subranges 
    if output == [] and sum == None:
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

        return output, sum_subranges(output)

    # If this is a subsequent window then derive the subranges and
    # sum for this window using those of the previous window
    else:
        # If previous window was empty then check only the end
        # boundary for new ranges since all elements before
        # that are still the same elements that were in the
        # previous window
        if output == []:
            if input[stop - 1] >= input[stop - 2]:
                output.append([stop - 2, stop - 1])
                sum = 1
                return output, sum
            else:
                return output, sum

        # If the begining of the subranges of the previous window 
        # overlaps with with the boundary of the present window then 
        # shift it so it begins from the start of present window.
        if output[0][0] < start:
            sum -= (output[0][1] - output[0][0])
            output[0][0] = start

        # Check if last two elements of present window are a 
        # non-decreasing subrange. If it is merge it with the last
        # subrange of the previous window if they are a continuos
        # non-decreasing subrange.
        if input[stop - 1] >= input[stop - 2]:
            if output[-1][1] == stop - 2:
                output[-1][1] = stop - 1
                diff = output[-1][1] - output[-1][0]
                sum += diff
            else:
                output.append([stop - 2, stop - 1])
                sum += 1

        # If shifting the first subrange of the previous window makes
        # makes it have just one element then delete the subrange
        if output[0][1] - output[0][0] <= 0:
            output.pop(0)

        return output, sum

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

    start = 0
    stop = start + K

    # nds = non-decreasing subranges of a given window
    nds, sum_nds = get_non_decr_subranges(start, stop, UPVOTES, nds)
        
    # nis = non-increasing subranges of a given window
    nis, sum_nis = get_non_incr_subranges(start, stop, UPVOTES, nis)

    print sum_nds - sum_nis

    for start in xrange(1, ((N - K) + 1)):
        stop = start + K

        # nds = non-decreasing subranges of a given window
        nds, sum_nds = get_non_decr_subranges(start, stop, UPVOTES,
            nds, sum_nds)
        
        # nis = non-increasing subranges of a given window
        nis, sum_nis = get_non_incr_subranges(start, stop, UPVOTES,
            nis, sum_nis)

        print sum_nds - sum_nis