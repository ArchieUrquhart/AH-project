import mysql.connector
#connect to database
try:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        database="archie_u ah project",
        user="pupil",
        password="pupilpassword"
    )

except mysql.connector.Error as err:
    #show error message
    print("Error with connection: {}".format(err))
    
else:
    #run insert
    def addGame(game_username, game_points):
        cursor = cnx.cursor()
        query = ("INSERT INTO gamedetails_testing(username, score) VALUES (%s,%i")
        cursor.execute(query,(game_username, game_points))
        cnx.commit()
        
    #get highscore data from database
    def getTable():
        #run select
        cursor = cnx.cursor()
        query = ("SELECT username, MAX(score) as 'highscore', count(*) as 'games_played' FROM gamedetails_testing GROUP BY username")
        cursor.execute(query)
        table_entries = cursor.fethchall()

        #init highscore table
        HighScores = [[[""],[0],[0] for i in range(cursor.rowcount())] 
        #read select into 2d array
        for i, (username, highscore, games_played) in enumerate(cursor):
            HighScores[i][0] = username
            HighScores[i][1] = highscore
            HighScores[i][2] = games_played

        return HighScores
            
    
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
