import cv2
import numpy as np
from pynput.keyboard import Controller

from piclap import *

import os
import sys
sys.path.append(os.path.abspath('.'))


class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 30000

        # Image Window
        self.window_name = 'Yoga Cycle Counter'
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.org = (450, 1400)
        self.fontScale = 40
        self.color = (255, 0, 0)
        self.thickness = 100
        self.cycle = 0

        # Keyboard Controller for Keyboard Inputs
        self.keyboard = Controller()

        # White Background
        self.background = np.full((1920, 3840, 3), 255, dtype=np.uint8)

        # Display 0 Cycles
        image = cv2.putText(self.background, str(self.cycle), self.org, self.font,
                            self.fontScale, self.color, self.thickness, cv2.LINE_AA)
        cv2.imshow(self.window_name, image)
        cv2.waitKey(1)

    def on1Claps(self):

        self.keyboard.press('a')
        self.keyboard.release('a')
        # Increment Cycles
        self.cycle += 1
        print(str(self.cycle))

        # Display Cycle Count
        self.background = cv2.putText(np.full((1920, 3840, 3), 255, dtype=np.uint8), str(self.cycle), self.org, self.font,
                                      self.fontScale, self.color, self.thickness, cv2.LINE_AA)

        cv2.imshow(self.window_name, self.background)

    def on2Claps(self):
        self.keyboard.press('a')
        self.keyboard.release('a')
        # Decrement Cycles
        self.cycle -= 1
        print(str(self.cycle))

        # Display Cycle Count
        self.background = cv2.putText(np.full((1920, 3840, 3), 255, dtype=np.uint8), str(self.cycle), self.org, self.font,
                                      self.fontScale, self.color, self.thickness, cv2.LINE_AA)

        cv2.imshow(self.window_name, self.background)

    def on3Claps(self):
        # Close All Image Windows
        cv2.destroyAllWindows()
        raise KeyboardInterrupt


def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
