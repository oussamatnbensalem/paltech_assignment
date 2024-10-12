import rclpy
from rclpy.node import Node
from custom_interfaces.srv import GetWaypoints, SetWaypoints
from custom_interfaces.msg import Waypoint
from std_srvs.srv import Trigger
import json

# [Oussama] custom imports
import math
import numpy as np
import matplotlib.pyplot as plt



class WaypointManager(Node):
    def __init__(self):
        super().__init__("waypoint_manager")
        self.get_waypoints_srv = self.create_service(
            GetWaypoints, "get_robot_waypoints", self.get_robot_waypoints_callback
        )
        self.set_waypoint_srv = self.create_service(
            SetWaypoints, "set_waypoints", self.set_waypoints_callback
        )
        self.reset_waypoint_srv = self.create_service(
            Trigger, "reset_waypoints", self.reset_waypoints_callback
        )
        self.robot_inital_geo = (47.740114, 10.322442)   # THE ROBOT INITIAL POSITION IN GEO COORDINATES !!!!

        self.waypoint_list_geo = []  # needs to be an array of Waypoint() messages
        self.waypoint_list_robot_frame = []
        self.set_waypoint_client = self.create_client(SetWaypoints, "set_waypoints")
            
        #[Oussama] I added this to calculate the yaw angle when facing the first point 
    def calculate_yaw_angle(self, waypoint):
        dx = waypoint.longitude - self.robot_inital_geo[1]
        dy = waypoint.latitude - self.robot_inital_geo[0]
        yaw_angle = math.atan2(dy, dx)
        return yaw_angle

    # [Oussama] defining 2D euler Rotation matrix around YAW axis.  
    def rotate_point(self,point, angle):
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        return np.dot(point, rotation_matrix)

    def set_waypoints_callback(self, request, response):
        response.success = False
                
        try: 
            # read the geojson file from the file path set down below.
            with open(request.file_path, 'r') as f:
                data = json.load(f)
                waypoints = []
                for feature in data['features']:
                    if feature['geometry']['type'] == 'Point':
                        coordinates = feature['geometry']['coordinates']
                        # use the Waypoint message to store the coordinates and orientation.
                        waypoints.append(Waypoint(latitude=coordinates[1], longitude=coordinates[0], orientation=0.0))
                self.waypoint_list_geo = waypoints
                response.success = True
        except Exception as e:
            self.get_logger().error(f"Failed to load waypoints from given file path: {e}")
            
        self.get_logger().info(f"Task 1: Loaded waypoints:  {self.waypoint_list_geo}")
        return response

    def convert_waypoints_to_robot_frame(self):
        
        if self.waypoint_list_geo:
            first_waypoint = self.waypoint_list_geo[0]
            yaw_angle = self.calculate_yaw_angle(first_waypoint)
        else:
            self.get_logger().error("first call function .set_waypoints_callback")
            return
        
        # Applying a transformation matrix with 2D rotation and translation to convert the waypoints to the robot frame.
        for coords in self.waypoint_list_geo:
            point = [coords.longitude, coords.latitude] 
            rotated_point = self.rotate_point(point, yaw_angle)
            rotated_robot_origin = self.rotate_point([self.robot_inital_geo[1],self.robot_inital_geo[0]], yaw_angle)
            translated_point = rotated_point - rotated_robot_origin
            self.waypoint_list_robot_frame.append(Waypoint(latitude=translated_point[1], longitude=translated_point[0], orientation=yaw_angle))
            
        self.get_logger().info(
            f" Task 2: Waypoints in robot frame:  {self.waypoint_list_robot_frame}"
        )

        pass

    def plot_waypoints(self):
        self.get_logger().info(
            f" Task 3: Plot and save a graph of loaded waypoints in robot coordinate frame (png)"
        )
        
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        
        # load the waypoints in the robot frame 
        x = [waypoint.longitude for waypoint in self.waypoint_list_robot_frame]
        y = [waypoint.latitude for waypoint in self.waypoint_list_robot_frame]
        yaw = self.waypoint_list_robot_frame[0].orientation
        
        # prepare quiver arrow for the orientation of the robot 
        # Calculate direction components based on yaw_angle
        dx = np.cos(yaw)
        dy = np.sin(yaw)
        
        # plot the waypoints in the robot frame  
        axs[0].scatter(x, y, color='r')
        axs[0].set_title('Transformed Waypoints')          
        
        # for comparison, plot the waypoints in the geo frame
        x_orig = [waypoint.longitude for waypoint in self.waypoint_list_geo]
        y_orig = [waypoint.latitude for waypoint in self.waypoint_list_geo]
        
        axs[1].scatter(x_orig, y_orig, color='r')
        axs[1].quiver(self.robot_inital_geo[1], self.robot_inital_geo[0], dx, dy, angles='xy', scale_units='xy', scale=1000, width=0.005, color="g")
        axs[1].plot(self.robot_inital_geo[1], self.robot_inital_geo[0], 'bo', label='Robot Origin')
        axs[1].set_title('Original Waypoints')
        
        plt.tight_layout()
        plt.show()             
        pass

    def get_robot_waypoints_callback(self, request, response):
        response.waypoints = self.waypoint_list_geo

        return response

    def reset_waypoints_callback(self, request, response):
        response.waypoints = []

        return response

    def call_set_waypoints_geo(self, request):
        self.future = self.set_waypoint_client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    waypoint_manager = WaypointManager()

    set_waypoints_msg = SetWaypoints.Request()
    set_waypoints_msg.file_path = "/home/bensalem/paltech_assignment/src/paltech_assignment/waypoints/waypoints.geojson"
    response = waypoint_manager.call_set_waypoints_geo(set_waypoints_msg)
    if response.success == True:
        waypoint_manager.convert_waypoints_to_robot_frame()
        waypoint_manager.plot_waypoints()
    else:
        print("No waypoints loaded")

    rclpy.spin(waypoint_manager)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
