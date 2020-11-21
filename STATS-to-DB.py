import os
import csv
import glob
import mysql.connector
import pandas as pd
import time

x = 0
print("************************|Stats-to-DB: Started|*********************************")

while True:
    if x == 0:
        os.chdir("C:/Users/USERNAME/Saved Games/DCS.openbeta_server/Logs")

        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

        # combine all files in the list and encode in utf-8-sig
        combined_csv = pd.concat([pd.read_csv(f, encoding='utf-8-sig') for f in all_filenames ])
        # export to csv
        combined_csv.to_csv("C:/Users/USERNAME/Desktop/Scores/combined_csv.csv", index=False, encoding='utf-8-sig')

        # Make connection to DB with below...
        db = mysql.connector.connect(
            host="IP/HOSTNAME",
            user="USERNAME",
            passwd="PASSWORD",
            db="DB NAME"
        )

        # Declare cursor
        cursor = db.cursor()

        # Drop Table **(Comment out on the first run of this file!! As there is no Table to drop...)**
        cursor.execute('DROP TABLE TABLENAME')
        
        # Create Table
        cursor.execute('CREATE TABLE TABLENAME (GameName varchar(50), RunTime varchar(50), Time time, PlayerName varchar(64), TargetPlayerName varchar(64), ScoreType varchar(50), PlayerUnitCoaltion varchar(50), PlayerUnitCategory varchar(50), PlayerUnitType varchar(50), PlayerUnitName varchar(50), TargetUnitCoalition varchar(50), TargetUnitCategory varchar(50), TargetUnitType varchar(50), TargetUnitName varchar(50), Times int, Score int)')

        os.chdir("C:/Users/USERNAME/Desktop/Scores/")

        with open('./combined_csv.csv') as csvfile:
            csv_data = csv.reader(csvfile)  # No NameError
            firstline = True
            for row in csv_data:

                if firstline:  # skip first line
                    firstline = False
                    continue

                cursor.execute("REPLACE INTO TABLENAME(GameName, RunTime, Time, PlayerName, TargetPlayerName, ScoreType, PlayerUnitCoaltion, PlayerUnitCategory, PlayerUnitType, PlayerUnitName, TargetUnitCoalition, TargetUnitCategory, TargetUnitType, TargetUnitName, Times, Score) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               row)

        db.commit()
        cursor.close()

        from datetime import date
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        x = 1

        print("*******************************************************************************")
        print("Done! Database connection, TABLE DROP, CREATION, and import of data complete!!!")
        print("Finished update! @ ", current_time, " on ", today)
        print("*******************************************************************************")
    if x == 1:
        time.sleep(900) # 15m refresh timer for sending stats to db and compiling scores
        x = 0
