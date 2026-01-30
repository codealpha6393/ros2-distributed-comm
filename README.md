# Autonomous Communication Node (ROS 2)

A distributed system node designed for real-time sensor communication and autonomous navigation.

## 🔧 Architecture & Systems
* **Distributed Messaging:** Uses Publisher/Subscriber patterns to handle high-frequency sensor data streams.
* **Concurrency:** Optimized Python threads to handle navigation algorithms without blocking communication sockets.
* **Fault Tolerance:** Implemented obstacle avoidance logic that interrupts main path planning when proximity sensors trigger (Safety Systems).

## 📂 Structure
* `/robotics-algorithm`: Core pathfinding logic (A* implementation).
* `/ros-project`: The node configuration and launch files.
