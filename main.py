# print("meaaaaaaaaaaw")
# print("meaaaaaaaaaaw")
# print("meaaaaaaaaaaw")

# i = 0
# while i < 3:
#     print("meaaaaaaaaw")
#     i += 1

# for i in [0, 1, 2]:
#     print("meaaaaaaaw")

# for i in range(3):
#     print("meaaaaaaaaw")

# for _ in range(3):
#     print("meaaaaaaaaw")

# print("meaaaaaaaaw" * 3)

# print("meaaaaaaaaaw\n" * 3, end="")

# while True:
#     n = int(input("what is your n? "))
#     if n < 0:
#         continue 
#     else:
#        break

# while True:
#     n = int(input("What is your n? "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meaaaaaaaw")

# def main():
#     meaw(get_number())

# def get_number():
#     while True:
#         n = int(input("what is your n? "))
#         if n > 0:
#             break
#     return n

# def meaw(n):
#     for _ in range(n):
#         print("meaaaaaaaaw")

# main()

# students = ["Hermione", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")

# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")

# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     print_raw(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# def print_row(width):
#     print("?" * width)
# # main()

# # def main():
# #     print_square(5)

# # def print_square(size):
# #     for i in range(size):
# #         for j in range(size):
# #             print("#", end="")
# #         print()

# # main()

# def main():
#     print_square(5)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# main()

# import random

# # coin = random.choice(["heads", "tails"])
# # print(coin)

# cards = ["jack", "king", "qween"]

# random.shuffle(cards)

# print(cards)

# import statistics

# print(statistics.mean([100, 90]))

# import sys

# try:
#     if (len(sys.argv) < 2):
#         print("Error: too few arguments")
#     if (len(sys.argv) > 2):
#         print("Erro: too many arguments")

#     print("My name is: ", sys.argv[1])

# except IndexError:
#     pass

# if (len(sys.argv) < 2):
#     sys.exit("Error: too few arguments")
# if (len(sys.argv) > 2):
#     sys.exit("Erro: too many arguments")

# print("My name is: ", sys.argv[1])


# import requests
# import sys
# import json

# # if len(sys.argv) != 2:
# #     sys.exit()

# # response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# # print(response.json())

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

# o = response.json()

# for result in o["results"]:
#     print(result["trackName"])


# name = input("What's your name?" )
# print(f"hello, {name}")

# names = []

# for _ in range(3):
#     name = input("What's your name?" )
#     names.append(name)
    
# for name in sorted(names):
#     print(name)

# name = input("what is your name? ")
# file = open("test.txt", "a")
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line)

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line)


import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
