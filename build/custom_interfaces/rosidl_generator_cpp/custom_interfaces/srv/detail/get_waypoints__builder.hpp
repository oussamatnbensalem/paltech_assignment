// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/GetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_

#include "custom_interfaces/srv/detail/get_waypoints__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::GetWaypoints_Request>()
{
  return ::custom_interfaces::srv::GetWaypoints_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_GetWaypoints_Response_success
{
public:
  explicit Init_GetWaypoints_Response_success(::custom_interfaces::srv::GetWaypoints_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::GetWaypoints_Response success(::custom_interfaces::srv::GetWaypoints_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::GetWaypoints_Response msg_;
};

class Init_GetWaypoints_Response_waypoints
{
public:
  Init_GetWaypoints_Response_waypoints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetWaypoints_Response_success waypoints(::custom_interfaces::srv::GetWaypoints_Response::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return Init_GetWaypoints_Response_success(msg_);
  }

private:
  ::custom_interfaces::srv::GetWaypoints_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::GetWaypoints_Response>()
{
  return custom_interfaces::srv::builder::Init_GetWaypoints_Response_waypoints();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_
