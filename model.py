# -*- coding: utf-8 -*-
"""
@author: 201376598
"""
#Introduce modules
import agentframework as afm
import matplotlib.pyplot as plt

num_of_agents = 25
drunks_num = []
house_num = []

#Add the density map
density_map = []

for i in range(300):
    blank_list=[]
    for j in range(300):
        blank_list.append(0)
    density_map.append(blank_list)
        

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
           environment[a][b]=98

#Determining the starting point of the drunks / labeling the house
for i in range(num_of_agents): 
    houseno = (i + 1) * 10
    house_num.append(houseno)
    

for j in range(num_of_agents):
    drunks_num.append(afm.Agent(environment))
    
    
#Keep moving drunks (25 starting points) until they reach the house area
for n in range(num_of_agents):
    while environment[drunks_num[n].x][drunks_num[n].y] != house_num[n]:
        drunks_num[n].move()
        drunks_num[n].eat(density_map)
    print("I am the No.", n+1, "arriving", "at", "House", int(house_num[n]/10) )

#Generate house-arriving map and density map
fig=plt.figure()
ax=fig.add_subplot(111)
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.title("Drunks arrival map")
patches = [ plt.plot([], marker="o", ms=10, ls="", mec=None, color="r", 
            label="Drunks (solid circles filled with various colours)" )[0] ]
plt.legend(handles=patches, loc='lower left', ncol=2, facecolor="plum", numpoints=1
           ,bbox_to_anchor=[-0.19, -0.19]) #Make the legend
for k in range(num_of_agents):
    plt.scatter(drunks_num[k].y, drunks_num[k].x)    
plt.imshow(environment, cmap = plt.cm.hot, vmin=0.1, vmax=2.5) 
plt.show() 

fig=plt.figure()
ax=fig.add_subplot(111)
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.title("Route density map")
patches = [ plt.plot([], ms=10, ls="", mec=None, color="w", 
            label="Brighter the colour is, higher the density is." )[0] ]
plt.legend(handles=patches, loc='lower left', ncol=2, facecolor="plum", numpoints=1
           ,bbox_to_anchor=[-0.19, -0.19])
plt.imshow(density_map) 
plt.show() 






        
        
    
    
    
    


    
        



            
            
            


