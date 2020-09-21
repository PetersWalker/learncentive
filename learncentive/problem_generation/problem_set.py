import json
from random import shuffle

from learncentive.problem_generation.difficulty_model import DifficultyModel
from learncentive.problem_generation.problem import generate as generate_problem

class ProblemSet():
    """ The ProblemSet class generates Problem Content to be
    exposed to the Frontend API. it does this in one of three ways:
            1. It grades a returning ProblemSet (results) from the user to
            to construct a new problem set.the appropriate new problem set
            is dictated by the DifficultyModel.
            2. It looks at {grades}
            3. It generates problems alacarte, that is choosing a monodifficulty
            set of s certain difficulty
            """
    def __init__(self, results):
        self.quantity = results['quantity']
        self.correct = results['correct']
        self.grades = results['grades']
        self.graded = False
        self.problems = results['problems']

        self.__dict__ = {'quantity':self.quantity,
                         'correct': self.correct,
                         'grades': self.grades,
                         'graded': self.graded,
                         'problems': self.problems
                         }

    @classmethod
    def from_grades(cls, grades):
        """Use case: the first problemset in a user session may need to fetch
        grades from the database
        """
        new_model = DifficultyModel(grades)
        quantity = new_model.generate_problem_quantity()
        new_set = {
            'quantity': quantity,
            'grades': grades,
        }

        new_set['correct'] = {k: 0 for k in new_set['quantity']}
        new_set['problems'] = cls._generate_problems(new_set['quantity'])

        problem_set = cls(new_set)
        return problem_set

    @classmethod
    def from_json(cls, json_data):
        pydata = json.loads(json_data)
        quantity = {int(k):v for k, v in pydata['quantity'].items()}
        correct = {int(k):v for k, v in pydata['correct'].items()}
        grades = {int(k):v for k, v in pydata['grades'].items()}
        fixed_problem_set = {
            'quantity': quantity,
            'correct': correct,
            'grades': grades,
            'graded': pydata['graded'],
            'problems': pydata['problems']
        }
        return cls(fixed_problem_set)

    @classmethod
    def alacarte(cls, amount_of_probs=10, type_of_prob=0):
        quantity = {type_of_prob: amount_of_probs}
        new_set = {
            'quantity': quantity,
            'grades': {type_of_prob:0},
        }

        new_set['correct'] = {k: 0 for k in quantity}
        new_set['problems'] = cls._generate_problems(quantity)

        problem_set = cls(new_set)

        return problem_set

    def new_problem_set(self):
        if self.graded is False:
            self._grade_set()
        return self.from_grades(self.grades)

    def _grade_set(self):
        """"The formula used to calculate self.grades is the entire
        grading system. It's simply the average of previous grades
        and the most recent correct answer count
        """

        for k in self.quantity:
            self.grades[k] = (((self.correct[k]/self.quantity[k]) + self.grades[k]) /2)
        self.graded = True

    @staticmethod
    def _generate_problems(quantity):
        problems = []
        for k, v in quantity.items():
#                {0:8, 1:2}
            while v > 0:
                problem = generate_problem(k)
                new_problem_info = {
                    'question':problem.question,
                    'answer':problem.answer,
                    'difficulty': k,
                    'result': False
                     }
                problems.append(new_problem_info)
                v -= 1

        return problems

    def to_json(self):
        return json.dumps(vars(self))
