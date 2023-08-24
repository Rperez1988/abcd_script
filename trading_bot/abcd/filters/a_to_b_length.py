def getAtoBLength(length_limit, pivot_a, pivot_length):

    if pivot_a.duration['barsSincePreviousPivot'] <= int((length_limit)):

        return True


def filter_getAtoBLength(length_limit, pivot_a, pivot_length):

    if length_limit == "Off":
        return True
    
    elif length_limit.isdigit():

        is_length_under_set_limit = getAtoBLength(length_limit, pivot_a, pivot_length)
        if is_length_under_set_limit:
            return True
        else:
            return False
