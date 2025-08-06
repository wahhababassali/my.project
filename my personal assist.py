#!/usr/bin/env python
# _*_ coding: utf-8 -*-
"""
This code is to print simple
personal assistant
"""
import time
from fileinput import filename
import os
import random

#Putting questions in list to be randomize

name_questions = [
    "What's your full name?: ",
    "Can you tell me your full name, please?: ",
    "How should I address you formally: ",
]

nickname_questions = [
    "What would you like me to call you?: ",
    "Do you have a nickname you prefer?: ",
    "How do your friends usually call you?: ",
]

age_questions = [
    "How old are you?: ",
    "What's your age?: ",
    "May I know your age?: ",
]
place_questions = [
    "Where do you currently live: ",
    "Which city or town do you live in?: ",
    "Where do you call home?: ",
]
school_questions = [
    "What's your highest of education?: ",
    "How far have you gone in school?: ",
    "What's your highest class or degree you have completed?: ",
]

shs_questions = [
    "Can you tell me the name of your shs?: ",
    "Which Senior High School did you attend?: ",
    "Where did you go to SHS?: ",
]

colour_questions = [
    "What colour do you love most?: ",
    "Do you have a favorite colour?: ",
    "What's your favorite color: ",
]

hobby_questions = [
    "What's your favorite Hobby?: ",
    "Tell me something fun you enjoy doing!: ",
    "What do you love doing in your free time?: ",
]

#introduction of the code

print("\nSimple Personal Assistant")
print("=" * 30)
print("Hi there!🙌")
print("I'm your personal assistant, here to learn a\n"
      "little about you so I can help make your\n"
      "experience smarter and more personalised.\n"
      "This will only take a moment\n"
      "ready when you are!😊\n")

#Randomizing the questions above
while True:
    full_name = input(random.choice(name_questions))
    user_name = input(random.choice(nickname_questions))
    user_age = int(input(random.choice(age_questions)))

    if user_age <= 0:
        print("Your age cannot be less than or equal 0")
        break

     

    place = input(random.choice(place_questions))
    school_level = input(random.choice(school_questions))
    shs_level = input(random.choice(shs_questions))
    favorite_colour = input(random.choice(colour_questions))
    hobby = input(random.choice(hobby_questions))

    summary = (f"Hello {user_name}!😊\nIt's a great pleasure to get to know you a little better.\n"
          f"You shared that your full name is {full_name}, and you're {user_age} years old.\n"
          f"You currently live in {place}, and you've reached {school_level} in your education.🧑‍🎓\n"
          f"You also went to {shs_level} for Senior High School, nice!.\n"
          f"\nI love that your favorite color is {favorite_colour} and in your free time you enjoy {hobby}\n"
          f"That's awesome, hobbies are such a great way to unwind.\n"
          f"\nThanks for telling me about yourself!\nI'm here to help however I can, now that i know a bit about you.")

    print("\n")
    print(summary)

    save = input("\nDo you want to save the document(yes/no): ")
    #saving file as .txt
    if save.lower() == "yes":
      filename = f"{user_name}.txt"
      # Rating and saving it to .txt
      while True:
          rating = int(input("Just for fun! How would you like to rate your assistant from 1 to 5 stars⭐?: "))
          if 1 <= rating <= 5:
              stars = "⭐" * rating

              print(f"Thanks for the {stars} rating!")
              break
          else:
              print("Please enter a number between 1 and 5")
      with open(filename, "w", encoding = "utf-8") as file:
        file.write(summary)
        file.write(f"\nAssistant Rating: {stars} ({rating}/5)")

      print(f"\nYour summary has been saved to {user_name}.txt")
      #showing file location
      print(f"Location: {os.path.abspath(filename)}")
    else:
      print("No problem! I won't save anything.")

    restart = input("\nWould you like to restart(yes/no): ")

    if restart == "yes":
        for i in range(1, 4):
         print("Restarting...")
         time.sleep(1)
        print("\n")
        continue
    else:
        print("\nAlright! Thanks for chatting, see you next time!")
        break