#connect to database

#run insert

#run select

#read select into 2d array

#sort 2d array
def sort_table(table):
    #the column in the table to be sorted by 
    feild = 1

    #interate through each row in the array
    for i in range(1,len(table)):
        #pick the next element in the array
        temp = arr2d[i]
        pos = i
        #move backwards through the array until the correct position is found 
        while pos > 0 and get_addr(table[pos-1][feild]) > get_addr(temp[field]):
            #move rows to make space for current row
            table[pos] = table[pos-1]
            pos -= 1

        #insert row into correct position
        table[pos] = temp

    #return sorted 
    return table
