# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "My_chatter: 1 messages, 0 services")

set(MSG_I_FLAGS "-IMy_chatter:/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(My_chatter_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg" NAME_WE)
add_custom_target(_My_chatter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "My_chatter" "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg" "std_msgs/Header"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(My_chatter
  "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/My_chatter
)

### Generating Services

### Generating Module File
_generate_module_cpp(My_chatter
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/My_chatter
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(My_chatter_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(My_chatter_generate_messages My_chatter_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg" NAME_WE)
add_dependencies(My_chatter_generate_messages_cpp _My_chatter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(My_chatter_gencpp)
add_dependencies(My_chatter_gencpp My_chatter_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS My_chatter_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(My_chatter
  "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/My_chatter
)

### Generating Services

### Generating Module File
_generate_module_lisp(My_chatter
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/My_chatter
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(My_chatter_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(My_chatter_generate_messages My_chatter_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg" NAME_WE)
add_dependencies(My_chatter_generate_messages_lisp _My_chatter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(My_chatter_genlisp)
add_dependencies(My_chatter_genlisp My_chatter_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS My_chatter_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(My_chatter
  "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/indigo/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/My_chatter
)

### Generating Services

### Generating Module File
_generate_module_py(My_chatter
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/My_chatter
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(My_chatter_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(My_chatter_generate_messages My_chatter_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cc/ee106a/fa17/class/ee106a-act/ros_workspaces/lab3/src/My_chatter/msg/JointState.msg" NAME_WE)
add_dependencies(My_chatter_generate_messages_py _My_chatter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(My_chatter_genpy)
add_dependencies(My_chatter_genpy My_chatter_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS My_chatter_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/My_chatter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/My_chatter
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(My_chatter_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/My_chatter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/My_chatter
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(My_chatter_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/My_chatter)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/My_chatter\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/My_chatter
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(My_chatter_generate_messages_py std_msgs_generate_messages_py)
endif()
