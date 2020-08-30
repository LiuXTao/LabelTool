'''
@File     : main.py
@Copyright: 
@author   : lxt
@Date     : 2020/8/29
@Desc     :
'''
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from uiwindow import Ui_MainWindow
import sys
import os
import pandas as pd

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icon/icon.ico'))
        self.setWindowTitle("标注小民工")
        self.data = None
        self.data_index = None
        self.totalindex = 0
        self.fileName = ""
        self.emotion_value = self.emotion_list[0]
        self.sarcasm = self.radio_list[0]
        self.metaphor = self.radio_list[0]
        self.exaggeration = self.radio_list[0]
        self.homophonic = self.radio_list[0]
        self.symbolism = self.radio_list[0]
        self.sentiment = self.radio_list[0]
        self.save_curr_flag = False
        # add action
        self.actionfileopen.triggered.connect(self._openFile)
        self.cb_6.currentIndexChanged[str].connect(self._selectEmotion)
        self.save_btn.clicked.connect(self._saveData)
        self.next_btn.clicked.connect(self._clickNext)
        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bg2.buttonClicked.connect(self.rbclicked)
        self.bg3.buttonClicked.connect(self.rbclicked)
        self.bg4.buttonClicked.connect(self.rbclicked)
        self.bg5.buttonClicked.connect(self.rbclicked)
        self.bg7.buttonClicked.connect(self.rbclicked)

    def _openFile(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件", os.getcwd(),
                                                                   "All Files(*);;Text Files(*.csv)")
        self._reset()
        self.fileName = fileName
        self._loadFile(fileName)
        self._showData()

    def _reset(self):
        self.data = None
        self.data_index = None
        self.totalindex = 0
        self.fileName = ""
        self.save_curr_flag = False
        self._resetSelection()

    def _resetSelection(self):
        self.emotion_value = self.emotion_list[0]
        self.sarcasm = self.radio_list[0]
        self.metaphor = self.radio_list[0]
        self.exaggeration = self.radio_list[0]
        self.homophonic = self.radio_list[0]
        self.symbolism = self.radio_list[0]
        self.sentiment = self.radio_list[0]
        self._cleanText()


    def _selectEmotion(self, i):
        self.emotion_value = i

    def _loadFile(self, file_path):
        self.data = pd.read_csv(file_path, encoding='utf-8')
        self.data_index = self.data.index
        print(len(self.data_index))
        print(self.data.shape)


    def _showData(self):
        nums = self.data.shape[0]
        for i in range(self.totalindex, nums):
            df = self.data.iloc[i]
            f1, f2, f3, f4, f5, f6, f7, f8 = df['sarcasm'], df['metaphor'], df['exaggeration'], df['homophonic'], df['symbolism'], df['emotion'], df['sentiment'], df['other_subtext']
            if pd.isnull(f1) or pd.isnull(f2) or pd.isnull(f3) or pd.isnull(f4) or pd.isnull(f5) or pd.isnull(f7) or pd.isnull(f8):
                if 'question' not in self.data.columns:
                    self.comment_text.setText(str(df['comment']))
                    self.content_text.setText("{}".format(df['content']))
                else:
                    self.comment_text.setText(str(df['comment']))
                    self.content_text.setText("{}\n{}".format(df['question'], df['content']))
                self.totalindex = i
                self._setLabel()
                break
            else:
                continue

    def _showPrev(self):
        df = self.data.iloc[self.totalindex]
        if 'question' not in self.data.columns:
            self.comment_text.setText(str(df['comment']))
            self.content_text.setText("{}".format(df['content']))
        else:
            self.comment_text.setText(str(df['comment']))
            self.content_text.setText("{}\n{}".format(df['question'], df['content']))
        self._setLabel()

    def _clickNext(self):
        flag = self._saveData()
        if flag == True:
            self.totalindex += 1
            self._showData()
            self._resetSelection()
            self.save_curr_flag = False
            if self.totalindex % 10 == 0:
                self._saveToFile()

    def _show_message(self, message):
        QtWidgets.QMessageBox.information(self, "信息提示框", message, QtWidgets.QMessageBox.Yes)

    def _setLabel(self):
        self.curr_label.setText("当前条:{}".format(self.totalindex))

    def _saveData(self):
        if self.data is None:
            self._show_message(message="请选择并打开文件")
            return False
        if self.save_curr_flag == True:
            return True
        l1, sent1 = self.sarcasm, self.inputtext_1.text()
        f1, data1 = self._constructor(l1, sents=sent1, flag=2)
        l2, sent21, sent22 = self.metaphor, self.inputtext_21.text(), self.inputtext_22.text()
        f2, data2 = self._constructor(l2, sents=sent21, sents2=sent22, flag=3)
        l3, sent3 = self.exaggeration, self.inputtext_3.text()
        f3, data3 = self._constructor(l3, sents=sent3, flag=2)
        l4, sent41, sent42 = self.homophonic, self.inputtext_41.text(), self.inputtext_42.text()
        f4, data4 = self._constructor(l4, sents=sent41, sents2=sent42, flag=3)
        l5, sent51, sent52 = self.symbolism, self.inputtext_51.text(), self.inputtext_52.text()
        f5, data5 = self._constructor(l5, sents=sent51, sents2=sent52, flag=3)
        data6 = self.emotion_value
        f7, data7 = self._constructor(self.sentiment, flag=1)
        data8 = self.input_8.text() if self.input_8.text() != "" else "-"
        # print(data1, data2, data3, data4, data5, data6, data7, data8)
        if f1 and f2 and f3 and f4 and f5 and f7:
            self.data.loc[self.data_index[self.totalindex],'sarcasm'] = data1
            self.data.loc[self.data_index[self.totalindex],'metaphor'] = data2
            self.data.loc[self.data_index[self.totalindex], 'exaggeration'] = data3
            self.data.loc[self.data_index[self.totalindex], 'homophonic'] = data4
            self.data.loc[self.data_index[self.totalindex], 'symbolism'] = data5
            self.data.loc[self.data_index[self.totalindex], 'emotion'] = data6
            self.data.loc[self.data_index[self.totalindex], 'sentiment'] = data7
            self.data.loc[self.data_index[self.totalindex], 'other_subtext'] = data8
            self.save_curr_flag = True
            return True
        self._show_message(message="输入不符合格式")
        return False

    def rbclicked(self):
        sender = self.sender()
        if sender == self.bg1:
            self.sarcasm = self.radio_list[self.bg1.checkedId()]
        elif sender == self.bg2:
            self.metaphor = self.radio_list[self.bg2.checkedId()]
        elif sender == self.bg3:
            self.exaggeration = self.radio_list[self.bg3.checkedId()]
        elif sender == self.bg4:
            self.homophonic = self.radio_list[self.bg4.checkedId()]
        elif sender == self.bg5:
            self.symbolism = self.radio_list[self.bg5.checkedId()]
        elif sender == self.bg7:
            self.sentiment = self.radio_list[self.bg7.checkedId()]


    def _saveToFile(self):
        self.data.to_csv(self.fileName, index=False)

    def _constructor(self, label, sents=None, flag=2, sents2=None):
        if label not in ["-1", "0", "1"]:
            return False, None
        if flag == 2:
            sents = "-" if sents == "" else sents
            return True, "{};{}".format(label, sents)
        elif flag ==3:
            sents = "-" if sents == "" else sents
            sents2 = "-" if sents2 == "" else sents2
            return True, "{};{};{}".format(label, sents, sents2)
        else:
            return True, "{}".format(label)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '信息', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            print("save")
            self._saveToFile()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())