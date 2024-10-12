# Paltech Assignment

I created a ROS2 working space and moved all the files to the source to be able to test my implimentation. Please find the code under /src directory.

## Part 1: Basic waypoint manager in ROS2

I didn't find any file or topic that provides information about the yaw angle of the robot so I assumed it will face the first waypoint and calculated the angle in that case just for the samke of this demonstrartion. 

## Part 2: Path Planning 

This task consists of designing a path planning algorithm for the robot to efficiently follow waypoints:  

- Generate M random GPS points (e.g. 500) distributed in an area of 1000 m². These points represent weed positions.
- Add a cluster of approximately 2-10 plants around 50% of the M points to simulate weed clusters. This can be achieved using a normal distribution with a standard deviation of 3 meters.
- Randomly assign a starting position to the robot and perform path planning for it with the following constraints:
    - The robot is non-holonomic and follows a Dubins motion model with a minimum turning radius of 2 meters.
    - It is not necessary for the robot to reach every generated point. Points that are unreachable due to the robot's turning radius constraints can be omitted from the plan.
- Plot the calculated path. You may simplify the path using straight lines.
- Output the time and path length of the calculated path (you can assume a constant velocity of 1m/s)

**BONUS:**  

- How does the path planning change if we allow the robot to move in reverse? (REEDS_SHEPP motion model instead of DUBINS) Explain.
- What would happen if the working area of the robot is taken into account? E.G. the robot can remove weeds that are in a radius of 0,5m around its center. Explain.

## Submit your answers

To submit your completed assignment, **please fork this repository**, complete the tasks within a week (7 days), and then push your changes to your forked repository. Once done, send us the link to your forked repository to felix.schiegg@paltech.eu with the subject line "Assignment Submission - [Your Name]". Ensure your repository is public so we can review your work.










