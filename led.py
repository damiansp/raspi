from time import sleep
from gpiozero import LED

DUR = 5

def main():
    red = LED(17)  # gpio pin number
    while True:
        red.on()
        sleep(DUR)
        red.off()
        sleep(DUR)


if __name__ == '__main__':
    main()
