def getValidColumns(data):
    # data is a list of objects
    print(data)
    if len(data)==0:
        return

    i = 0
    valid_cols_set = set()
    
    while(i < min(5, len(data))): # want to check at least 5 rows to account for null values
        row = data[i]
        for key, val in row.items():
            if val != None:
                if (isinstance(val, int) or isinstance(val, bool)) and (key not in valid_cols_set):
                    valid_cols_set.add(key)
        i += 1

    
    
    return(list(valid_cols_set))
        