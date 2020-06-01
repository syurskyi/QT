class MainData:

    """frame of page data about Pyqt5"""

    def __init__(self):
        self.action=dict()#统一管理action
        self.canvas=dict()#批量创建同类型相同组件的槽函数
        self.control={"QLabel": [], "QTabWidget": [], "QPushButton": [], "QTextEdit": [],
                        "QRadioButton": [], "QComboBox": [], "QSpinBox": [], "QTableWidget": [], "QLCDNumber": [],
                      "Clickable_Lable":[],"QProgressBar":[],"RedBall":[]}

        self.controlData=dict()#自动读取存储的数据，并根据读取的内容调整相关控件的各种参数

    def controlClear(self):
        """
        remove all the controls except menuBar before open a new page
        """
        self.control = {"QLabel": [], "QTabWidget": [], "QPushButton": [], "QTextEdit": [],
                        "QRadioButton": [], "QComboBox": [], "QSpinBox": [], "QTableWidget": [], "QLCDNumber": [],
                        "Clickable_Lable":[],"QProgressBar":[],"RedBall":[]}

    def addFrame(self, imageName):
        """
        add a empty dictionary to record page data
        """
        self.controlData[imageName] = dict()
        self.controlData[imageName]["QRadioButton"] = {"isChecked": []}
        self.controlData[imageName]["QComboBox"] = {"itemText": [], "currentIndex": []}
        self.controlData[imageName]["QSpinBox"] = {"value": []}
        self.controlData[imageName]["QTableWidget"] = {"data": []}
        self.controlData[imageName]["QLCDNumber"] = {"value": []}
        self.controlData[imageName]["save"] = []

    def controlDataClear(self, imageName):
        """
        remove data  before refresh current page
        """
        self.controlData[imageName]["QRadioButton"]["isChecked"] = []
        self.controlData[imageName]["QComboBox"]["itemText"] = []
        self.controlData[imageName]["QComboBox"]["currentIndex"] = []
        self.controlData[imageName]["QSpinBox"]["value"] = []
        self.controlData[imageName]["QTableWidget"]["data"] = []
        self.controlData[imageName]["QLCDNumber"]["value"] = []
        self.controlData[imageName]["save"] = []