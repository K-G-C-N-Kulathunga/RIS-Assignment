cmake_minimum_required(VERSION 3.8)
project(tb3_maze_nav)

find_package(ament_cmake REQUIRED)

# Install non-code resources
install(DIRECTORY launch worlds models config rviz resource
  DESTINATION share/${PROJECT_NAME}
)

# Also install package.xml so `ros2 pkg` can find it
install(FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
