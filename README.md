## Battery Monitor for Linux and Windows

### Problem Statement
One issue which people close to me were complaining about was the ability to have a notifier program which
would be able to notify the user based on the desired battery percentage. Meaning, that when the battery
percentage of the laptop goes below a certain point, the program would notify the user whether to charge
or keep using the same.

### The solution
In order to write the Proof Of Concept program, the choice of language was Python. Initial attempts were made
with C and C++, however the requirement of extensive libraries and the amount of time at hand forced me to
use Python.

### Problems faced and the respective solutions
1. Show notifications in Windows 10+ OS(s)
