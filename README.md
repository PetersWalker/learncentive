# Learncentive
An automated tutoring web application


##Development Workflow

 #### React App: 
    1. navigate to the js direcctory in the classroom blueprint
    2. Run 'npm run serve' to run the react development server
    3. Modify the applicable files in blueprints/classroom/static/js
    4. Run 'npm run build' to bundle js files in react-dist to be imported by the classroom template
    
 ### Flask App:
    1. Write test in applicable tests directory 
    2. Run pytest in the tests directory and ensure you have a failing test
    3. Add or modify just enough code to ensure the test passes
    4. Ensure Flask development server is running to catch any unforseen errors
 

## Prerequisites
    Postgresql version 12+
    npm version 14+
    Python3
    
## Getting Started

### Setting up the virtual environment
1. "git clone https://github.com/PetersWalker/learncentive" in desired project directory
2. "pip install virtualenv"
3. "virtualenv venv" in the place where you keep all your virtual environments
4. "source venv/bin/activate" to enter the virtual environment
5. "pip install -r requirements.txt" in the learncentive folder

### Setting up the postgres databases
1. 