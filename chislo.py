import random

secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Угадайте число (1–100): "))
    attempts += 1
    if guess == secret:
        print(f"Правильно! Количество попыток: {attempts}")
        break
    elif guess < secret:
        print("Слишком мало")
    else:
        print("Слишком много")
