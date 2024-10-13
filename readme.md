# Paltech Assignment

I created a ROS2 working space and moved all the files to the source to be able to test my implementation. Please find the code under /src directory.

## Part 1: Basic waypoint manager in ROS2

I didn't find any file or topic that provides information about the origin yaw angle of the robot (which should be provided to the waypoint message) so I assumed it will face the first waypoint and calculated the angle in that case just for the sake of this demonstration. 

## Part 2: Path Planning 
- Generate M random GPS points (e.g. 500) distributed in an area of 1000 m². These points represent weed positions: 
since the area is small and no point of origin was provided, I assumed that the area is flat and used coordinates in a cartisian System 
- Add a cluster of approximately 2-10 plants around 50% of the M points to simulate weed clusters. This can be achieved using a normal distribution with a standard deviation of 3 meters: 
I plotted the centers of clusters in red and single weeds seperately in green  

- Randomly assign a starting position to the robot and perform path planning for it with the following constraints:
I passed the orientation when using dubins as 0 because we're dealing with a point.

- Plot the calculated path. You may simplify the path using straight lines: the path can be seen in yellow.

- Output the time and path length of the calculated path (you can assume a constant velocity of 1m/s) : I compared the greedy algorithme I used to a primitive approach to show the difference in time and distance.

**BONUS:**  

- How does the path planning change if we allow the robot to move in reverse? (REEDS_SHEPP motion model instead of DUBINS) Explain.
[Answer] : 
the Path planning would be more efficient when using REEDS_SHEPP: allowing reverse motion adds maneuverability that allows the robot to take shorter paths rather than having to take unnecessary large turns.

- What would happen if the working area of the robot is taken into account? E.G. the robot can remove weeds that are in a radius of 0,5m around its center. Explain.
[Answer] : 
Primarly this would mean that the robot wouldn't have to reach the exact positions of weeds when planning the path but rather follow a path that brings it within a 0.5m radius from the weeds. Which basically means that the robot could find a smoother and shorter path with much more effitiency. To achieve this, the weeds could be clustered using algorithms like K-MEANS with a radius of 0.5 and then planning a path between the centroids of those clusters using any algorithm solving the Traveling Salesman Problem (TSP). 











