# -*- coding: utf-8 -*-
"""
@author: 201376598
"""
#Introduce modules
import agentframework as afm
import matplotlib.pyplot as ppt

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
    print("I am the No.", k+1, "to arrive", "at", "House", house_labels[k] )

#Generate house-arriving map and density map
fig=ppt.figure()
ax=fig.add_subplot(111)
ppt.xlim(0, 300)
ppt.ylim(0, 300)
ppt.title("Drunks route map")
patches = [ ppt.plot([],[], marker="o", ms=10, ls="", mec=None, color="r", 
            label="Drunks (with various colours filled in)" )[0] ]
ppt.legend(handles=patches, loc='lower right', ncol=2, facecolor="plum", numpoints=1
           ,bbox_to_anchor=[1, -0.2]) #Make the legend
for m in range(num_of_agents):
    ppt.scatter(drunks[m].y, drunks[m].x)    
ppt.imshow(environment, cmap = ppt.cm.hot, vmin=0.1, vmax=2.5) 
ppt.show() 

fig=ppt.figure()
ax=fig.add_subplot(111)
ppt.xlim(0, 300)
ppt.ylim(0, 300)
ppt.title("Walking density map")
ppt.imshow(density) 
ppt.show() #Brighter the color is, more times drunks walk on, higher the density is.






        
        
    
    
    
    


    
        



            
            
            


