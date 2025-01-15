import random

def game_of_8_ball():
    answers = ["It is certain, it is decidedely so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes", "most likely", "outlook good", "Yes", "signs point to Yes", "Reply hazy, try again", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again", "don't count on it", "my reply is no", "my sources say no", "outlook not so good", "very doubtful"]

    final_answer = random.choice(answers)

    print(final_answer)
