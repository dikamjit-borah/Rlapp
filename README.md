# Rlapp
A flask web app to get csv file from user and calculate shortest path using a RL algorithm

User will provide us coordinates of his wsn. Now we will first make a csv file containing the coordinates of the respective nodes using the populateCoordinates script. Next we calculate the distance between the nodes(each and every) using the calculateDistance script. We read the coordinates and distances with pandas. We make two lists x[] and y[] to store x and y coordinates of the nodes. This will be useful when plotting the points. Then we have visualize the coordinates in a graph (plotCoordinates())  with the help of matplotlib.

Activate python virtual environment with Scripts/activate

main.py is the is the homepage of our web app. It allows us to upload a csv containing nodeA-nodeB-weight. We define two input paramteters; the start node and the end node respectively and in the backend the best paths(shortest distance(weight) to reach end node from start node) is calculated and displayed. 
