import quiz_data as qd


def start():
    user_answers = list()
    result = 0
    question_number = 0
    # our dictionary is as such: {key: question, value: answer}
    for question, answer in qd.questions.items():
        # the following two lines print the question number alongside the question
        question_number += 1
        print(str(question_number) + '- ' + question)
        # print the options for each question
        for option in qd.options[question_number - 1]:
            print('\t', option)
        # store the answer of the user in a variable
        while True:
            user_answer = input('\t Enter (A, B, C, or D): ').upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
        user_answers.append(user_answer)
        # store the correct answer that is in the dictionary, in another variable - just to make it easier to read
        correct_answer = qd.questions.get(question)
        # compare the answers
        result += grade(user_answer, correct_answer)
        # print('\n-----------------------------------------\n')
        print()

    display_results(user_answers, result)


def grade(user, answer):
    if user == answer:
        # print('\t\t==> CORRECT!')
        return 1
    else:
        # print('\t\t==> Incorrect :(')
        return 0


def repeat():
    # reminder to convert the user response to lowercase, because all the options in the yesses list are lowercase
    redo = input('Do you want to reattempt the quiz (yes/no): ').lower()
    if redo not in qd.yesses:
        print('Quiz has ended.')
        return False
    return True


def display_results(useranswers, result):
    print('---------------------------')
    print('\t\tRESULTS')
    print('---------------------------')
    print('Your Answers:', end=' ')
    for answer in useranswers:
        print(answer, end=' ')
    print()
    print('Correct Answers: ', end=' ')
    for k, v in qd.questions.items():
        print(v, end=' ')
    score = int((result / len(qd.questions)) * 100)
    print(f'\nYour score is {score} %')
    print('---------------------------')


"""
    Validate the quiz before initiating it. This is a very important step, if we are gonna use this program for
    more quizzes in the future.
"""

if len(qd.options) != len(qd.questions):
    print(f'Error - Questions and Options Lists are not aligned properly.\n-Number of Questions:{len(qd.questions)}'
          f'\n-Number of Options Lists: {len(qd.options)}')
    exit()


attempts = 2        # user can get 2 more attempts
start()             # first attempt
while repeat() and attempts > 0:
    print('\n\n----------------------------------------------\n')
    start()
    attempts -= 1

if attempts == 0:
    print('Sorry. You ran out of attempts.')