// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/Waypoint.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_

#include "custom_interfaces/msg/detail/waypoint__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_Waypoint_orientation
{
public:
  explicit Init_Waypoint_orientation(::custom_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::Waypoint orientation(::custom_interfaces::msg::Waypoint::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_longitude
{
public:
  explicit Init_Waypoint_longitude(::custom_interfaces::msg::Waypoint & msg)
  : msg_(msg)
  {}
  Init_Waypoint_orientation longitude(::custom_interfaces::msg::Waypoint::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_Waypoint_orientation(msg_);
  }

private:
  ::custom_interfaces::msg::Waypoint msg_;
};

class Init_Waypoint_latitude
{
public:
  Init_Waypoint_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Waypoint_longitude latitude(::custom_interfaces::msg::Waypoint::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_Waypoint_longitude(msg_);
  }

private:
  ::custom_interfaces::msg::Waypoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::Waypoint>()
{
  return custom_interfaces::msg::builder::Init_Waypoint_latitude();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__WAYPOINT__BUILDER_HPP_
