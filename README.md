# Tournament Results
Udacity Full Stack developer project

## Project Specification

Develop a database schema to store details of a games matches between players.   
Then write a Python module to rank the players and pair them up in matches in a tournament.

## Files 

**tournament.py**  Contains the implementation for the Swiss tournament  

**tournament.sql**  Contains the SQL queries to create the database, tables and views   

**tournament_test.py**  Contains the test cases for tournament.py  

## Prerequisites 

The latest vagrant build for the Udacity tournament project. (In project notes)

## Instructions

1. Start Vagrant
  1. Open Terminal or cmd and browse to the vagrant folder
  2. Type `vagrant up`
2. SSH in to the vagrant VM
  1. In the same terminal type `vagrant ssh`
3. Change to the correct folder
  1. Type `cd /vagrant/tournament`
4. Open PSQL and run the tournament.sql 
  1. type `psql`
  2. copy the contents of tournament.sql and paste in to the terminal window
  3. type `\q` to quit out of PSQL 
5. Run the tests
  1. In the terminal type `python tournament_test.py`

## Expected Outcome
.....
.....
.....
Success!  All tests pass!  
