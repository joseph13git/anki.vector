import anki_vector
import time
from random import randint


def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        secret = randint(1,10)
        print("Welcome!")
        robot.behavior.say_text("Welcome")
        time.sleep(1)
        guess = 0
        while guess!=secret:
            robot.behavior.say_text("Guess the number")
            g = input("Guess the number: ")
            guess = int(g)
            time.sleep(1)
            if guess == secret:
                print("You win!")
                robot.behavior.say_text("You win")
                time.sleep(1)
            else:
                if guess > secret:
                    print("Too high")
                    robot.behavior.say_text("Too high")
                else:
                    print("Too low")
                    robot.behavior.say_text("Too low")
                time.sleep(1)
        print("Game over!")
        robot.behavior.say_text("Game over")
        time.sleep(1)


if __name__ == "__main__":
    main()