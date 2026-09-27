"""
Module 2 — Lesson 3: Loops & Lists
Student: Manganti, Justin Rey A.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A list is like a grocery list that holds multiple items in one place,
A loop is a way to repeat an action automatically for every item on 
that list without typing the same code over and over


============================================
KEY VOCABULARY
============================================
- list:a group of items saved together in square brackets
- for loop:a way to repeat an action for every item in a list
- while loop:a way to keep repeating an action as long as a rule stays true
- index:the position number of an item in a list (always starts at 0)
- iteration:doing one full loop cycle
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
favorite_foods = ["pizza", "tacos", "sushi", "pasta"]

print("my favorite foods:")
for food in favorite_foods:
    print(" - " + food)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
since it starts counting at index 0, the first item in a list is list number 0, not 1, trying to 
access the last item using the total list length , like in my example, there is 4 foods, and trying 
to call or access the pasta which is the last by using the length of the list which is 4 
it will cause an error


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
