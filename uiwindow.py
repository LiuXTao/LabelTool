'''
@File     : fileOpen.py
@Copyright: 
@author   : lxt
@Date     : 2020/8/29
@Desc     :
'''

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QTextEdit,QVBoxLayout,QPushButton, QRadioButton,QButtonGroup, QLabel, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon

class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setWindowTitle('QLineEdit例子')
        self.emotion_list = ['气愤', '担心', '厌恶', '相信', '开心', '惊喜', '期待', '伤心', '无']
        self.radio_list = ["1", "-1", "0"]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("标注工具")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionfileopen = QtWidgets.QAction(MainWindow)
        self.actionfileopen.setObjectName("actionfileopen")
        self.menufile.addAction(self.actionfileopen)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 初始化主界面
        self.initMain()

    def initMain(self):
        font = QtGui.QFont()
        font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        font.setPointSize(13)  # 括号里的数字可以设置成自己想要的字体大小
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.top_layout = QHBoxLayout()
        self.top_widget = QWidget()
        self.top_layout.addWidget(self.top_widget)

        # self.pre_btn = QPushButton("上一条")
        self.curr_label = QLabel("")
        self.curr_label.setFont(font)
        # self.next_btn = QPushButton("下一条")
        self.file_path = QLabel("")
        self.top_layout.addWidget(self.curr_label, 1, QtCore.Qt.AlignLeft)
        self.top_layout.addWidget(self.file_path, 4, QtCore.Qt.AlignRight)
        # self.top_layout.addWidget(self.next_btn, 1, QtCore.Qt.AlignRight)


        self.body_widget = QWidget()  # 创建窗口主部件
        self.body_layout = QHBoxLayout()  # 创建主部件的布局
        self.body_layout.addWidget(self.body_widget)

        self.main_layout.addLayout(self.top_layout, stretch=1)
        self.main_layout.addLayout(self.body_layout, stretch=10)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QVBoxLayout()  # 创建左侧部件的网格布局
        self.right_widget = QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QVBoxLayout()  # 创建右侧部件的网格布局

        self.left_layout.addWidget(self.left_widget)
        self.right_layout.addWidget(self.right_widget)

        self.body_layout.addLayout(self.left_layout, stretch=5)
        self.body_layout.addLayout(self.right_layout, stretch=2)

        self.content_label = QLabel("原文内容：")
        self.content_text = QTextEdit()  # 创建文本框用于显示
        self.content_text.setReadOnly(True)

        self.comment_label = QLabel("评论内容：")
        self.comment_text = QTextEdit()  # 创建文本框用于显示
        self.comment_text.setReadOnly(True)
        font.setPointSize(12)
        self.content_text.setFont(font)
        self.comment_text.setFont(font)

        self.left_layout.addWidget(self.content_label, stretch=1)
        self.left_layout.addWidget(self.content_text, stretch=10)
        self.left_layout.addWidget(self.comment_label, stretch=1)
        self.left_layout.addWidget(self.comment_text, stretch=5)

        font.setBold(True)
        font.setPointSize(12)
        self.label1 = QLabel("反讽：")
        self.label2 = QLabel("比喻：")
        self.label3 = QLabel("夸张：")
        self.label4 = QLabel("谐音：")
        self.label5 = QLabel("象征：")
        self.label6 = QLabel("情感：")  # 用下拉列表
        self.label7 = QLabel("态度：")
        self.label8 = QLabel("其余潜台词：")
        self.label1.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)
        self.label4.setFont(font)
        self.label5.setFont(font)
        self.label6.setFont(font)
        self.label7.setFont(font)
        self.label8.setFont(font)

        self.radio11 = QRadioButton("有")
        self.radio12 = QRadioButton("没有")
        self.radio13 = QRadioButton("不确定")
        # self.radio11.setChecked(True)
        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.radio11, 0)
        self.bg1.addButton(self.radio12, 1)
        self.bg1.addButton(self.radio13, 2)
        self.layout11 = QHBoxLayout()
        self.layout11.addWidget(self.label1)
        self.layout11.addWidget(self.radio11)
        self.layout11.addWidget(self.radio12)
        self.layout11.addWidget(self.radio13)

        self.inputtext_1 = QLineEdit()
        self.inputtext_1.setPlaceholderText("反讽语句")
        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.inputtext_1, stretch=4)

        self.radio21 = QRadioButton("有")
        self.radio22 = QRadioButton("没有")
        self.radio23 = QRadioButton("不确定")
        # self.radio21.setChecked(True)
        self.bg2 = QButtonGroup(self)
        self.bg2.addButton(self.radio21, 0)
        self.bg2.addButton(self.radio22, 1)
        self.bg2.addButton(self.radio23, 2)
        self.layout21 = QHBoxLayout()
        self.layout21.addWidget(self.label2)
        self.layout21.addWidget(self.radio21)
        self.layout21.addWidget(self.radio22)
        self.layout21.addWidget(self.radio23)

        self.inputtext_21 = QLineEdit()
        self.inputtext_22 = QLineEdit()
        self.inputtext_21.setPlaceholderText("喻体")
        self.inputtext_22.setPlaceholderText("本体")
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.inputtext_21, stretch=2)
        self.layout2.addWidget(self.inputtext_22, stretch=2)

        self.radio31 = QRadioButton("有")
        self.radio32 = QRadioButton("没有")
        self.radio33 = QRadioButton("不确定")
        # self.radio31.setChecked(True)
        self.bg3 = QButtonGroup(self)
        self.bg3.addButton(self.radio31, 0)
        self.bg3.addButton(self.radio32, 1)
        self.bg3.addButton(self.radio33, 2)
        self.layout31 = QHBoxLayout()
        self.layout31.addWidget(self.label3)
        self.layout31.addWidget(self.radio31)
        self.layout31.addWidget(self.radio32)
        self.layout31.addWidget(self.radio33)
        self.inputtext_3 = QLineEdit()
        self.inputtext_3.setPlaceholderText("夸张语句")
        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.inputtext_3, stretch=4)

        self.radio41 = QRadioButton("有")
        self.radio42 = QRadioButton("没有")
        self.radio43 = QRadioButton("不确定")
        # self.radio41.setChecked(True)
        self.bg4 = QButtonGroup(self)
        self.bg4.addButton(self.radio41, 0)
        self.bg4.addButton(self.radio42, 1)
        self.bg4.addButton(self.radio43, 2)
        self.layout41 = QHBoxLayout()
        self.layout41.addWidget(self.label4)
        self.layout41.addWidget(self.radio41)
        self.layout41.addWidget(self.radio42)
        self.layout41.addWidget(self.radio43)
        self.inputtext_41 = QLineEdit()
        self.inputtext_42 = QLineEdit()
        self.inputtext_41.setPlaceholderText("谐音内容")
        self.inputtext_42.setPlaceholderText("正确内容")
        self.layout4 = QHBoxLayout()
        self.layout4.addWidget(self.inputtext_41, stretch=2)
        self.layout4.addWidget(self.inputtext_42, stretch=2)

        self.radio51 = QRadioButton("有")
        self.radio52 = QRadioButton("没有")
        self.radio53 = QRadioButton("不确定")
        # self.radio51.setChecked(True)
        self.bg5 = QButtonGroup(self)
        self.bg5.addButton(self.radio51, 0)
        self.bg5.addButton(self.radio52, 1)
        self.bg5.addButton(self.radio53, 2)
        self.layout51 = QHBoxLayout()
        self.layout51.addWidget(self.label5)
        self.layout51.addWidget(self.radio51)
        self.layout51.addWidget(self.radio52)
        self.layout51.addWidget(self.radio53)
        self.inputtext_51 = QLineEdit()
        self.inputtext_52 = QLineEdit()
        self.inputtext_51.setPlaceholderText("象征内容")
        self.inputtext_52.setPlaceholderText("真正内容")
        self.layout5 = QHBoxLayout()
        self.layout5.addWidget(self.inputtext_51, stretch=2)
        self.layout5.addWidget(self.inputtext_52, stretch=2)

        # 实例化QComBox对象
        self.cb_6 = QComboBox(self)
        self.cb_6.addItems(self.emotion_list)
        self.layout6 = QHBoxLayout()
        self.layout6.addWidget(self.cb_6, stretch=1)

        self.radio71 = QRadioButton("积极")
        self.radio72 = QRadioButton("消极")
        self.radio73 = QRadioButton("不确定")
        # self.radio71.setChecked(True)
        self.bg7 = QButtonGroup(self)
        self.bg7.addButton(self.radio71, 0)
        self.bg7.addButton(self.radio72, 1)
        self.bg7.addButton(self.radio73, 2)
        self.input_7 = QLineEdit()
        self.input_7.setPlaceholderText("态度信息")

        self.layout7 = QHBoxLayout()
        self.layout7.addWidget(self.radio71)
        self.layout7.addWidget(self.radio72)
        self.layout7.addWidget(self.radio73)

        self.input_8 = QLineEdit()
        self.input_8.setPlaceholderText("其他潜台词信息")
        self.layout8 = QHBoxLayout()
        font.setPointSize(14)
        font.setBold(False)
        self.save_btn = QPushButton("保存")
        self.next_btn = QPushButton("下一条")
        self.save_btn.setFont(font)
        self.next_btn.setFont(font)
        self.layout8.addWidget(self.save_btn, stretch=1)
        self.layout8.addWidget(self.next_btn, stretch=1)


        self.right_layout.addLayout(self.layout11)
        self.right_layout.addLayout(self.layout1)
        self.right_layout.addLayout(self.layout21)
        self.right_layout.addLayout(self.layout2)
        self.right_layout.addLayout(self.layout31)
        self.right_layout.addLayout(self.layout3)
        self.right_layout.addLayout(self.layout41)
        self.right_layout.addLayout(self.layout4)
        self.right_layout.addLayout(self.layout51)
        self.right_layout.addLayout(self.layout5)
        self.right_layout.addWidget(self.label6)
        self.right_layout.addLayout(self.layout6)
        self.right_layout.addWidget(self.label7)
        self.right_layout.addLayout(self.layout7)
        self.right_layout.addWidget(self.label8)
        self.right_layout.addWidget(self.input_8)
        self.right_layout.addLayout(self.layout8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "文件"))
        self.actionfileopen.setText(_translate("MainWindow", "打开文件..."))

    def _cleanText(self):
        self.inputtext_1.setText("")
        self.inputtext_21.setText("")
        self.inputtext_22.setText("")
        self.inputtext_3.setText("")
        self.inputtext_41.setText("")
        self.inputtext_42.setText("")
        self.inputtext_51.setText("")
        self.inputtext_52.setText("")
        self.input_8.setText("")
        self.cb_6.setCurrentIndex(0)
        # self.radio11.setChecked(True)
        # self.radio21.setChecked(True)
        # self.radio31.setChecked(True)
        # self.radio41.setChecked(True)
        # self.radio51.setChecked(True)
        # self.radio71.setChecked(True)

