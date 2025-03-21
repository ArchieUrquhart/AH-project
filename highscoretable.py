import mysql.connector

# connect to database - FR 1.1
try:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        database="archie_u ah project",
        user="root",
        password=""
    )

except mysql.connector.Error as err:
    # show error message
    print("Error with connection: {}".format(err))

else:
    # run insert
    def add_game(game_username, game_score):
        cursor = cnx.cursor()
        # query to insert the username and score of the player who just played - FR 2.3
        query = ("INSERT INTO gamedetails_testing(username, score) VALUES ('{}',{})".format(game_username, game_score))
        cursor.execute(query)
        cnx.commit()


    # get highscore data from database - FR 1.2/ 1.3
    def get_table():
        cursor = cnx.cursor()
        # query to get the required data for the highscore table - FR 1.2
        query = (
            "SELECT username, MAX(score) as 'highscore', count(*) as 'games_played' FROM gamedetails_testing GROUP BY username")
        cursor.execute(query)
        table_entries = cursor.fetchall()

        # FR 1.3
        # init highscore table
        HighScores = [["", 0, 0] for i in range(cursor.rowcount)]
        # read select into 2d array
        row = 0
        for data in table_entries:
            HighScores[row][0] = data[0]
            HighScores[row][1] = data[1]
            HighScores[row][2] = data[2]
            row += 1

        # return the sorted table
        sort_table(HighScores)
        return HighScores


    # sort 2d array - FR 1.4
    def sort_table(table):

        # interate through each row in the array
        for i in range(1, len(table)):
            # pick the next element in the array
            temp = table[i]
            pos = i
            # move backwards through the array until the correct position is found by comparing highscores
            while pos > 0 and table[pos - 1][1] < temp[1]:
                # move rows to make space for current row
                table[pos] = table[pos - 1]
                pos -= 1

            # insert row into correct position
            table[pos] = temp
