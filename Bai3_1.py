import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


def main(cascaded, block_orientation, rotate):

    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=cascaded,
                     block_orientation=block_orientation, rotate=rotate)
    device.contrast(20)
    # debugging purpose
    print("[-] Matrix initialized")
    # print hello world on the matrix display
    msg = "hello world"
    # debugging purpose
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="white",
                 font=proportional(CP437_FONT), scroll_delay=0.1)


if __name__ == "__main__":
    try:
        main(cascaded=1, block_orientation=-90, rotate=0)
    except KeyboardInterrupt:
        pass
