__author__ = 'joel'
from Calculator import CalTools
from PySide import QtCore, QtGui


class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.resize(300, 300)
        # layouts
        self.main_layout = QtGui.QGridLayout()
        self.edit_line_layout = QtGui.QGridLayout()
        self.button_layout = QtGui.QGridLayout()
        # widgets
        self.label = QtGui.QLabel("Expr:")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_line_layout.addWidget(self.label, 0, 0)
        self.line_edit = QtGui.QLineEdit()
        self.edit_line_layout.addWidget(self.line_edit, 0, 1)
        # buttons
        self.button1 = QtGui.QPushButton("1")
        self.button2 = QtGui.QPushButton("2")
        self.button3 = QtGui.QPushButton("3")
        self.button4 = QtGui.QPushButton("4")
        self.button5 = QtGui.QPushButton("5")
        self.button6 = QtGui.QPushButton("6")
        self.button7 = QtGui.QPushButton("7")
        self.button8 = QtGui.QPushButton("8")
        self.button9 = QtGui.QPushButton("9")
        self.button0 = QtGui.QPushButton("0")
        self.button_plu = QtGui.QPushButton("+")
        self.button_sub = QtGui.QPushButton("-")
        self.button_mut = QtGui.QPushButton("*")
        self.button_div = QtGui.QPushButton("/")
        self.button_lbr = QtGui.QPushButton("(")
        self.button_rbr = QtGui.QPushButton(")")
        self.button_dot = QtGui.QPushButton(".")
        self.button_equ = QtGui.QPushButton("=")
        self.button_back = QtGui.QPushButton("<-")
        self.button_clear = QtGui.QPushButton("C")
        # add buttons to layout
        self.button_layout.addWidget(self.button1, 2, 0)
        self.button_layout.addWidget(self.button2, 2, 1)
        self.button_layout.addWidget(self.button3, 2, 2)
        self.button_layout.addWidget(self.button4, 2, 3)
        self.button_layout.addWidget(self.button5, 3, 0)
        self.button_layout.addWidget(self.button6, 3, 1)
        self.button_layout.addWidget(self.button7, 3, 2)
        self.button_layout.addWidget(self.button8, 3, 3)
        self.button_layout.addWidget(self.button9, 4, 0)
        self.button_layout.addWidget(self.button0, 4, 1)
        self.button_layout.addWidget(self.button_lbr, 4, 2)
        self.button_layout.addWidget(self.button_rbr, 4, 3)
        self.button_layout.addWidget(self.button_mut, 5, 0)
        self.button_layout.addWidget(self.button_div, 5, 1)
        self.button_layout.addWidget(self.button_plu, 5, 2)
        self.button_layout.addWidget(self.button_sub, 5, 3)
        self.button_layout.addWidget(self.button_dot, 6, 0)
        self.button_layout.addWidget(self.button_clear, 6, 1)
        self.button_layout.addWidget(self.button_back, 6, 2)
        self.button_layout.addWidget(self.button_equ, 6, 3)
        # add layouts
        self.main_layout.addLayout(self.edit_line_layout, 0, 0)
        self.main_layout.addLayout(self.button_layout, 1, 0)
        # set layout to window
        self.setLayout(self.main_layout)
        #connect events to functions
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.on_button1_clicked)
        self.connect(self.button2, QtCore.SIGNAL('clicked()'), self.on_button2_clicked)
        self.connect(self.button3, QtCore.SIGNAL('clicked()'), self.on_button3_clicked)
        self.connect(self.button4, QtCore.SIGNAL('clicked()'), self.on_button4_clicked)
        self.connect(self.button5, QtCore.SIGNAL('clicked()'), self.on_button5_clicked)
        self.connect(self.button6, QtCore.SIGNAL('clicked()'), self.on_button6_clicked)
        self.connect(self.button7, QtCore.SIGNAL('clicked()'), self.on_button7_clicked)
        self.connect(self.button8, QtCore.SIGNAL('clicked()'), self.on_button8_clicked)
        self.connect(self.button9, QtCore.SIGNAL('clicked()'), self.on_button9_clicked)
        self.connect(self.button0, QtCore.SIGNAL('clicked()'), self.on_button0_clicked)
        # not numbers
        self.connect(self.button_lbr, QtCore.SIGNAL('clicked()'), self.on_button_lbr_clicked)
        self.connect(self.button_rbr, QtCore.SIGNAL('clicked()'), self.on_button_rbr_clicked)
        self.connect(self.button_mut, QtCore.SIGNAL('clicked()'), self.on_button_mut_clicked)
        self.connect(self.button_div, QtCore.SIGNAL('clicked()'), self.on_button_div_clicked)
        self.connect(self.button_plu, QtCore.SIGNAL('clicked()'), self.on_button_plu_clicked)
        self.connect(self.button_sub, QtCore.SIGNAL('clicked()'), self.on_button_sub_clicked)
        self.connect(self.button_dot, QtCore.SIGNAL('clicked()'), self.on_button_dot_clicked)
        self.connect(self.button_clear, QtCore.SIGNAL('clicked()'), self.on_button_clear_clicked)
        self.connect(self.button_back, QtCore.SIGNAL('clicked()'), self.on_button_back_clicked)
        self.connect(self.button_equ, QtCore.SIGNAL('clicked()'), self.on_button_equ_clicked)
        self.error_str = "Error"
        self.nan_str = "NaN"

    # check whether error occurs, if so clear edit line
    def check_error(self):
        if self.error_str == self.line_edit.text() or self.nan_str == self.line_edit.text():
            self.line_edit.setText("")

    def on_button1_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "1")

    def on_button2_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "2")

    def on_button3_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "3")

    def on_button4_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "4")

    def on_button5_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "5")

    def on_button6_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "6")

    def on_button7_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "7")

    def on_button8_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "8")

    def on_button9_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "9")

    def on_button0_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "0")

    def on_button_lbr_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "(")

    def on_button_rbr_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + ")")

    def on_button_mut_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "*")

    def on_button_div_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "/")

    def on_button_plu_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "+")

    def on_button_sub_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + "-")

    def on_button_clear_clicked(self):
        self.line_edit.setText("")

    def on_button_back_clicked(self):
        text = self.line_edit.text()
        if len(text) > 0:
            self.line_edit.setText(text[0:len(text)-1])

    def on_button_dot_clicked(self):
        self.check_error()
        self.line_edit.setText(self.line_edit.text() + ".")

    def on_button_equ_clicked(self):
        # calculate begin...
        cal_str = self.line_edit.text()  # get string from edit line
        cal_str = CalTools.str_filter(cal_str)  # filter string
        prefix_stack = CalTools.get_calculator_stack(cal_str)  # create a prefix stack
        # print some logs
        print "cal str:", cal_str
        print "prefix stack:"
        CalTools.print_calculator_stack(prefix_stack)
        # make prefix to suffix
        suffix_stack = CalTools.prefix_to_suffix(prefix_stack)
        if None == suffix_stack:
            self.line_edit.setText(self.error_str)
            print self.error_str
            return
        print "suffix stack:"
        CalTools.print_calculator_stack(suffix_stack)
        # calculate suffix
        result_str = CalTools.calculate_from_stack(suffix_stack)
        print "---calculator result---"
        print result_str
        if result_str == self.error_str:
            self.line_edit.setText(self.error_str)
            return
        else:
            self.line_edit.setText(result_str)

