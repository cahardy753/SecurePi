## Inspiration
The inspiration from this project comes from CS326. This is for our embedded systems class and have learned everything from this project from there.

## Project Summary
Our project, Pi Secure, is a prototype security system designed to control access to a building using a web-based interface. The system consists of a video camera and a simulated door mechanism (constructed from a cardboard shoebox). The primary objective was to create a simple yet functional access control system that allows a user to remotely decide who may enter a secured area.The system works as follows: a live video feed is streamed from the ESP32-CAM module to a web interface, allowing a user to observe the area outside the door. The user can control the camera’s orientation via two servo motors that enable pan and tilt functionality. To control door access, two push buttons on the webpage allow the user to open or close the door. This mechanism is driven by another servo motor and controlled through MQTT messaging. Lastly, we also set up a SQL database and so one may monitor when the door has been opened or closed. The video stream and camera controls are served from the ESP32 using HTTP while the database is run on Aiven. Much of the code used in our project was open-source or vendor provided.

## How we built it
We built it using the kits given to us for our CS326 class. This included a rasberry pi, a servo motor, a camera, and all the necessary electrical components. We mainly used python for coding except for the webpage which used html. Also C++ and C is used to program the ESP32 cams.

## How to use it
First there are two different servo files. One is for publishing to the raspberry pi with the servo, and the other is for subscribing to that publisher. The publisher should be connected to two pushbuttons that are used to send an open or close signal to the servo. The php file is used to create a webpage to view the database created by opening and closing the door. The ESP32 code is used to flash the ESP32 Cam AI Thinker and setup a webpage for controlling the camera and seeing the live vido feed.

## Challenges we ran into
Initially we wanted to use face recognition to make the system automatic. However, we ran into many problems with setting it up using the cameras we had. The libraries didn't work for one camera, and the other camera didn't have enough processing power for the facial recognition software

## What we learned
We learned a lot about how SQL and webpages work. Also, we gained a better understanding of how cameras operate and the libraries surrounding them. 

## What's next for PiSecure
We still want to setup facial recognition in the future despite the problems we have had so far.

## Credit
Some of the code we used in this project is taken from the CS326 labs written by Professor Schuurman. Also the code used to program the ESP32 is taken from the example code it comes with.
