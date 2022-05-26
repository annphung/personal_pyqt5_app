from multiprocessing.sharedctypes import Value
import sys, os
from turtle import width 
from PyQt5.QtCore import* 
from PyQt5.QtGui import* 
from PyQt5.QtWidgets import* 

class CircularProgress(QWidget):
    def __init__(self):
     super().__init__()


    # Properties that defines the look of the progressbar
     self.width = 200 
     self.height = 200 
     self.progress_width = 10 
     self.progress_rounded_cap = True 
     self.progress_color = 0x0069B6 
     self.max_value = 7200
     self.value = 7200
     self.font_size = 12 
     self.suffix = ""
     self.text_color = 0x0069B6
     self.font_family = "Arial"
     self.value_text = "0:0:0"
     #self.enable_shadow = True
     # Attributes to set default size, in case it is not hosted inside a layout
     self.resize (self.width, self.height)

    def set_value(self, value):
        self.value = value
        self.repaint()                                              # re-render when value changed


    # Using imported class PaintEvent to design the bar, standard QT event 
    def paintEvent(self, event):
        # Progressbar parameters
        width = self.width - self.progress_width                    # Width = width of widget line - width og progress bar
        height = self.height - self.progress_width
        margin = self.progress_width/2                              # dynamically compensating the position on our widget
        if self.value == 0:
            value = 0
        else:
            value = self.value * 360/self.max_value                     
        
        # Creating an instance that lets us create art 
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)                  # Smoothing out the edges of the bar
        paint.setFont(QFont(self.font_family, self.font_size))      # function to change font size of the widget

        # Create a rectangle that contains the same width 
        rect = QRect(0,0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # Using a pen, responsible for the color, style and width of the bar
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Creating the circular bar
        paint.setPen(pen)
        paint.drawArc(int(margin), int(margin), int(width), height, -90 * 16, int(-value * 16))          # 360 degree angle in Qt arc is represented by 5760. 

        # Creating the text 
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value_text}{self.suffix}")
        

        # Close the paint 
        paint.end()