def merge_patterns(pattern_abcd):
 
    patterns = {}

    abcd = pattern_abcd

    # Create dict
    for each in abcd:
        b_date = each.pattern_B_pivot_date
        c_date = each.pattern_C_pivot_date
        dates = str(b_date) + '-' + str(c_date)
        if dates not in patterns:
            patterns[dates] = []
    
    # Assign each pattern object to correct list
    for each in abcd:
        b_date = each.pattern_B_pivot_date
        c_date = each.pattern_C_pivot_date
        dates = str(b_date) + '-' + str(c_date)
        for key, value in patterns.items():
            if dates == key:
                patterns[key].append(each)

    # Create new list.
    new_patterns = {}
    for key, value in patterns.items():
        new_patterns[key] = []

    for key,value in patterns.items():

        # Find the highest A price of the current list
        
        d_dropped_below_b_dates = []
        a_high = 0
        for each in value:
            a = each.pattern_A_open if each.pattern_A_open > each.pattern_A_close else each.pattern_A_close
            if a > a_high:
                a_high = a 
            d_dropped_below_b_dates.append(each.d_dropped_below_b)
        

        # Collect all patterns where A matches a_high
        for each in value:
            a = each.pattern_A_open if each.pattern_A_open > each.pattern_A_close else each.pattern_A_close
            if a == a_high:
                new_patterns[key].append(each)

            
            


    

        

    merged_patterns = []
    # Grab the smallest D
    for key, value in new_patterns.items():

        max_object = max(value, key=lambda obj: obj.pattern_ABCD_end_date)

        earliest_date = min(value, key=lambda obj: obj.d_dropped_below_b).d_dropped_below_b

        max_object.d_dropped_below_b = earliest_date
        
        merged_patterns.append(max_object)

        d_dates = []
        for each in value:
            d_dates.append(each.trade_entered_date)
            
        for each in value:
            each.pattern_d_created_date = min(d_dates)

    return merged_patterns
