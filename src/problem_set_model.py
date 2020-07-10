class ProblemSetModel():

    pass


"""
Arithmetic:

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
    will be <90%. Once the correct answer rate hits 90% the next
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
            [   (addition, diffi culty 1, correct),
                (subtraction, difficulty 3, correct),
                (division, difficulty 3, wrong),
                (addition, difficulty 2, correct),
                (multiplication, difficulty 2, wrong),
                (addition, difficulty 2, correct)   ]









"""
