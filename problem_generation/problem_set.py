from learncentive.problem_generation.difficulty_model import DifficultyModel

class ProblemSet():
    """ The ProblemSet class generates Problem Content to be
    exposed to the Frontend API. it does this in one of two ways:
            1. It grades a returning ProblemSet from the user to
            determine what to generate next.
            2. It looks at User history to determine what to
            generate next. """
    def __init__(self, results):
        self.graded = False
        self.problems = results['problems']
        self.quantity = results['meta']['quantity']
        # {problem difficulty: quantitiy}

        self.correct = {i:0 for i in self.quantity.keys()}
        # {problem difficulty: number correct}

    def grade(self):

        for problem in self.problems.keys():
            result = self.problems[problem]['result']
            difficulty = self.problems[problem]['difficulty']

            if result:
                self.correct[difficulty] += 1
        difficulties = self.quantity.keys()
        self.grades = {i:(self.correct[i]/self.quantity[i]) for i in difficulties}
        self.graded = True

    def new(self):
        pass
