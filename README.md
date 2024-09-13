# CS50 Final Project: Rock Paper Scissors
## Video Demo:  https://youtu.be/ZcJYZ04Xo9s
## Deployed Site: https://jorenabat.pythonanywhere.com/
## Description:
### My journey through making this project:
For my final project, I wanted to create a simple game using all the skills that I have gathered throughout the course. I plan on persuing web development so I wanted to incorporate HTML, CSS, JavaScript and the web framework we learned which was Flask.

Upon debating what to choose, I decided on creating a Rock Paper Scissors game because I was able to use every skill and incorporate various little details to make the project a bit more complex. Some examples include randomness in the computer opponent, player input, changing the web page using JavaScript and more that I will explain in this document.

To start, let's go through my thought process and any obstacles I faced while making this project.

I started with getting the fundamental mechanics working before I added any extra bells and whistles to make the website look nicer. I did this fairly easily within Flask using Python. I looked over previous problem sets and the lectures to get a base within flask and used Python to create a bare bones version of Rock Paper Scissors that used an index page and rendered/redirected the user to a results screen. At this point, all I had was an app.py file, an index.html file and a result.html file.

The HTML files only had plain text and a sad looking dropdown box so I knew I wanted to make things look nicer. I wanted to incorporate Bootstrap since I used it in previous problem sets but I also knew that I wanted to create a layout.html first that I can copy the template across all HTML files. I created a layout.html file that contains the majority of the HTML code which also allowed me to use Bootstrap, one of the CSS Frameworks we learned in class in all HTML files. I used the bootstrap website and examples from previous problem sets to prepare the rest of the HTML files to use Bootstrap tags and features. I added various classes to the divs to make the website look nicer and have a more consistent style.

From there, I decided to spice things up a bit and incorporate some JavaScript. Since we used JavaScript fairly minimally during this course, I came across multiple issues that I had to search up on w3schools and also I asked cs50.ai duck to help me out. Eventually I managed to get an image of the object that the user picked, as well as some flavour text based on the chosen object. I did this by first hiding all the content that I coded into index.html that was saved for each object and only showed them once the user has selected the specific object in the dropdown box.

Next, I wanted to account for the instance where someone doesn't pick an object and just click "Select" right away. I created a missing.html file that users get sent to as some sort of an error page if someone doesn't pick an object. It displays the cat from the apology function in the finance problem set and makes the user click a button to try again.

Lastly, I wanted to make the result page a bit more interesting instead of simply saying if the user wins or loses. I first coded flavour text that changes based on the object that was chosen and the outcome. For example, if you chose a rock and you won, the text would say 'You crushed them!' or if you won with paper, it says 'You covered them up!', etc. I also wanted to change the background to be green or red depending on whether you win or lose respectively and I did this using python/flask to send the results to results.html and using Jinja to modify the page.

One of the biggest issues I faced was a complete oversight when dealing with ties. It was working perfectly fine but then upon adding more features such as the changing background in the results page, I completely forgot to account for when a tie happens. I got the error ***'UnboundLocalError: cannot access local variable 'bg_colour' where it is not associated with a value'***
I managed to fix this by simply assigning the variable 'bg_colour' and 'flavour_text' in the if branch that resulted in a tie.

Overall, this project was really fun to piece things together I learned throughout this course and I'm excited to continue learning and improving my skills to create even more things.

### Short description of each file
#### app.py
Where most of the logic in this game is located. It contains 2 routes, one for the index page or the page that people load into, and the play route where the game plays out and we are given a result.

#### layout.html
Barebones HTML / Bootstrap layout code that is copied throughout all the HTML files to use Bootstrap and both the CSS and JS file that I created for the project

#### script.js
JavaScript file that mostly handles displaying an image of the chosen object, as well as flavour text for said object.

#### style.css
CSS file for styling various things such as images of the objects.

#### index.html
The starting page that allows users to select an object and displays said object upon selection using JavaScript.

#### missing.html
If the user doesn't select anything, they are thrown to this page which tells the user to select an object before pressing select.

#### result.html
The results page that shows the result of the game. The background is changed based on the outcome and I used Jinja and python to have it change.
