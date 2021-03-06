import math

class DifficultyModel():
    """The difficulty model handles the rules for generating new problem sets.
    When generating a new ProblemSet, a request will be made to an instance of the
    Difficulty Model Class which will dictate the quantity of problems and
    difficulty of those problems.

    These class attributes below hard code the difficulty configuration
    """
    problem_set_size = 10
    hard_problem_ratio = .2
    threshold = .93

    def __init__(self, grades):
        self.hard_problems = math.ceil(self.hard_problem_ratio * self.problem_set_size)
        self.easy_problems = self.problem_set_size - self.hard_problems


        for difficulty in range(len(grades)):
            self.current_difficulty = difficulty
            if grades[difficulty] < self.threshold:
                break

    def generate_problem_quantity(self):
        new_model = {}
        new_model[self.current_difficulty] = self.easy_problems
        new_model[self.current_difficulty+1] = self.hard_problems

        return new_model


# problem_difficulty = {
# 0: , # sums < 10
# 1:, # subtraction < 10
# 2:, # sums > 10 < 20
# }
"""Arithmetic:

    Level 0
        addition with numbers < 5
        subtraction < 5

    level 1
        addition >= 5 and < 10
        subtraction >= 5 and < 10

    level 2
        addition >= 10 and < 50
        subtraction >= 10 and < 50

    level 3
        multiplication < 5
        division < 5


    level 4
        multipication >= 5 and < 10

    level 5 .....

    PROPOSAL: Treat responses (i.e. correct or incorrect answers) from the user as
    statistical sample of their skill level. From the ratio of correct answers to
    total problems,  with the types of problem taken into account you can deduce
    the likelyhood they will answer future problems at.

    EXAMPLE RULE 1: Problems can be provided so that the rate of correct answers
    will be <93%. Once the correct answer rate hits 93% the next
    problem category is provided.

    numerical example:

        level 0: 95%
        level 1: 92%
        level 2: 83%
        level 3: 0%

        With this information and the above rule, the system would provide level
        2 problems until the user got to 90%, then it would provide level 3 problems

    EXAMPLE RULE 2: use a statistical Distribution of the student's
    skill level. The provided problem set follows a normal distribution of
    difficulty where the mean problem plus some deviation is expected
    to be answered correctly by the student. this distribution is updated everytime
    a problem set is returned with correct/incorrect labels.

        This can be done with each type of problem and only a mean number magnitude
    would need to be supplied for each one. (i.e. there is a distribution for each
    of:

    addition
    subtraction
    multipliction
    division
    composite problems )

    numerical example:
        1. A problem set is returned with the following:
            [   (addition, difficulty 1, correct),
                (subtraction, difficulty 3, correct),
                (division, difficulty 3, wrong),
                (addition, difficulty 2, correct),
                (multiplication, difficulty 2, wrong),
                (addition, difficulty 2, correct)   ]







guiding principles:
    always give a problem beyond the current problem difficulty level
"""
