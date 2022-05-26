from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer, QUrl, Qt
from PyQt5 import QtGui
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


from timer_bg import Ui_timer_bg
from circular_progress import CircularProgress

class timerWidget(QWidget, Ui_timer_bg):
    started = False 
    onPaused = False
    count = 0
    slider_value = 0

    def __init__(self):
        super().__init__()
        self.widget = Ui_timer_bg()
        self.widget.setupUi(self)
        style = "stylesheets/timer_stylesheet.css"
        with open(style, "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        
        # Sound component 
        self.title = "crystal-logo.mp3"
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.title)))

        # Timer buttons 
        self.widget.stop_timer_button.clicked.connect(self.stop_timer_func)
        self.widget.start_stop_timer_button.clicked.connect(self.start_timer)

        # Timer component 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_timer)

        # Slider component 
        self.widget.set_timer_duration_bar.setMaximum(7200)
        self.widget.set_timer_duration_bar.valueChanged.connect(self.slider_value) 

        # Circular progressbar component 
        self.circ_prog = CircularProgress()
        self.circ_prog.width = 230
        self.circ_prog.height = 230
        self.circ_prog.setMinimumSize(self.circ_prog.width, self.circ_prog.height)
        self.circ_prog.progress_color = "#c5dedd"
        self.circ_prog.text_color = "#c5dedd"
        self.circ_prog.font_size = 30
        self.widget.timer_layout.addWidget(self.circ_prog, Qt.AlignCenter, Qt.AlignCenter)



    def slider_value(self):
        self.slider_value = self.widget.set_timer_duration_bar.value() 
        self.count = self.slider_value
        self.change_timer_display(self.slider_value)
        # self.show_time(self.slider_value*1000)
        # self.circ_prog.max_value = self.slider_value
        # self.circ_prog.set_value(self.slider_value)


    # Will stop and reset the timer 
    def stop_timer_func(self):
        self.onPaused = False 
        self.started = False
        self.timer.stop()
        self.count = self.slider_value
        self.change_timer_display(self.slider_value)
        # self.show_time(self.slider_value*1000)
        # self.circ_prog.max_value = self.slider_value
        # self.circ_prog.set_value(self.slider_value)
        self.widget.stop_timer_button.setDisabled(True)
        self.widget.start_stop_timer_button.setIcon(QtGui.QIcon(":/icons/icons/play.svg"))
        self.widget.start_stop_timer_button.setText("Start countdown")


    # Will stop and reset timer to initial. On press when running will also reset timer. 
    def start_timer(self):
        # If timer is NOT already running 
        if not self.started:
            self.started = True
            self.timer.start(1000)
            self.widget.start_stop_timer_button.setIcon(QtGui.QIcon(":/icons/icons/pause.svg"))
            self.widget.start_stop_timer_button.setText("Pause countdown")
            self.widget.stop_timer_button.setDisabled(False)
        # If timer is running, but already on pause 
        elif self.onPaused:
            self.onPaused = False 
            self.widget.stop_timer_button.setDisabled(False)
            self.widget.start_stop_timer_button.setIcon(QtGui.QIcon(":/icons/icons/pause.svg"))
            self.widget.start_stop_timer_button.setText("Pause countdown")
            self.timer.start(1000)
        elif not self.onPaused:
            self.onPaused = True 
            self.widget.start_stop_timer_button.setIcon(QtGui.QIcon(":/icons/icons/play.svg"))
            self.widget.start_stop_timer_button.setText("Resume countdown")
            self.widget.stop_timer_button.setDisabled(False)
            self.timer.stop()

         

    def run_timer(self):
        self.timer.start(1000)
        # When the timer has started, display and maintain continous countdown
        if self.count > 0:
            self.count -= 1
            self.circ_prog.set_value(self.count)
            self.show_time(self.count * 1000)
        # If time is up 
        elif self.count == 0:
            self.timer.stop()
            self.started = False
            self.change_timer_display(self.slider_value)
            self.count = self.slider_value
            self.widget.start_stop_timer_button.setIcon(QtGui.QIcon(":/icons/icons/play.svg"))
            self.widget.start_stop_timer_button.setText("Start")
            self.widget.stop_timer_button.setDisabled(True)
            # Play sound when time's up
            self.player.play()

        else:
            pass


    def show_time(self, millis):
        seconds=(millis/1000)%60
        seconds = int(seconds)
        minutes=(millis/(1000*60))%60
        minutes = int(minutes)
        hours=(millis/(1000*60*60))%24  
        self.circ_prog.value_text = ("%d:%d:%d" % (hours, minutes, seconds))


    def change_timer_display(self,slider_value):
        self.show_time(slider_value*1000)
        self.circ_prog.max_value =slider_value
        self.circ_prog.set_value(slider_value)


"""
Credits:
Music by SergeQuadrado from Pixabay

"""