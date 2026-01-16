### 🎢 Europa‑Park Coaster Recommender

A secure, structured, and user‑friendly web application that recommends the most suitable Europa‑Park roller coaster based on user preferences.


## Overview
The Europa‑Park Coaster Recommender is a web application that helps visitors discover which roller coaster best matches their preferences.
Users answer a short set of questions, and the system selects the most appropriate coaster based on predefined attributes.

The opening question is how tall is the user.
The following questions would be based on the persons length.

The program always starts with questions about the intensity of the coaster.
When rejecting an intense ride, more questions follow about the preference for fun roller coasters.

questions, they can scroll down and open the bar that displays a list of all the roller coasters.
Clicking on the link for a specific roller coaster takes them directly to the information about it.
 The disclaimer about the app can also be found in the bar below.

When the survey is completed, a recommended roller coaster is provided. On this page, the user will find a POV "ride video", the specifications, and the ride experience of the roller coaster.
The ride experience consists of 3 characteristics:

* Intensity
How intense the roller coaster is in the form of g-forces, tight turns or intense inversions.

* Thrill Factor
How exciting the ride is in the form of height, speed or scary inversions.

* Physical Load
How heavy the ride is. Consider the risk of getting nausea, the roughness of the ride and whether you'll need to recover after riding the coaster.


## Technical information
This project was built with a strong focus on clean architecture, security, and professional development practices.
It serves both as a functional tool and as a demonstration of secure backend design, input validation, and structured reasoning.

The web app works over a simple if else loop. The program takes a look over the data.
For instance; if inversions is not in data, ask the user if he wants inversions into the coaster.
One other method for asking questions is for instans; Does the user want a water coaster with one steep drop and a big splash or a roller coaster track that ends with a splash?


## Web Securety and juristics
The webapp contains a cople of safety priorities.
Furthermore, the web app considers legal liability. The disclaimer provides detailed information about the embedded video's shown on the recommended coaster pages from YouTube. It also emphasizes that users shouldn't take the web app's advice about roller coaster preferences too seriously. Medical history and Europa Park's own instructions are always the determining factor when riding a roller coaster. The questionnaire with the results is for educational and entertaining purposes for average roller coaster riders, not for people with a medical condition that could hinder to take a ride on a roller coaster.

