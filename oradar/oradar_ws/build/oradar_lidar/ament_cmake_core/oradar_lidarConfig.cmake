# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_oradar_lidar_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED oradar_lidar_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(oradar_lidar_FOUND FALSE)
  elseif(NOT oradar_lidar_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(oradar_lidar_FOUND FALSE)
  endif()
  return()
endif()
set(_oradar_lidar_CONFIG_INCLUDED TRUE)

# output package information
if(NOT oradar_lidar_FIND_QUIETLY)
  message(STATUS "Found oradar_lidar: 0.0.0 (${oradar_lidar_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'oradar_lidar' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${oradar_lidar_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(oradar_lidar_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${oradar_lidar_DIR}/${_extra}")
endforeach()
