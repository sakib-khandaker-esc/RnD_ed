# RnD_ed
These Repository containt projects related to RnD_BUCC

Documentation >> Random Password Generator
Hello World: 
Good day, everyone!
Thanks for opening the link! Here I have tried to put together a project from the resources assigned to me to make it! Thanks to all the people who worked hard to make those resources and those who compiled them together to make amazing collections of ideas! Thanks to their choice and preferences. 

What is it: 
I am Sakib, an undergraduate student from Brac University! Today, in this project I have learned and created, there was a slight touch of modification that I made! Since I was not that much familiar with Java Script, I have decided to do the entire work using python! Yes you are thinking it right, it’s backend logics and codes are done with python/ Flask : : A well-liked development framework for Python web applications and because of its simplicity and minimalistic style I have decided to choose it. All the codes of designing the server side logic and routing is done with this. To make the generator more secure, I have selected to import the random module. After generation, using the clipboard API, I have exploited the feature of copy functionality. And for Frontend I have used HTML5, CSS3, and JavaScript for creating the user interface. 

PREREQUISITES: 
Python 3.6+ >> Please install (bash) this using “pip install flask
” →And now, Run : : “python app.py”
Flask package
A Web browser with common sense. Go to the “http://localhost:5000” local host from that browser. 

>> You can clone the repository (bash):
git clone https://github.com/your-repo/password-generator.git 
cd password-generator 

If you are wondering like me, that what it does: 
Just like we copy things and paste it, or download it to our local dick, these commands clone (download a copy of) a Git repository from GitHub. In this case, the one you are seeing in your address bar after entering the repo! Please copy that link and paste it with the commands! Maintain the orders as well. It will create a local directory called password-generator with all the repository's files inside it.
The second command changes your current working path to the newly copied and downloaded password-generator folder that you created recently using the first command. 
Get Introduced with the INTERFACE: 
Use the length Slider, which almost looks like <> in your dialogue of entering the password, there, you normally choose password length (MIN 6-50 MAX chars)
Check the checkboxes with your types of requirements you need. This under the hood works like booleans to turn the decisions on or off! Just like you used to code with flagging systems, yeah just like that. 
Generate Button, runs the python function from inside the app.py where it returns/ Creates new password and later from inside the index.html, the function of JS works to make the display. You click it to make sure the password is generated correctly.  (also an alternative approach) if frontend-only needed.
Result Display will show you the generated password
Copy Button, you know it.

 Potential Challenges I Bumped Into: 
Challenge A: How would I make the password secure and unpredictable by greedy password hungry people who are always lurking to fetch it? 
Saviour: I have used the power of randomness to generate the password, from choosing it from the random module already built in method. Now, good luck with your prediction confidence. 

Challenge B: If you need cross-browser clipboard access then what? 
Saviour: Tried Implementing clipboard API with fallback alerts.

Challenge C: Is that scalable in terms of design when it comes to your Phone? 
Saviour: Tried being lazy using Flexbox: a CSS layout model that allows you to design flexible and responsive layouts without floats or positioning hacks.

Challenge D: Form submission handling
Saviour: Instead of letting a form submit and reload the page, the code intercepts the submission, sends the data in the background, and handles the response without refreshing it.

Challenges E: So many things altogether? 
Saviour Mindset: All you need to do it develop an outline of your project, what are the elements that it will keep inside itself, what are the features and models you are gonna use there, what are the tools and resources you can use, chalk them down and then start your execution one after another! If you feel too stressed, just remember that’s just one google away. 


VISUALS: 
Terminal Commands:
[git clone] → [cd] → [venv] → [activate] → [pip install] → [python app.py]
Browser Access:
[localhost:5000] → [Generate Password]

Start
└🟩> Clone Repository
│ git clone https://github.com/your-repo/password-generator.git
└🟩> Navigate to Project Directory
│ cd password-generator
└🟩> Create Virtual Environment
│ python -m venv venv
└🟩> Activate Virtual Environment
│ Linux/Mac: source venv/bin/activate
│ Windows: venv\Scripts\activate
└🟩> Install Dependencies
│ pip install flask
└🟩> Run Flask Application
│ python app.py
└🟩> Access in Browser
│ Open http://localhost:5000
└🟩> Generate Password

Conclusion:

This project shows some initial work related to Full-stack web development, One of the primary concepts of secure password generation techniques (if you are interested please meet cryptography ASAP), modern web design principles, problem-solving in implementation and building logics and arts side by side. (Sorry about the colors selected! You can actually change them from the index.html folder! Just click on the ⏺️ color square and then change it as you want!)

The small combination of backend and frontend makes it lightweight, dummy friendly yet works well, you would love it, it’s suitable for both learning and practical use. Thank you for reading my gibberish! Good day! 


