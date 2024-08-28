class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"] #allowing for default options when there is no choices provided

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

#IGNORE THESE
personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)
#IGNORE THESE
surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}

for i,survey in enumerate(satisfaction_survey.questions):
    print(i,survey.question)
''' Result
0 Have you shopped here before?
1 Did someone else shop with you today?
2 On average, how much do you spend a month on frisbees?
3 Are you likely to shop here again?
'''

'''
# Loop through the questions in the satisfaction_survey
for i, question in enumerate(satisfaction_survey.questions, start=1):
    print(f"Question {i}: {question.question}")
    print(f"Choices: {', '.join(question.choices)}")
    print(f"Allow Text Response: {question.allow_text}")
    print()


- satisfaction_survey.questions | Accesses the list of Question objects in the Survey.
- question.question | Accesses the text of each question.
- question.choices | Accesses the list of choices available for each question.
- question.allow_text | Checks if text responses are allowed for the question.


For the given satisfaction_survey, running the above code will produce:
Question 1: Have you shopped here before?
Choices: Yes, No
Allow Text Response: False

Question 2: Did someone else shop with you today?
Choices: Yes, No
Allow Text Response: False

Question 3: On average, how much do you spend a month on frisbees?
Choices: Less than $10,000, $10,000 or more
Allow Text Response: False

Question 4: Are you likely to shop here again?
Choices: Yes, No
Allow Text Response: False

'''