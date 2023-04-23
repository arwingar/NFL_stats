# NFL_stats

Make sure to download all files in this repository to run this application. 

graphics.py MUST be in the same location as connection.py, otherwise it will not run.

Install applications Python and Visual Studio Code, if not already on your device.

Before running, follow these steps: 
  (1) Import the CSV files to your MySQL Workbench in a schema called 'nfl_stats'
  (2) Check if you have Python installed on your device 
        run this command in command prompt: python -V 
        if you see message 'Python3.9.x' or something similar, proceed to the next step
        if you receive an error message, this means you do not have Python installed
        install Python, then start with step 1 again.
  (3) Install Python extensions in Visual Studio Code 
        Click the “Extensions” icon and install:
          Python (Microsoft)
          Pylance (Microsoft, Language Support)
  (4) Create/navigate to the directory in which to store the files you downloaded
        if not already created, run this command in command prompt: mkdir dbconnect
        add file 'connection.py' to the newly created dbconnect folder along with 'graphics.py'
        start Visual Studio Code and open a folder 
          File -> Open folder
          choose the folder you just created
          click 'Open File' and open file 'connection.py'
  (5) Create a virtual environment
        open terminal menu with View -> Terminal
        run this command: python -m venv .venv
        activate environment with this command: venv\Scripts\activate
        you should now see this in front of your file path in the terminal: (.venv)
  (6) Select Python interpreter
        open the command pallet  in Visual Studio (ctrl-shift-p)
        type “python select interpreter” and select it
        choose “enter interpreter path” and “find”
        choose python
  (7) Set connector parameters
        in the 'connection.py' file you will see the following code at the top:
            conn = mysql.connector.connect(
              host="localhost",
              database="nfl_stats",
              user="root",
              password="Buddies3$" )
         fill in your own database information for host, user, and password (you should have created a database using the downloaded files)
   (8) Run the Python file and enjoy the application!
