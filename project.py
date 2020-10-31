from Question import Question
import random

question_prompts = [
    "Which one is the best car brand ?\n(a) BMW\n(b) Benz\n(c) Porshe\n\n",
    "What is the result of this equation ? 2+2*4 = \n(a) 6\n(b) 8\n(c) 10\n\n",
    "Which is the fastest animal on the land ?\n(a) Cheetah\n(b) rat\n(c) cat\n\n",
    "which planet is known as the Red Planet ?\n(a) Earth\n(b) Mars\n(c) Moon\n\n",
    "which is the tallest animal on the earth ?\n(a) Tiget\n(b) Mice\n(c) Giraffe\n\n",
    "The largest 'Democracy' in the world ?\n(a) China\n(b) America\n(c) India\n\n",
    "How many years are there in a century ?\n(a) One Hundred\n(b) ten\n(c) one\n\n",
    "Which is the largest country in the world ?\n(a) America\n(b) Russia\n(c) China\n\n",
    "Which is the most sensitive organ in our body ?\n(a) Heart\n(b) eyes\n(c) Skin\n\n",
    "Whic is the largest ocean in the world ?\n(a) Pacific\n(b) Atlantic\n(c) Indian\n\n",
    "Adults have a total of 34 theeth\n(a) True\n(b) False\n\n",
    "There are 30 days in May\n(a) True\n(b) False\n\n",
    "New York is the capital of America\n(a) True\n(b) False\n\n",
    "A jellyfish is 95% water\n(a) True\n(b) False\n\n",
    "Bubble gum contains rubber\n(a) True\n(b) False\n\n",

]


def generate_random_questions(questions):
    shuffled_questions = random.sample(questions, len(questions))
    print(shuffled_questions)
    return shuffled_questions


def show_score(score, total_number_of_questions):
    print("You got " + str(score) + "/" + str(total_number_of_questions) + " correct")


def run_test(questions):
    score = 0
    random_questions = generate_random_questions(questions)
    for question in random_questions:
        answer = input(question.getPrompt())
        if answer == question.getAnswer():
            score += 1
    show_score(score, len(questions))


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "a"),
    Question(question_prompts[14], "a"),
]


run_test(questions)

