import sys, os, traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

try:
    from ui import Ui_MainWindow
except Exception:
    print("Failed importing ui.py:")
    import traceback as _tb
    print(_tb.format_exc())
    raise

def resource_path(relative):
    return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), relative)

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        try:
            self.setupUi(self)
        except Exception:
            tb = traceback.format_exc()
            print("Error in UI setup:\n", tb)
            QMessageBox.critical(None, "UI Error", "Error in UI setup:\n\n" + tb)
            raise

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # load stylesheet
    qss = resource_path("styles.qss")
    if os.path.exists(qss):
        try:
            with open(qss, "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
        except Exception as e:
            print("Failed loading styles.qss:", e)

    try:
        win = MainApp()
        win.setWindowTitle("Smart Notice Board")
        # center window
        screen = app.primaryScreen().availableGeometry()
        w, h = 1280, 780
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2
        win.setGeometry(x, y, w, h)
        win.show()
    except Exception:
        tb = traceback.format_exc()
        print("Startup error:\n", tb)
        QMessageBox.critical(None, "Startup Error", tb)
        sys.exit(1)

    sys.exit(app.exec_())
