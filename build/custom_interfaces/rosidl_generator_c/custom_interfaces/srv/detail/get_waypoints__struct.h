// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/GetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/GetWaypoints in the package custom_interfaces.
typedef struct custom_interfaces__srv__GetWaypoints_Request
{
  uint8_t structure_needs_at_least_one_member;
} custom_interfaces__srv__GetWaypoints_Request;

// Struct for a sequence of custom_interfaces__srv__GetWaypoints_Request.
typedef struct custom_interfaces__srv__GetWaypoints_Request__Sequence
{
  custom_interfaces__srv__GetWaypoints_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__GetWaypoints_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'waypoints'
#include "custom_interfaces/msg/detail/waypoint__struct.h"

// Struct defined in srv/GetWaypoints in the package custom_interfaces.
typedef struct custom_interfaces__srv__GetWaypoints_Response
{
  custom_interfaces__msg__Waypoint__Sequence waypoints;
  bool success;
} custom_interfaces__srv__GetWaypoints_Response;

// Struct for a sequence of custom_interfaces__srv__GetWaypoints_Response.
typedef struct custom_interfaces__srv__GetWaypoints_Response__Sequence
{
  custom_interfaces__srv__GetWaypoints_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__GetWaypoints_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_
