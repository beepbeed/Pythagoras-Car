
# Introduction

<p>The issue that Pythagoras aims to solve is the question of how to navigate a maze of obstacles completely autonomously, even if the complete maze is unknown. These obstacles will include pools of lava, which should be avoided, and gems, which should be detected and collected by playing a sound. Pythagoras will detect its environment and identify obstacles via a variety of sensors while slowly building up an internal map of the maze.</p>

# Design

![Electrical diagram](electricalDiagram.png)

<p>In order to reach our final product, we hope to integrate an array of sensors that work with a localization program onboard a Raspberry Pi 3. These various sensors on the car will  include ultrasonic sensors, load cells, photoresistors, IR sensors and a camera which will map out the general environment for the car while also allowing for obstacle detection.</p>

![Pan tilt mechanism](Pythagoras.png)

# Implementation

<p>To complete our objective, we will be using Python as our main coding language. With Python, we will be able to access various packages such as time, motor, (add more that we might need) which will help accomplish our goals.</p>

<p>Specifically, this project will make use of motor, the embedded time library, GPIO, I2C, Turtle, Infrared, and MPU packages in our code. We will be organizing our code within a variety of files, each one pertaining to some specific part of the robotic car and connected through imports. Most of our inputs will be run through Git Bash/Nano, which will be our main control scheme.</p>


> The methodology of our vehicle goes as follows:</p>
> - The GPIO will be our primary way of automated movement. 
> - We will use the camera module (infrared) as an “obstacle” detection mechanism. 
> - The MPU will be the way we will track the movement and acceleration of the robot and store that data. 
> - With the stored data, we will use Turtle to draw a map of the obstacle course, like a way of digital localization and see the path the robot took to complete it. 
> 	- We will also use Turtle to draw the obstacles the camera module recognizes, so we can see if there are any walls obstructing the robot.





