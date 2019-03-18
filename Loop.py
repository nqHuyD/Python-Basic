# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else:
#     print('Sorry You failed !')
#
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         print("Car started ...")
#         started = True
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             print("Car stopped ...")
#             started = False
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I do not understand")

# for item in 'Python':
#     print(item)

# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)
#
# for item in range(10):
#     print(item)
#
# for item in range(5, 10):
#     print(item)
#
# for item in range(5, 10, 2):
#     print(item)
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
