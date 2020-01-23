# -*- coding: utf-8 -*-
"""
@author: 201376598
"""
#Introduce modules
import agentframework as afm
import matplotlib.pyplot as plt

num_of_agents = 25
drunks = []
house_labels = []

#Add the density map
density = []

for i in range(300):
    rowlist=[]
    for j in range(300):
        rowlist.append(0)
    density.append(rowlist)
        

#Introduce environment raster
f = open("drunkenv.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()


#Mark pub location
for a in range(300):
    for b in range(300):
        if environment[a][b]==1:
           environment[a][b]=99

#Determining the starting point of the drunks / labeling the house
for j in range(num_of_agents): 
    houseno = (j + 1) * 10
    house_labels.append(houseno)
    

for i in range(num_of_agents):
    drunks.append(afm.Agent(environment))
    
    
#Keep moving drunks (25 starting points) until they reach the house area
for k in range(num_of_agents):
    while environment[drunks[k].x][drunks[k].y] != house_labels[k]:
        drunks[k].move()
        drunks[k].eat(density)
    print("I am the No.", k+1, "to arrive", "at", "House", int(house_labels[k]/10) )

#Generate house-arriving map and density map
fig=plt.figure()
ax=fig.add_subplot(111)
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.title("Drunks route map")
patches = [ plt.plot([],[], marker="o", ms=10, ls="", mec=None, color="r", 
            label="Drunks (solid circles filled with various colours)" )[0] ]
plt.legend(handles=patches, loc='lower left', ncol=2, facecolor="plum", numpoints=1
           ,bbox_to_anchor=[-0.19, -0.19]) #Make the legend
for m in range(num_of_agents):
    plt.scatter(drunks[m].y, drunks[m].x)    
plt.imshow(environment, cmap = plt.cm.hot, vmin=0.1, vmax=2.5) 
plt.show() 

fig=plt.figure()
ax=fig.add_subplot(111)
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.title("Walking density map")
plt.imshow(density) 
plt.show() #Brighter the color is, more times drunks walk on, higher the density is.






        
        
    
    
    
    


    
        



            
            
            


