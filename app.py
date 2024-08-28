from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey #renaming the satisfaction survey variable from surveys.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES_KEY = 'responses'

''' SESSION
Session is basically a dictionary that, in our case, holds the values of the responses
RESPONSES_KEY is just being used as a consistent way to initialize the dictionary with the responses | session dictionary will look like the below
session = {'responses': [ 'answer1', 'answer2', etc...]}

#0 RESPONSES_KEY = 'responses'
#0 session       = {}

#1 session   | {'responses': []}
#2 responses | []
#3 responses | ['answer1','answer2']
       WITH VARIABLES                                     LITERAL
#4 session[RESPONSES_KEY] = [responses]  |  {}['responses'] = ['answer1','answer2']
#5 {'responses': ['answer1', 'answer2']}
'''

@app.route('/')
def home():
    '''Home page for survey start'''
    return render_template('home.html', survey=survey)


@app.route('/start', methods=['POST'])
def start_survey():
    '''Start survey with clearing the responses'''
    session[RESPONSES_KEY] = [] #1 looks like {'responses': []}
    return redirect('/questions/0') #NOTE: num is defined here by starting with 0 | num is dynamic and can be anything (within error handling guidlines)


@app.route('/answer', methods=['POST'])
def answer_handler():
    '''Save the responses and go to next question'''
    #users choice grabbed from the form in questions.html | answer is the 'name' in the html
    choice = request.form['answer']
    #add user response to the session which holds all the answers from the survey
    responses = session[RESPONSES_KEY] #2 pulling the list from the session dictionary (currently has nothing) | responses = [] | using list.append to add the user responses
    responses.append(choice) #3
    session[RESPONSES_KEY] = responses #4 adding responses to the session dictionary | since responses is the same as our key, it adds the user inputs as key val pair
    #5 results in session looking like {'responses': ['answer1']}
    
    if (len(responses) == len(survey.questions)): #if these are responses and length are equal, that means all the questions are answered
        return redirect("/end")
    else:
        return redirect(f"/questions/{len(responses)}") #sends to the next question based on number or responses there are in the session key


@app.route('/questions/<int:num>')
def survey_question(num):
    '''Presents the current/next question'''
    responses = session.get(RESPONSES_KEY)
    
    # error handling
    if (responses is None):
        # trying to access questions before start of survey
        return redirect("/")
    if (len(responses) == len(survey.questions)):
        # all the questions have been answered
        return redirect("/complete")
    if (len(responses) != num):
        # trying to access questions out of order
        flash(f"Invalid question id: {num}.")
        return redirect(f"/questions/{len(responses)}") #NOTE: num is then changed based on the number of response in the session key
    
    #grabbing the question from the survey based on the num
    question = survey.questions[num]
    #adding in response and survey length to change what the button says
    return render_template('questions.html', question=question, num=num, resp_len=len(responses), sur_len=len(survey.questions)-1)

@app.route('/end')
def survey_end():
    responses = session[RESPONSES_KEY] #grabbing the list of responses to display on the page
    return render_template('end.html',survey=survey, responses=responses)
