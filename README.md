# dcs-moose-custom-scoring
Utilize MOOSE to create and save custom scoring files for DCS (Digital Combat Simulator) to input in a database and host on a web server if desired
--
[AS USED BY 'The Dragon Squadron' on https://thedragonsquadron.com]

-- See link for more MOOSE Scoring details if desired (https://flightcontrol-master.github.io/MOOSE_DOCS/Documentation/Functional.Scoring.html)

A. We need to tell DCS to enable us the option to save a file, go into the following folder - DCS World\Scripts\ and change the marked lines to look as follows in the file - "MissionScripting.lua" -
--
```lua
Code:
do
	sanitizeModule('os')
	--sanitizeModule('io')
	--sanitizeModule('lfs')
	require = nil
	loadlib = nil
end
```

B. Setup and run "CustomSCORE.lua" after MOOSE has been initialized (e.g. Trigger "NO ACTION" -> After time "X seconds" -> Run LUA file "CustomSCORE.lua)
--
-- Once running, check that the scoring does in fact work, and is out putting on the name of file you specified in the CustomSCORE.lua file

C. If all is working, do the following setup for the STATS-to-DB.py file to work properly
--
  1). Create a LAMP box (https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)
      # This allows for the required MySQL database and potential web hosting w/ Appache you may need to view the scores on a web page via php
      
  2). Allow access from other devices on your network and open MySQL port locally (https://websiteforstudents.com/configure-remote-access-mysql-mariadb-databases/)
      # Use this in case you are not hosting the DCS Server on the same box as the MySQL Database
      
  3). Confirm that each box can reach the other (e.g. "Windows 10 DCS Server Box" <---> "Ubuntu MySQL/Web Server" )
      # Ping each box and ensure they are reachable from each other
      
  4). Install at least Python v3.8 on the box with the DCS Server (https://www.python.org/downloads/)
      # Python is required for the script to work!
      
  5). On the Windows box w/ DCS Server create a folder called "Scores" on the Desktop.
      # This is the default location the files will compile
      
  6). Download, Configure, and Run "STATS-to-DB.py" on the box with the DCS Server
      # Confirm you have set all required variables and do have python installed
      
  7). If setup properly, you should be pushing the accumulating score/csv. files to the combined_csv.csv file in "Scoring" on the Desktop
      # All scores will at the very least, if they are being generated, be parsed and all saved in one document as listed above
      
  8). Double check that your database is recieving the data you are pushing and or check any errors that may occur. Ensure all variables are set.
      # https://www.mysqltutorial.org/mysql-show-databases/
      
  9). Pull data from database to web page on webserver via php
      # https://www.ionos.com/community/hosting/mysql/use-php-to-retrieve-information-from-a-mysqlmariadb-database/
