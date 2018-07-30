def get_non_incr_subranges(start, stop, input, output = []):
    """
    Find non-increasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    output = list(output)
    # If this is the first window or the previous window had no
    # non-increasing subrange then do a fresh search for
    # non-increasing subranges 
    if output == []:
        first = last = start
        for index in xrange(start, stop):
            if input[index] <= input[first]:
                last = index
            elif last != first:
                output.append([first, last])
                first = last = index
            else:
                first = last = index
        if last != first:
            output.append([first, last])
        return list(output)
    
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

        return list(output)

def get_non_decr_subranges(start, stop, input, output = []):
    """
    Find non-decreasing subrange groups in a window.
    Return list of list where each sub list is [start, end] of a
    subrange group.
    """

    output = list(output)
    # If this is the first window or the previous window had no
    # non-decreasing subrange then do a fresh search for
    # non-decreasing subranges 
    if output == []:
        first = last = start
        for index in xrange(start, stop):
            if input[index] >= input[first]:
                last = index
            elif last != first:
                output.append([first, last])
                first = last = index
            else:
                first = last = index
        if last != first:
            output.append([first, last])
        return list(output)
    
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

        return list(output)