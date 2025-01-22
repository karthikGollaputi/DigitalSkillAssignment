Description:
 Framework checks the input vehicles  with motorway website and then validates 
 with Output file data
 Input File contains Some Unstructured data with the Registration Numbers. 
 project extracts the Registration Numbers and Validate these vehicles in Motorway
 Website using url "https://motorway.com"

After  getting the details of the Vehicle and Validate this 
Vehicle Details With the Output File.

Assuming the Registration Numbers in the Format of ("AA53 ABC")

Tools ::-
=========
To develop this Project We used the below tools.
  1) Pytest for Unit Testing Framework
  2)Python Language for developing the code.

POM(Page Object Model)  design pattern used for developing the framework to maintain
the code efficiently and to increase the reusability of the code

Folders :-
========
The below folders and files has been Created for the Project to organize the code 
efficiently.

1) Conftest.Py : File Contains all the reusable Methods accross the tests.
2) Utils Folder : Contains all the Utility classes.
   DriverManager Utility Class ::-
     Here used the Factory Method Pattern(Creational Design Pattern) used to 
     get the Driver Object dynamically based on the user input
   File Utils class:-
     Contains all the Methods related to File handling
3) tests Folder : contains the Actual tests
4) PageLocators : contains all the Page Element Locators
5) PageObjects Folder : contains all the Page Objects

Execution:-
==========
 pytest --browser="chrome"

 the browser  specifed as part of the command, the tests get executed in that
browser

// As the output texts doesn't have the Proper 
 
