Pur Beurre
OpenClassroom - Python - Project 05

PURPOSE
User can interact with api thanks to this program. He can show a selection of products to find the best sort by category.

REQUIREMENTS
You will need MySQL 8 to get this script working. You will also need to create a user and give him proper rights (under MySQL 8) :

CREATE USER 'user_purbeurre'@'localhost' IDENTIFIED BY 'user_purbeurre';
GRANT ALL PRIVILEGES ON 'pur_beurre'.* TO 'user_purbeurre'@'localhost';
If following user is created with needed rights, the script will create and update the database automatically.

DETAILS
main.py: Main file for run the script.

dbinit.py : Use for drop and create automatically the database. 

api_data_manager.py: file for the API request.

bdd_data_manager.py: file for interaction between api_data_manager and Database.

navigation.py : Use for user interaction with the database.

HOW TO USE
The script will display a menu and ask you what you want to do. Following your answer it will propose you other choice(s) and so on. All of your choice must be enter according to what is writing, if not it will tell you and ask you again..

F.A.Q
The first launch can be long, depending of your network and computer, just give it some time, it will inform you of the progress. (It needs to download the products, process them and create the local database).

