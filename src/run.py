
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui import gui

if __name__ == "__main__":
    init = gui.GUI()
    init.run()

