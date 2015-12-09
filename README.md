# CS_558_Assignment_2
Assignment #2 Using Python
Haval Ahmed and Ryan Stevens
815013661,      810318529
CS 558 Fall 2015

Assignment 2: Aquarium simulation ( aka prey and predator simulation):

In this simulation we look at the relationship between prey's and predators.
We use ODE's to solve first order equations.


File manifest (name of all files included in this project)
ReadMe
  Documentation
SCIPY_Implementation
  The source code for the program

Compile instructions
The user needs python 2.7 and scipy and numpy. No compiling is needed.

Operating instructions 
The user needs t run the program and input the values they want.

List/description of novel/significant design decisions
The code is laid out in the same way that it would run. The initiualization is in the top, the program is in the middle, and the calculations and output is in the bottom.
We also do not stop the simulation when a prey or predator go below 1.
After much debate and research we noticed that when using a ODE it is bad to have stopping conditions. 
We also decided that instead of having a number for fish eaten it is more important to look at how many fish were eaten vs born.
This also came about since we decided that it is wrong to create fish objects since in class it has been said numerous times
that the program should be easy and creating objects would be more object orientated versus scripting. 

List/description of any extra features/algorithms/functionality 
We output a graph and we output extra data that the user might not need. 
Also the user can change the variables so they can run different tests.

List/description of any known deficiencies or bugs
no known bugs are found at this time.

Lessons Learned 
Since we have no numpy and sciy experience that was a steep learning curve. With little python experience we also learned more python skills. Things like list manipulation is very easy to do in python. 
