## Inspiration
The inspiration from this project comes from CS326. This is our embedded systems class and have learned everything from this project from there. Also, we are using our SecurePi camera system for the final project for this class.

## What it does
It is a security system that uses a camera and a servo to open a door. Someone will watch the camera and determined whether or not the person at the door should be allowed entry. Using and MQTT broker, the person watching the camera will send a payload to a raspberry pi that will control a servo motor, which opens the door or closes it depending on the person. We also set up a SQL database and a webpage to allow for easy monitoring of what is going on.

## How we built it
We built it using the kits given to us for our CS326 class. This included a rasberry pi, a servo motor, a camera, and all the necessary electrical components. We mainly used python for coding except for the webpage which used html. Also C++ and C is used to program the ESP32 cams.

## How to use it
First there are two different servo files. One is for publishing to the raspberry pi with the servo, and the other is for subscribing to that publisher. The publisher should be connected to two pushbuttons that are used to send an open or close signal to the servo. The php file is used to create a webpage to view the database created by opening and closing the door. The ESP32 code is used to flash the ESP32 Cam AI Thinker. One cam is used for hosting wi-fi so the cam and laptop can communicate and one is used for the live feed.

## Challenges we ran into
Initially we wanted to use face recognition to make the system automatic. However, we ran into many problems with setting it up using the cameras we had. The libraries didn't work for one camera, and the other camera didn't have enough processing power for the facial recognition software

## Accomplishments that we're proud of
We are proud of the database and webpage we setup. This took a while because it was the first time we tried setting up a webpage/database. 

## What we learned
We learned a lot about how SQL and webpages work. Also, we gained a better understanding of how cameras operate and the libraries surrounding them. 

## What's next for PiSecure
We still want to setup facial recognition in the future despite the problems we have had so far. The next step would probably be to get a higher quality camera or find a different library to use.

## Credit
Some of the code we used in this project is taken from the CS326 labs written by Professor Schuurman. Also the code used to program the ESP32 is taken from the example code it comes with.
