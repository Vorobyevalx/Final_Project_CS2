from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox
from GradeCalcGui import Ui_MainWindow


def get_best_score(scores):
    return max(scores)


def get_grade(score, best_score):
    if score >= best_score - 10:
        return "A"
    elif score >= best_score - 20:
        return "B"
    elif score >= best_score - 30:
        return "C"
    elif score >= best_score - 40:
        return "D"
    else:
        return "F"


class GradeCalcMain(QMainWindow):
    def __init__(self):
        super().__init__()

        # create an instance of the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize the number of students to 0
        self.num_students = 0

        self.ui.calc_btn.clicked.connect(self.calculate_grades)
        self.ui.add_student.clicked.connect(self.add_line_edit)

    def calculate_grades(self):

        # Get the total number of students from the line edit
        num_students = self.ui.gridLayout.count() // 2  # divide by 2 because there is a label for each line edit

        # Get the scores from the line edits and store them in a list
        scores = []
        for i in range(1, self.ui.gridLayout.count()):
            widget = self.ui.gridLayout.itemAt(i).widget()
            if isinstance(widget, QLineEdit):
                scores.append(int(widget.text()))

        # Calculate the best score and the grades for each student
        best_score = get_best_score(scores)
        for i in range(num_students):
            grade = get_grade(scores[i], best_score)
            print(grade)

    def add_line_edit(self):
        line_edit = QLineEdit()
        object_name = f"student_{self.num_students}_score"
        line_edit.setObjectName(object_name)
        label = QLabel(f"Enter Student {self.num_students} Grade")
        self.ui.gridLayout.addWidget(label)
        self.ui.gridLayout.addWidget(line_edit)
        self.num_students += 1
        print(f"Added line edit with object name: {line_edit.objectName()}")


if __name__ == "__main__":
    app = QApplication([])
    window = GradeCalcMain()
    window.show()
    app.exec_()