import numpy as np
import matplotlib.pyplot as plt
import dubins
import networkx as nx 


# Using 2D cartesian coordinates to represent the area 
def generate_weed_positions(M, area_size=1000, cluster_fraction=0.5, cluster_std=3):

    # Generate random weed positions within the defined area
    positions = np.random.uniform(low=0, high=np.sqrt(area_size), size=(M, 2))
    
    # Determine the number of clusters
    num_clusters = int(M * cluster_fraction)
    
    # Create clusters by generating 2-10 plants around each weed position using a normal distribution
    weeds_in_clusters = []
    centers = positions[:num_clusters]
    for point in range(num_clusters):
        center = positions[point]

        num_cluster_points = np.random.randint(2, 11)
        
        while True:  
            cluster_points = center + np.random.normal(scale=cluster_std, size=(num_cluster_points, 2))
            
            # Filter out points that are outside the area
            cluster_points = cluster_points[
                (cluster_points[:, 0] >= 0) & (cluster_points[:, 0] <= np.sqrt(area_size)) &
                (cluster_points[:, 1] >= 0) & (cluster_points[:, 1] <= np.sqrt(area_size))
            ]
            if len(cluster_points) >= 2:
                break  
        
        weeds_in_clusters.extend(cluster_points)
    single_weeds = positions[num_clusters:]
    
    return np.array(centers) ,single_weeds, np.array(weeds_in_clusters)


def plot_weeds_and_path(centers , single_weeds , weeds_in_clusters , path):
    # Plotting the weed positions
    plt.figure(figsize=(8, 8))
    plt.scatter(single_weeds[:, 0], single_weeds[:, 1], c='green', marker='o', label='single Weed')
    plt.scatter(weeds_in_clusters[:, 0], weeds_in_clusters[:, 1], c='blue', marker='x', label='Weeds in Cluster')
    plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='o', label='centers')
    
    path = np.array(path)
    # plot path start 
    plt.plot(path[0, 0], path[0, 1], c='black', marker='o', label='Start')
    #plot the path in yellow
    plt.plot(path[:, 0], path[:, 1], c='yellow', linewidth=1, alpha=0.9, label='Path')
    
    plt.title('Randomly Generated Weed Positions with Clusters')
    plt.xlabel('X (meters)')
    plt.ylabel('Y (meters)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
# Greedy algorithm to find the nearest neighbor
def find_nearest_neighbor(current_position, waypoints):
    min_distance = float('inf')
    nearest_waypoint = None
    nearest_index = -1
    for i, waypoint in enumerate(waypoints):
        distance = np.linalg.norm(np.array(current_position) - np.array(waypoint))
        if distance < min_distance:
            min_distance = distance
            nearest_waypoint = waypoint
            nearest_index = i
    return nearest_waypoint, nearest_index
    
def dubins_path_planning(start, goal, turning_radius):
    
    path = dubins.shortest_path(start, goal, turning_radius)
    configurations, _ = path.sample_many(0.1)  # Sample points along the path
    return configurations    

# using configurations of dubins to iteratevily plan the path between current position and the nearest waypoint  
def plan_path(start, waypoints, turning_radius):

    path = []
    current_position = start  
    remaining_waypoints = waypoints.copy()
    
    while remaining_waypoints.any():
        nearest_waypoint, nearest_index = find_nearest_neighbor(current_position, remaining_waypoints)
        
        # Set yaw to 0 for both current_position and nearest_waypoint Since we're working with a point robot
        current_position_with_yaw = (current_position[0], current_position[1], 0)
        nearest_waypoint_with_yaw = (nearest_waypoint[0], nearest_waypoint[1], 0)
        
        segment = dubins_path_planning(current_position_with_yaw, nearest_waypoint_with_yaw, turning_radius)
        path.extend(segment)
        current_position = nearest_waypoint
        # remove the reached point from the list of waypoints 
        remaining_waypoints = np.delete(remaining_waypoints, nearest_index, axis=0)
    
    return path

# Dummy path planning function that connects the waypoints in the order they were generated: to see how good the greedy algorithm is. 
def plan_path_dummy(start, waypoints, turning_radius):
    path = []
    current_position = start
    
    for waypoint in waypoints:
        # Set yaw to 0 for both current_position and waypoint
        current_position_with_yaw = (current_position[0], current_position[1], 0)
        waypoint_with_yaw = (waypoint[0], waypoint[1], 0)
        
        segment = dubins_path_planning(current_position_with_yaw, waypoint_with_yaw, turning_radius)
        path.extend(segment)
        current_position = waypoint
    
    return path


def main():
    M = 20
    centers , single_weeds , weeds_in_clusters = generate_weed_positions(M)
    all_weeds = np.concatenate((centers, single_weeds, weeds_in_clusters))
    
    start = np.random.uniform(low=0, high=np.sqrt(1000), size=2)     
    turning_radius = 2
    # Plan the path through the weed cluster points
    path = plan_path(start, all_weeds, turning_radius)
    dummy_path = plan_path_dummy(start, all_weeds, turning_radius)
    
     # Calculate the total path length
    path_length = sum(np.linalg.norm(np.array(path[i][:2]) - np.array(path[i-1][:2])) for i in range(1, len(path)))
    dummy_path_length = sum(np.linalg.norm(np.array(dummy_path[i][:2]) - np.array(dummy_path[i-1][:2])) for i in range(1, len(dummy_path)))
    # Calculate the time taken
    time_taken = path_length / 1  # velocity = 1 m/s   
    
    print(f'Path length: {path_length:.2f} meters')
    print(f'Time taken: {time_taken:.2f} seconds')
    print(f'Dummy path length: {dummy_path_length:.2f} meters')
    print(f'Dummy time taken: {dummy_path_length / 1:.2f} seconds')

    
    
    # plot_path(path)  
    plot_weeds_and_path(centers , single_weeds , weeds_in_clusters, path)


if __name__ == "__main__":  
    main()