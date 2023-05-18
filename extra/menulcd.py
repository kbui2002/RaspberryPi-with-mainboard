# import
import RPi.GPIO as GPIO
import time
import socket
# Define GPIO to LCD mapping
LCD_RS = 23
LCD_E = 27
LCD_D4 = 18
LCD_D5 = 17
LCD_D6 = 14
LCD_D7 = 3
LED_ON = 2
# Define some device constants
LCD_WIDTH = 16  # Max char
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # 1 LCD RAM add
LCD_LINE_2 = 0xC0  # 2 LCD RAM add
# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005
BT1 = 21
BT2 = 26
BT3 = 20
demmenu = 0


def lcd_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_D4, GPIO.OUT)
    GPIO.setup(LCD_D5, GPIO.OUT)
    GPIO.setup(LCD_D6, GPIO.OUT)
    GPIO.setup(LCD_D7, GPIO.OUT)
    GPIO.setup(LED_ON, GPIO.OUT)
    # Initialise display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)


def lcd_string(message, line):
    message = message.rjust(len(message))
    if line == 1:
        lcd_byte(LCD_LINE_1, False)
    else:
        lcd_byte(LCD_LINE_2, False)
    for i in range(len(message)):
        lcd_byte(ord(message[i]), LCD_CHR)


def lcd_clear():
    lcd_string("                ", 1)
    lcd_string("                ", 2)


def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True for character
    #       False for command
    GPIO.output(LCD_RS, mode)  # RS
    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)
    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)
    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)
    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)


def menucapnhat():
    if (demmenu == 0):
        lcd_clear()
        lcd_string(">Xem IP", 1)
        lcd_string(" MENU 2", 2)
    elif (demmenu == 1):
        lcd_clear()
        lcd_string(" Xem IP", 1)
        lcd_string(">MENU 2", 2)
    elif (demmenu == 2):
        lcd_clear()
        lcd_string(">MENU 3", 1)
        lcd_string(" MENU 4", 2)
    elif (demmenu == 3):
        lcd_clear()
        lcd_string(" MENU 3", 1)
        lcd_string(">MENU 4", 2)


def get_ip_address():
    ip_address = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


def chonmenu():
    match(demmenu):
        case 0:
            lcd_clear()
            lcd_string("DIA CHI IP", 1)
            lcd_string(get_ip_address(), 2)
            time.sleep(3)
        case 1:
            lcd_clear()
            lcd_string("MENU 2", 1)
            lcd_string("NOI DUNG MENU 2.", 2)
            time.sleep(3)
        case 2:
            lcd_clear()
            lcd_string("MENU 3", 1)
            lcd_string("NOI DUNG MENU 3.", 2)
            time.sleep(3)
        case 3:
            lcd_clear()
            lcd_string("MENU 4", 1)
            lcd_string("NOI DUNG MENU 4.", 2)
            time.sleep(3)


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    lcd_init()
    time.sleep(1)
    lcd_clear()
    GPIO.output(LED_ON, True)
    time.sleep(1)

    while True:

        if (GPIO.input(BT1) == 0):
            if (demmenu >= 3):
                demmenu = 0
            else:
                demmenu += 1
                menucapnhat()
            time.sleep(3)

        if (GPIO.input(BT2) == 0):
            if (demmenu <= 0):
                demmenu = 3
            else:
                demmenu -= 1
            menucapnhat()
            time.sleep(3)

        if (GPIO.input(BT3) == 0):
            chonmenu()
            menucapnhat()
            time.sleep(3)


main()
