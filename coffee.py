import urllib.request
import anki_vector
import time

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        page = urllib.request.urlopen("http://localhost:8000/coffee.html/coffee.html.html")
        text = page.read().decode("utf8")
        price = text[1103:1108]
        print(price)
        robot.behavior.say_text(price)
        time.sleep(1)

if __name__ == "__main__":
    main()