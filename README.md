# 🚁 Wraith – Autonomous Payload Delivery System

An autonomous UAV payload delivery system developed using **PX4 SITL**, **Gazebo Harmonic**, and **MAVSDK-Python**. The project demonstrates autonomous GPS-based navigation, payload transportation, precision payload release, and Return-to-Launch (RTL) in a realistic simulation environment.

---

## 📌 Project Overview

Wraith is designed to simulate an autonomous aerial logistics mission where a multirotor UAV:

* Takes off autonomously
* Navigates to a predefined GPS waypoint
* Carries a suspended payload
* Releases the payload over the target location
* Returns safely to the launch point

The project is built on the PX4 Autopilot ecosystem and serves as a foundation for future work involving computer vision, precision landing, and intelligent autonomous delivery.

---

## ✨ Features

* ✅ PX4 SITL simulation
* ✅ Gazebo Harmonic environment
* ✅ Autonomous takeoff
* ✅ GPS waypoint navigation
* ✅ Payload attachment using Gazebo Detachable Joint
* ✅ Autonomous payload release
* ✅ Return-to-Launch (RTL)
* ✅ Downward-facing camera integration
* ✅ Custom Gazebo world with payload delivery scenario
* 🔄 Planned: AprilTag-based precision payload drop
* 🔄 Planned: Mission dashboard
* 🔄 Planned: Wind disturbance analysis

---

## 🛠️ Technologies Used

* PX4 Autopilot
* Gazebo Harmonic
* MAVSDK-Python
* Python
* Ubuntu 24.04
* ROS 2 Jazzy
* VS Code
* Git & GitHub

---

## 📂 Repository Structure

```text
Wraith_Project/
│
├── dashboard/
├── config/
├── docs/
├── logs/
├── media/
├── models/
│   ├── apriltag_marker/
│   └── payload_box/
│
├── px4_custom/
│   ├── models/
│   └── worlds/
│
├── scripts/
│   ├── compute_target_gps.py
│   └── mission_gps_drop.py
│
├── worlds/
│   └── drop_demo.sdf
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🚀 Mission Workflow

```text
Takeoff
    │
    ▼
GPS Navigation
    │
    ▼
Reach Delivery Point
    │
    ▼
Descend
    │
    ▼
Release Payload
    │
    ▼
Return To Launch (RTL)
```

---

## 📦 Simulation Components

### Drone

* PX4 X500 Multirotor
* Downward-facing camera
* Custom payload attachment mechanism

### Payload

* Custom Gazebo payload model
* Detachable joint implementation
* Autonomous release command

### World

* Custom delivery environment
* AprilTag marker
* GPS waypoint target

---

## 🔧 Requirements

* Ubuntu 24.04
* PX4 Autopilot
* Gazebo Harmonic
* ROS 2 Jazzy
* MAVSDK-Python
* Python 3.10+

---

## ▶️ Running the Mission

1. Launch PX4 SITL with the custom world.
2. Start the Gazebo simulation.
3. Run the mission script:

```bash
python3 mission_gps_drop.py
```

The UAV will:

* Arm automatically
* Take off
* Navigate to the delivery location
* Release the payload
* Return to launch

---

## 📈 Future Work

* AprilTag-based visual precision delivery
* Live mission dashboard
* Battery-aware mission planning
* Multi-waypoint delivery
* Dynamic obstacle avoidance
* Wind disturbance analysis
* Object detection using deep learning
* Mission report generation

---

## 👨‍💻 Author

**Samadrita Bhattacharya**

B.Tech Aerospace Engineering

Amrita Vishwa Vidyapeetham

---

## 📜 License

This project is released under the MIT License.

---

⭐ If you find this project interesting, consider starring the repository!
