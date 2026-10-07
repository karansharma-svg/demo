from PySide6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit,QHBoxLayout,QTabWidget
from PySide6.QtCore import Qt, QTimer,QEvent




# # window.setWindowOpacity(0.90)
# # window.setWindowTitle("My first app")
# # button=QPushButton()
# # button.setText("press me")
# # window.setCentralWidget(button)
# # def butt_clicked():
# #     print("hell yeah!")
# # button.clicked.connect(butt_clicked)

# window.show()
# app.exec()
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app=app
        self.setWindowTitle("not wokring")
        menu_bar=self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu=menu_bar.addMenu("&file")
        quit_action=file_menu.addAction("Quit")
        quit_action.triggered.connect(self.app.quit)
        edit_bar=menu_bar.addMenu("Actions")
        quick_action=edit_bar.addAction("hello")
        uick_action=edit_bar.addAction("ho")
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vasteganahunyiya")
        self.setFixedSize(400, 300) 
        button_hard=QPushButton("Hard")
        button_hard.clicked.connect(self.hard)
        button_soft=QPushButton("soft")
        button_soft.clicked.connect(self.soft)
        button_soft.pressed.connect(self.pressed)
        button_soft.released.connect(self.released)
        layout=QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_soft)
        self.setLayout(layout)
    def soft(self):
          print("clicked")
    def pressed(self):
          print("pressed")
    def released(self):
          print("released")
    def hard(self):
                message=QMessageBox()
                message.setMinimumSize(700,200)
                message.setWindowTitle("This is A WARNING!!")
                message.setText("Something big happened")
                message.setInformativeText("Do soemthing about it ")
                message.setIcon(QMessageBox.Critical)
                message.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                message.setDefaultButton(QMessageBox.Ok)
                ret=message.exec()
                if ret==QMessageBox.StandardButton.Ok:
                       print("User selected OK")
                else:
                       print("User selected cancel")
                
class Widget1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qlite taking input")
        label=QLabel("Full Name: ")
        self.line_edit=QLineEdit()
        button=QPushButton("Grab data")
        self.text_holder_label=QLabel("I am here")
        button.clicked.connect(self.grab_data)
        h_layout=QHBoxLayout()

        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        v_layout=QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        self.setLayout(v_layout)

    
    def grab_data(self):
      text = self.line_edit.text()
      print(text)                          # prints to the terminal/console
      self.text_holder_label.setText(text) 
class Widget5(QWidget):
    def __init__(self):
        super().__init__()
        self.seconds = 5 * 60                      # 1. create the data first

        self.label = QLabel()                      # 2. create the display
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 48px; font-weight: bold;")

        self.timer = QTimer(self)                  # 3. create the timer
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)      # every second → run tick()

        start_btn = QPushButton("Start")           # 4. create the buttons
        stop_btn = QPushButton("Stop")
        reset_btn = QPushButton("Reset")
        start_btn.clicked.connect(self.timer.start)
        stop_btn.clicked.connect(self.timer.stop)
        reset_btn.clicked.connect(self.reset)

        buttons = QHBoxLayout()                    # 5. arrange everything
        buttons.addWidget(start_btn)
        buttons.addWidget(stop_btn)
        buttons.addWidget(reset_btn)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addLayout(buttons)

        self.update_label()                        # 6. show 00:05:00 at start

    def tick(self):                                # runs every second
        if self.seconds > 0:
            self.seconds -= 1
            self.update_label()
        else:
            self.timer.stop()
            self.label.setText("Time's up!")

    def reset(self):
        self.timer.stop()
        self.seconds = 5 * 60
        self.update_label()

    def update_label(self):
        h, rest = divmod(self.seconds, 3600)
        m, s = divmod(rest, 60)
        self.label.setText(f"{h:02}:{m:02}:{s:02}")
class Widget3(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget=QTabWidget(self)
        page=QWidget()
        layout = QVBoxLayout()
        page.setLayout(layout)
        layout.addWidget(QLabel("User Login"))
        layout.addWidget(QLineEdit("Enter info"))
        page2=QWidget()
        layout=QVBoxLayout()
        page2.setLayout(layout)
        layout.addWidget(QLabel("Other details"))
        layout.addWidget(QLineEdit("Your Detail"))
        tab_widget.addTab(page,"My tab")
        tab_widget.addTab(page2,"Your tab")
        tab_widget.addTab(Widget5(), "Timer")
        tab_widget.resize(self.size()) 
        page2.setStyleSheet("#settingsPage { background: #dcfce7; }")
        layout.setContentsMargins(0, 0, 0, 0)
class Widget9(QWidget):
    def __init__(self,app):
         super().__init__()
         self.app=app
         button=QPushButton("Its over")
         layout=QVBoxLayout()
         layout.addWidget(button)
         button.clicked.connect(self.close1)
         self.setLayout(layout)
    def close1(self):
                print(self.isMaximized()) 


            

   

