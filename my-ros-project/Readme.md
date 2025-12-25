# ROS 2 Autonomous Turtle Controller (Square Trajectory)

## 🤖 Project Overview
This project implements a **ROS 2 (Robot Operating System)** control node written in **Python**. It autonomously navigates a robot (Turtlesim) in a precise geometric square pattern using a state-machine logic. 

This project demonstrates core robotics concepts including **Node creation**, **Topic Publishing**, **Velocity Kinematics**, and **Open-loop Control**.

![Simulation Demo](turtle_square.mp4)
*(Note: Add a screenshot of your Turtlesim window here)*

## 🚀 Key Features
* **ROS 2 Architecture:** Implements a custom Node (`square_drawer`) that interfaces with the ROS 2 ecosystem.
* **Topic Communication:** Publishes `geometry_msgs/Twist` messages to the `/turtle1/cmd_vel` topic to control linear and angular velocity.
* **State Machine Logic:** Uses a timer-based callback loop to switch between "Drive" and "Turn" states without blocking the thread.
* **Clean Termination:** Handles `KeyboardInterrupt` for safe node shutdown.

## 🛠️ Tech Stack
* **OS:** Ubuntu 22.04 LTS (via WSL2)
* **Middleware:** ROS 2 Humble Hawksbill
* **Language:** Python 3.10
* **Library:** `rclpy` (ROS Client Library for Python)
* **Simulator:** Turtlesim

## ⚙️ Prerequisites
Ensure you have ROS 2 installed and sourced.
```bash
source /opt/ros/humble/setup.bash
