// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/SetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__SET_WAYPOINTS__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__SET_WAYPOINTS__BUILDER_HPP_

#include "custom_interfaces/srv/detail/set_waypoints__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_SetWaypoints_Request_file_path
{
public:
  Init_SetWaypoints_Request_file_path()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::SetWaypoints_Request file_path(::custom_interfaces::srv::SetWaypoints_Request::_file_path_type arg)
  {
    msg_.file_path = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::SetWaypoints_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::SetWaypoints_Request>()
{
  return custom_interfaces::srv::builder::Init_SetWaypoints_Request_file_path();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_SetWaypoints_Response_success
{
public:
  Init_SetWaypoints_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::SetWaypoints_Response success(::custom_interfaces::srv::SetWaypoints_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::SetWaypoints_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::SetWaypoints_Response>()
{
  return custom_interfaces::srv::builder::Init_SetWaypoints_Response_success();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__SET_WAYPOINTS__BUILDER_HPP_
