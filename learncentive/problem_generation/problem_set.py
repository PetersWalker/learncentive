import json
from random import shuffle

from learncentive.problem_generation.difficulty_model import DifficultyModel
from learncentive.problem_generation.problem import generate as generate_problem

class ProblemSet():
    """ The ProblemSet class generates Problem Content to be
    exposed to the Frontend API. it does this in one of three ways:
            1. It grades a returning ProblemSet (results) from the user to
            to construct a new problem set. the appropriate new problem set
            is dictated by the DifficultyModel.
            2. It looks at previous grades (possibly from the database).
            3. It generates problems alacarte, that is choosing a monodifficulty
            set of s certain difficulty
            """
    def __init__(self, results):
        # self.quantity = results['quantity']
        # self.correct = results['correct']
        self.grades = results['grades']
        self.graded = False
        self.problems = results['problems']

        self.__dict__ = {'grades': self.grades,
                         'graded': self.graded,
                         'problems': self.problems
                         }

    @classmethod
    def from_grades(cls, grades):
        new_problem_set = {'grades': grades}

        diff_model = DifficultyModel(grades)
        quantity = diff_model.generate_problem_quantity()
        new_problem_set['problems'] = cls._generate_problems(quantity)

        new_problem_set = cls(new_problem_set)

        return new_problem_set

    @classmethod
    def alacarte(cls, amount_of_probs=10, type_of_prob=0):
        quantity = {type_of_prob: amount_of_probs}
        grades = [ 1 for i in range(type_of_prob)]
        grades.append(0)
        new_set = {
            'grades': grades,
            'graded': False,
            'problems': cls._generate_problems(quantity)
        }

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

        if self.graded is False:
            difficulties = {problem['difficulty'] for problem in self.problems}

            """Count the amount of correctly answered problems, and
            the amount of each problem difficulty.
            """
            quantity = dict.fromkeys(difficulties, 0)
            correct = dict.fromkeys(difficulties, 0)
            for problem in self.problems:
                quantity[problem['difficulty']] += 1
                if problem['correct'] is True:
                    correct[problem['difficulty']] += 1

            """Grade set by difficulty and average with the corresponding
            difficulty in self.grades.
            """
            grades_dict = {i:self.grades[i] for i in range(len(self.grades))}
            for i in quantity.keys():
                new_grade = correct[i]/quantity[i]
                try:
                    grades_dict[i] = (new_grade + grades_dict[i]) / 2
                except KeyError:
                    grades_dict[i] = new_grade
                #[.92, .5]
            self.grades = [v for _, v in grades_dict.items()]
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
                    'correct': False
                     }
                problems.append(new_problem_info)
                v -= 1

        return problems
