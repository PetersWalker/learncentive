import json
from random import shuffle

from learncentive.problem_generation.difficulty_model import DifficultyModel
from learncentive.problem_generation.problem import generate as generate_problem

class ProblemSet():
    """ The ProblemSet class generates Problem Content to be
    exposed to the Frontend API. it does this in one of two ways:
            1. It grades a returning ProblemSet (results) from the user to
            to construct a new problem set.the appropriate new problem set
            is dictated by the DifficultyModel.
            2. It looks at (grades) from the database???
            """

    def __init__(self, *results, grades=None):

        if len(results) > 0:
            results, = results
            self.quantity = results['quantity']
            self.correct = results['correct']
            self.grades = results['grades']
            self.graded = False
            self.problems = results['problems']

        elif grades is not None:
            self.quantity = DifficultyModel(grades).generate_problem_quantity()
            self.correct = {i:0 for i in self.quantity.keys()}
            self.grades = grades
            self.graded = False
            self.problems = self._generate_problems(self.quantity)

        self.__dict__ = {'quantity':self.quantity,
                         'correct': self.correct,
                         'grades': self.grades,
                         'graded': self.graded,
                         'problems': self.problems
                         }
    def grade(self):
        """"The formula used to calculate self.grades is the entire
        grading system. It's simply the average of previous grades
        and the most recent correct answer count
        """
        difficulties = self.quantity.keys()
        for i in difficulties:
            self.grades[i] = (((self.correct[i]/self.quantity[i]) + self.grades[i]) /2)
        self.graded = True

    def new_problem_set(self):
        if self.graded == False:
            self.grade()

        return ProblemSet(grades=self.grades)

    def _generate_problems(self, quantity):
        problems = []
        for difficulty in quantity.keys():
            while quantity[difficulty] > 0:
                problem = generate_problem(difficulty)
                new_problem_info = {
                    'question':problem.question,
                    'answer':problem.answer,
                    'difficulty': difficulty,
                    'result': False
                     }
                problems.append(new_problem_info)
                quantity[difficulty] -= 1

        return problems

    def to_json(self):
        return json.dumps(vars(self))

    @classmethod
    def from_json(cls, json_data):
        
        def _patch_json_string_index_to_int(problem_set):
            problem_set.quantity = {int(k):v for k,v in problem_set.quantity.items()}
            problem_set.correct = {int(k):v for k,v in problem_set.correct.items()}
            problem_set.grades = {int(k):v for k,v in problem_set.grades.items()}

        data = json.loads(json_data)

        try:
            problem_set = ProblemSet(data)
            _patch_json_string_index_to_int(problem_set)
            return problem_set

        except KeyError:
            print('data in {} doesn\'t match the ProblemSet spec'.format(data))
