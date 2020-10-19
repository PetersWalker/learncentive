from learncentive.blueprints.problem_generation.difficulty_model import DifficultyModel
from learncentive.tests.fixtures import client

def test_difficulty_model_finds_current_difficulty(client):
    grades = {0: .9, 1: .75, 2: .50}
    test_model1 = DifficultyModel(grades)
    assert test_model1.current_difficulty == 0

    grades = {0: .93, 1: .75, 2: .50}
    test_model2 = DifficultyModel(grades)
    assert test_model2.current_difficulty == 1

    grades = {0: .93, 1: 1, 2: .93}
    test_model2 = DifficultyModel(grades)
    assert test_model2.current_difficulty == 2


def test_difficulty_model_specifies_new_problem_difficulties(client):
    model1 = DifficultyModel({0: .93, 1: .75, 2: .50})
    assert model1.generate_problem_quantity() == {1: 8, 2: 2}

    model2 = DifficultyModel({0: .94, 1: .5})
    assert model2.generate_problem_quantity() == {1: 8, 2: 2}

# def test_difficulty_model_grades_are_ints(client):
