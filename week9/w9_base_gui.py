from abc import ABC, abstractmethod
from tkinter import *

class BaseGUI(ABC):
    def __init__(self, title, dimension):
        self._create_window(title, dimension)
        self._create_widgets()
    
    def _create_window(self, title, dimension):
        self._window = Tk()
        self._window.title(title)
        self._window.geometry(dimension)

    @abstractmethod
    def _create_widgets(self):
        pass

    def run(self):
        self._window.mainloop()