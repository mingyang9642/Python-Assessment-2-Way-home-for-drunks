# Python Assessment 2 - Way home for drunks
# Introduction
Having gone through the first assessment, we learnt about basic parts of Python?variables, modules, functions, loops etc?. Thereby, the second one is surely be the advanced type. We have five tasks to choose, and I choose to carry out the Drunks way home. 

This task is like a video game. It provides an existed 300*300 raster map as the background and requires us to generate 25 drunks from a pub (which locates at the centre of map) and let them move in a drunk way until they get one of their 25 houses. Their tracks should be displayed in some sort of density map in order to have a look about how they move.

# Prerequisites
Python 3.7 environment, which can be established by installing Anaconda 3 on the computer. Link: anaconda.com/distribution

# Files/Directories
There is only one file needed to be input from outside into Python, which is the 300*300 environment raster file(.txt). In the file, the pub is denoted by 1, the houses by the numbers 10-250, and the empty spaces 0. Another two file are Python-coding files(.py), the structure is the same with the first assessment (one is model, and the other one is agentframework).

# Coding progress
The entire progress can be described in two words, difficult and fun. For a fresh programmer, it is not easy to convert a task written in words into a computer language, and eventually make the computer understand them. The reason why I chose the Drunks home project is because it has similarities with Assessment 1, which is an advanced and extended project.

First, I added environment raster, and then started thinking about what the core of this project is. I figured out the key part is to control the drunks (each point on the map) and make them move (the coordinates of the points change) to where they could stop. Thereby, once the coordinates are in the required area of ??the house, the drunks stop immediately. It should be a loop. 

After some attempts, I decided to use a While loop statement. When the values ??on the map represented by the coordinates of drunks, are not equal to the house number, they are always moving. This will ensure that drunks constantly move before they touch the edge of their house and stop once they touch. This is undoubtedly beautiful and precise coded.

After the general direction is determined, as in Assessment 1, I created an agentframework to add to the main model and set the starting point of drunks to be in the pub area. (In the code, I use For loop to find the coordinate range of the pub.) At the same time, the houses need to be labelled, and they are related to the number of drunks (10 times). According to the characteristics of Python, I wrote an assignment to establish the relationship between the two. After careful modification, most of the code is complete.

Then it is the plotting step. Before using matplot, generating a density map is needed, so I create a new list of 300 * 300 values ??that are all zero, and use the Eat idea I learned in first assessment to control the density (since the colour depth of the plot produced by matplotlib is related to the value). Finally, I managed to set up two plots. The mission is over.

# Running the programme
- How to run? Running this programme is quite simple. Just download the whole directory to local drive in the same folder, double-click the folder. Now the key is to hold onto SHIFT button, right click at blank space, and open the POWERSHELL (Win10). Type “Python model.py” into the command, the programme runs.
- What will it be like when it is running? A good display of animation running in a window shows at last. The animation is about a certain number of sheep (points) running on green grass (raster with evaluation data) and eating them (colour of the raster fades gradually).

# UML diagram

# License
This project is licensed under the MIT License, see the LICENSE.txt file for details.

