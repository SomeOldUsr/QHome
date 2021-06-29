from PyQt5 import QtWidgets, uic, QtCore
from datetime import datetime
import sys
# import OpenGL.GL as gl
# import OpenGL.GLU as glu
# import OpenGL.GLUT as glut


class KlingelWindow(QtWidgets.QMainWindow):
    """
    Klingel Window
    """
    # type hints for the IDE
    comboBox: QtWidgets.QComboBox
    horizontalSlider: QtWidgets.QSlider
    durchsageButton: QtWidgets.QPushButton
    tuerButton: QtWidgets.QPushButton
    lcdNumber: QtWidgets.QLCDNumber
    openGLWidget: QtWidgets.QOpenGLWidget

    def __init__(self, path):
        super(KlingelWindow, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi(path, self)  # Load the .ui file

        # creating additional objects
        self.timer = QtCore.QTimer(self)

        # adding events
        self.durchsageButton.clicked.connect(self.durchsage_click)
        self.tuerButton.clicked.connect(self.tuer_click)
        self.timer.timeout.connect(self.next_minute)

        self._setup()

    ##########
    # EVENTS
    ##########

    # Button
    def durchsage_click(self):
        """
        click event for durchsageButton
        :return:
        """
        QtWidgets.QMessageBox(text=self.sender().text()).exec()

    def tuer_click(self):
        """
        click event for tuerButton
        :return:
        """
        QtWidgets.QMessageBox(text=self.sender().text()).exec()

    # Timer
    def next_minute(self):
        """
        timeout event for timer object
        increments minute
        :return:
        """
        self.lcdNumber.display(datetime.now().strftime('%H:%M'))

    ###########
    # HELPER
    ###########

    # init
    def _setup(self):
        self._init_timer()

        self.show()

    def _init_timer(self):
        """
        initializes the timer once a time with 0.000 seconds is reached,
        in order for the clock to be synchronized
        """
        self.next_minute()
        milliseconds = 1000 - datetime.now().microsecond // 1000
        seconds = 60 - datetime.now().second
        QtCore.QTimer.singleShot(seconds * 1000 + milliseconds, lambda: (self.next_minute(), self.timer.start(60_000)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = KlingelWindow('UI/Klingel.ui')
    app.exec()

    '''
    I Don't know what any of this does

    def setupUI(self):
        print("\033[1;101m SETU6P UI \033[0m")
        self.windowsHeight = self.openGLWidget.height()
        self.windowsWidth = self.openGLWidget.width()

        self.openGLWidget.initializeGL()
        self.openGLWidget.resizeGL(self.windowsWidth, self.windowsHeight)
        self.openGLWidget.paintGL = self.paintGL
        self.openGLWidget.initializeGL = self.initializeGL

    def paintGL(self):
        self.loadScene()
        glut.glutWireSphere(2, 13, 13)

    def initializeGL(self):
        print("\033[4;30;102m INITIALIZE GL \033[0m")
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        gl.glEnable(gl.GL_DEPTH_TEST)

    def loadScene(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        x, y, width, height = gl.glGetDoublev(gl.GL_VIEWPORT)
        glu.gluPerspective(
            45,  # field of view in degrees
            width / float(height or 1),  # aspect ratio
            .25,  # near clipping plane
            200,  # far clipping plane
        )

        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        glu.gluLookAt(12, 12, 12, 0, 0, 0, 0, 1, 0)
    '''