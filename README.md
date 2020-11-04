# Quiz
General knowladge quiz
import random


def run_test(questions):
    score = 0
    wrong_answers = []
    random_questions = generate_random_questions(questions)
    for question in random_questions:
        answer = input(question["text"])
        if answer == question["answer"]:
            score += 1
        else:
            wrong_answers.append(question)
    show_score(score, len(questions))
    show_correct_answers(wrong_answers)


def generate_random_questions(questions):
    shuffled_questions = random.sample(questions, len(questions))
    return shuffled_questions


def show_score(score, total_number_of_questions):
    print("You got " + str(score) + "/" + str(total_number_of_questions) + " correct")


def show_correct_answers(wrong_answered_questions):
    for item in wrong_answered_questions:
        print(item["text"] + " The correct answer was " + "'" + item["answer"] + "'")


questions = [
    {
        "text":  "Which one is the best car brand ?\n(a) BMW\n(b) Benz\n(c) Porshe\n\n",
        "answer": "a"
    },
    {
        "text": "What is the result of this equation ? 2+2*4 = \n(a) 6\n(b) 8\n(c) 10\n\n",
        "answer": "c"
    },
    {
        "text": "Which is the fastest animal on the land ?\n(a) Cheetah\n(b) rat\n(c) cat\n\n",
        "answer": "a"
    },
    {
        "text": "which planet is known as the Red Planet ?\n(a) Earth\n(b) Mars\n(c) Moon\n\n",
        "answer": "b"
    },
    {
        "text": "which is the tallest animal on the earth ?\n(a) Tiget\n(b) Mice\n(c) Giraffe\n\n",
        "answer": "c"
    },
    {
        "text":  "Adults have a total of 34 theeth\n(a) True\n(b) False\n\n",
        "answer": "b"
    },
    {
        "text": "There are 30 days in May\n(a) True\n(b) False\n\n",
        "answer": "b"
    },
    {
        "text": "New York is the capital of America\n(a) True\n(b) False\n\n",
        "answer": "b"
    },
    {
        "text": "A jellyfish is 95% water\n(a) True\n(b) False\n\n",
        "answer": "a"
    },
    {
        "text": "Bubble gum contains rubber\n(a) True\n(b) False\n\n",
        "answer": "a"
    },
]

run_test(questions)
