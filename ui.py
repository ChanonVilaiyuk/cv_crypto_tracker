# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\scripts\python\cv_crypto_tracker\ui.ui'
#
# Created: Sat May 22 20:37:40 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CVCryptoTracker(object):
    def setupUi(self, CVCryptoTracker):
        CVCryptoTracker.setObjectName("CVCryptoTracker")
        CVCryptoTracker.resize(1059, 750)
        self.centralwidget = QtWidgets.QWidget(CVCryptoTracker)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.portfolio_tab = QtWidgets.QWidget()
        self.portfolio_tab.setObjectName("portfolio_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.portfolio_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.filter_hlayout_5 = QtWidgets.QHBoxLayout()
        self.filter_hlayout_5.setObjectName("filter_hlayout_5")
        self.filter_label_5 = QtWidgets.QLabel(self.portfolio_tab)
        self.filter_label_5.setObjectName("filter_label_5")
        self.filter_hlayout_5.addWidget(self.filter_label_5)
        self.crypto_filter_comboBox = QtWidgets.QComboBox(self.portfolio_tab)
        self.crypto_filter_comboBox.setObjectName("crypto_filter_comboBox")
        self.filter_hlayout_5.addWidget(self.crypto_filter_comboBox)
        self.active_checkBox = QtWidgets.QCheckBox(self.portfolio_tab)
        self.active_checkBox.setObjectName("active_checkBox")
        self.filter_hlayout_5.addWidget(self.active_checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filter_hlayout_5.addItem(spacerItem)
        self.label_12 = QtWidgets.QLabel(self.portfolio_tab)
        self.label_12.setObjectName("label_12")
        self.filter_hlayout_5.addWidget(self.label_12)
        self.text_search_lineEdit = QtWidgets.QLineEdit(self.portfolio_tab)
        self.text_search_lineEdit.setObjectName("text_search_lineEdit")
        self.filter_hlayout_5.addWidget(self.text_search_lineEdit)
        self.filter_hlayout_5.setStretch(1, 1)
        self.filter_hlayout_5.setStretch(3, 6)
        self.filter_hlayout_5.setStretch(5, 2)
        self.verticalLayout_6.addLayout(self.filter_hlayout_5)
        self.portfolio_treeWidget = QtWidgets.QTreeWidget(self.portfolio_tab)
        self.portfolio_treeWidget.setObjectName("portfolio_treeWidget")
        self.verticalLayout_6.addWidget(self.portfolio_treeWidget)
        self.summary_layout = QtWidgets.QHBoxLayout()
        self.summary_layout.setObjectName("summary_layout")
        self.summary_frame = QtWidgets.QFrame(self.portfolio_tab)
        self.summary_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.summary_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.summary_frame.setObjectName("summary_frame")
        self.frame_layout = QtWidgets.QVBoxLayout(self.summary_frame)
        self.frame_layout.setObjectName("frame_layout")
        self.detail_gridlayout = QtWidgets.QGridLayout()
        self.detail_gridlayout.setObjectName("detail_gridlayout")
        self.title1_label = QtWidgets.QLabel(self.summary_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title1_label.setFont(font)
        self.title1_label.setObjectName("title1_label")
        self.detail_gridlayout.addWidget(self.title1_label, 0, 0, 1, 1)
        self.value2_label = QtWidgets.QLabel(self.summary_frame)
        self.value2_label.setObjectName("value2_label")
        self.detail_gridlayout.addWidget(self.value2_label, 1, 1, 1, 1)
        self.title2_label = QtWidgets.QLabel(self.summary_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title2_label.setFont(font)
        self.title2_label.setObjectName("title2_label")
        self.detail_gridlayout.addWidget(self.title2_label, 1, 0, 1, 1)
        self.title3_label = QtWidgets.QLabel(self.summary_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title3_label.setFont(font)
        self.title3_label.setObjectName("title3_label")
        self.detail_gridlayout.addWidget(self.title3_label, 2, 0, 1, 1)
        self.value1_label = QtWidgets.QLabel(self.summary_frame)
        self.value1_label.setObjectName("value1_label")
        self.detail_gridlayout.addWidget(self.value1_label, 0, 1, 1, 1)
        self.title4_label = QtWidgets.QLabel(self.summary_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title4_label.setFont(font)
        self.title4_label.setObjectName("title4_label")
        self.detail_gridlayout.addWidget(self.title4_label, 3, 0, 1, 1)
        self.value3_label = QtWidgets.QLabel(self.summary_frame)
        self.value3_label.setObjectName("value3_label")
        self.detail_gridlayout.addWidget(self.value3_label, 2, 1, 1, 1)
        self.value4_label = QtWidgets.QLabel(self.summary_frame)
        self.value4_label.setObjectName("value4_label")
        self.detail_gridlayout.addWidget(self.value4_label, 3, 1, 1, 1)
        self.detail_gridlayout.setColumnStretch(0, 1)
        self.detail_gridlayout.setColumnStretch(1, 4)
        self.frame_layout.addLayout(self.detail_gridlayout)
        self.summary_layout.addWidget(self.summary_frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.summary_layout.addItem(spacerItem1)
        self.summary_layout.setStretch(0, 1)
        self.summary_layout.setStretch(1, 2)
        self.verticalLayout_6.addLayout(self.summary_layout)
        self.tabWidget.addTab(self.portfolio_tab, "")
        self.wallet_tab = QtWidgets.QWidget()
        self.wallet_tab.setObjectName("wallet_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wallet_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wallet_treeWidget = QtWidgets.QTreeWidget(self.wallet_tab)
        self.wallet_treeWidget.setObjectName("wallet_treeWidget")
        self.wallet_treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.wallet_treeWidget)
        self.frame = QtWidgets.QFrame(self.wallet_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.channel_hlayout = QtWidgets.QHBoxLayout()
        self.channel_hlayout.setObjectName("channel_hlayout")
        self.channel_label = QtWidgets.QLabel(self.frame)
        self.channel_label.setObjectName("channel_label")
        self.channel_hlayout.addWidget(self.channel_label)
        self.p2p_radioButton = QtWidgets.QRadioButton(self.frame)
        self.p2p_radioButton.setChecked(True)
        self.p2p_radioButton.setObjectName("p2p_radioButton")
        self.channel_hlayout.addWidget(self.p2p_radioButton)
        self.visa_radioButton = QtWidgets.QRadioButton(self.frame)
        self.visa_radioButton.setObjectName("visa_radioButton")
        self.channel_hlayout.addWidget(self.visa_radioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.channel_hlayout.addItem(spacerItem2)
        self.channel_hlayout.setStretch(0, 1)
        self.channel_hlayout.setStretch(1, 1)
        self.channel_hlayout.setStretch(2, 1)
        self.channel_hlayout.setStretch(3, 10)
        self.verticalLayout_2.addLayout(self.channel_hlayout)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.add_gridLayout = QtWidgets.QGridLayout()
        self.add_gridLayout.setObjectName("add_gridLayout")
        self.cur1_label = QtWidgets.QLabel(self.frame)
        self.cur1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cur1_label.setObjectName("cur1_label")
        self.add_gridLayout.addWidget(self.cur1_label, 0, 0, 1, 1)
        self.cur2_label = QtWidgets.QLabel(self.frame)
        self.cur2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cur2_label.setObjectName("cur2_label")
        self.add_gridLayout.addWidget(self.cur2_label, 0, 2, 1, 1)
        self.rate_label = QtWidgets.QLabel(self.frame)
        self.rate_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rate_label.setObjectName("rate_label")
        self.add_gridLayout.addWidget(self.rate_label, 0, 4, 1, 1)
        self.cur1_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cur1_lineEdit.setObjectName("cur1_lineEdit")
        self.add_gridLayout.addWidget(self.cur1_lineEdit, 0, 1, 1, 1)
        self.cur2_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.cur2_lineEdit.setObjectName("cur2_lineEdit")
        self.add_gridLayout.addWidget(self.cur2_lineEdit, 0, 3, 1, 1)
        self.add_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.add_pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.add_pushButton.setObjectName("add_pushButton")
        self.add_gridLayout.addWidget(self.add_pushButton, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_gridLayout.addItem(spacerItem3, 0, 7, 1, 1)
        self.rate_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.rate_lineEdit.setObjectName("rate_lineEdit")
        self.add_gridLayout.addWidget(self.rate_lineEdit, 0, 5, 1, 1)
        self.add_gridLayout.setColumnStretch(0, 1)
        self.add_gridLayout.setColumnStretch(1, 2)
        self.add_gridLayout.setColumnStretch(2, 1)
        self.add_gridLayout.setColumnStretch(3, 2)
        self.add_gridLayout.setColumnStretch(4, 1)
        self.add_gridLayout.setColumnStretch(5, 2)
        self.add_gridLayout.setColumnStretch(6, 1)
        self.add_gridLayout.setColumnStretch(7, 6)
        self.verticalLayout_2.addLayout(self.add_gridLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.wallet_tab, "")
        self.buy_sell_tab = QtWidgets.QWidget()
        self.buy_sell_tab.setObjectName("buy_sell_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.buy_sell_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.history_treeWidget = QtWidgets.QTreeWidget(self.buy_sell_tab)
        self.history_treeWidget.setObjectName("history_treeWidget")
        self.history_treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_8.addWidget(self.history_treeWidget)
        self.frame_2 = QtWidgets.QFrame(self.buy_sell_tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.history_tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.history_tabWidget.setObjectName("history_tabWidget")
        self.buy_tab = QtWidgets.QWidget()
        self.buy_tab.setObjectName("buy_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.buy_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buy_label = QtWidgets.QLabel(self.buy_tab)
        self.buy_label.setObjectName("buy_label")
        self.horizontalLayout_2.addWidget(self.buy_label)
        self.buy1_lineEdit = QtWidgets.QLineEdit(self.buy_tab)
        self.buy1_lineEdit.setObjectName("buy1_lineEdit")
        self.horizontalLayout_2.addWidget(self.buy1_lineEdit)
        self.label_4 = QtWidgets.QLabel(self.buy_tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.buy2_lineEdit = QtWidgets.QLineEdit(self.buy_tab)
        self.buy2_lineEdit.setObjectName("buy2_lineEdit")
        self.horizontalLayout_2.addWidget(self.buy2_lineEdit)
        self.label_6 = QtWidgets.QLabel(self.buy_tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.buy3_lineEdit = QtWidgets.QLineEdit(self.buy_tab)
        self.buy3_lineEdit.setObjectName("buy3_lineEdit")
        self.horizontalLayout_2.addWidget(self.buy3_lineEdit)
        self.buy_pushButton = QtWidgets.QPushButton(self.buy_tab)
        self.buy_pushButton.setObjectName("buy_pushButton")
        self.horizontalLayout_2.addWidget(self.buy_pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 2)
        self.horizontalLayout_2.setStretch(6, 1)
        self.horizontalLayout_2.setStretch(7, 6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.history_tabWidget.addTab(self.buy_tab, "")
        self.sell_tab = QtWidgets.QWidget()
        self.sell_tab.setObjectName("sell_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.sell_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.sell_hLayout = QtWidgets.QHBoxLayout()
        self.sell_hLayout.setObjectName("sell_hLayout")
        self.label_5 = QtWidgets.QLabel(self.sell_tab)
        self.label_5.setObjectName("label_5")
        self.sell_hLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.sell_tab)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.sell_hLayout.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.sell_tab)
        self.label_7.setObjectName("label_7")
        self.sell_hLayout.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.sell_tab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.sell_hLayout.addWidget(self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.sell_tab)
        self.label_8.setObjectName("label_8")
        self.sell_hLayout.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.sell_tab)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.sell_hLayout.addWidget(self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.sell_tab)
        self.label_9.setObjectName("label_9")
        self.sell_hLayout.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.sell_tab)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.sell_hLayout.addWidget(self.lineEdit_8)
        self.sell_push = QtWidgets.QPushButton(self.sell_tab)
        self.sell_push.setObjectName("sell_push")
        self.sell_hLayout.addWidget(self.sell_push)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sell_hLayout.addItem(spacerItem5)
        self.sell_hLayout.setStretch(0, 1)
        self.sell_hLayout.setStretch(1, 2)
        self.sell_hLayout.setStretch(2, 1)
        self.sell_hLayout.setStretch(3, 2)
        self.sell_hLayout.setStretch(4, 1)
        self.sell_hLayout.setStretch(5, 2)
        self.sell_hLayout.setStretch(6, 1)
        self.sell_hLayout.setStretch(7, 2)
        self.sell_hLayout.setStretch(8, 1)
        self.sell_hLayout.setStretch(9, 6)
        self.verticalLayout_7.addLayout(self.sell_hLayout)
        self.history_tabWidget.addTab(self.sell_tab, "")
        self.verticalLayout.addWidget(self.history_tabWidget)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.verticalLayout_8.setStretch(0, 6)
        self.verticalLayout_8.setStretch(1, 1)
        self.tabWidget.addTab(self.buy_sell_tab, "")
        self.tracking_tab = QtWidgets.QWidget()
        self.tracking_tab.setObjectName("tracking_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tracking_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.filter_hlayout_3 = QtWidgets.QHBoxLayout()
        self.filter_hlayout_3.setObjectName("filter_hlayout_3")
        self.filter_label_3 = QtWidgets.QLabel(self.tracking_tab)
        self.filter_label_3.setObjectName("filter_label_3")
        self.filter_hlayout_3.addWidget(self.filter_label_3)
        self.filter_comboBox = QtWidgets.QComboBox(self.tracking_tab)
        self.filter_comboBox.setObjectName("filter_comboBox")
        self.filter_hlayout_3.addWidget(self.filter_comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filter_hlayout_3.addItem(spacerItem6)
        self.label_10 = QtWidgets.QLabel(self.tracking_tab)
        self.label_10.setObjectName("label_10")
        self.filter_hlayout_3.addWidget(self.label_10)
        self.search_lineEdit = QtWidgets.QLineEdit(self.tracking_tab)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.filter_hlayout_3.addWidget(self.search_lineEdit)
        self.filter_hlayout_3.setStretch(1, 1)
        self.filter_hlayout_3.setStretch(2, 6)
        self.filter_hlayout_3.setStretch(4, 2)
        self.verticalLayout_5.addLayout(self.filter_hlayout_3)
        self.track_treeWidget = QtWidgets.QTreeWidget(self.tracking_tab)
        self.track_treeWidget.setObjectName("track_treeWidget")
        self.track_treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.track_treeWidget)
        self.tabWidget.addTab(self.tracking_tab, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setObjectName("setting_tab")
        self.tabWidget.addTab(self.setting_tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        CVCryptoTracker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CVCryptoTracker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        CVCryptoTracker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CVCryptoTracker)
        self.statusbar.setObjectName("statusbar")
        CVCryptoTracker.setStatusBar(self.statusbar)

        self.retranslateUi(CVCryptoTracker)
        self.tabWidget.setCurrentIndex(0)
        self.history_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CVCryptoTracker)
        CVCryptoTracker.setTabOrder(self.tabWidget, self.portfolio_treeWidget)
        CVCryptoTracker.setTabOrder(self.portfolio_treeWidget, self.wallet_treeWidget)
        CVCryptoTracker.setTabOrder(self.wallet_treeWidget, self.p2p_radioButton)
        CVCryptoTracker.setTabOrder(self.p2p_radioButton, self.visa_radioButton)
        CVCryptoTracker.setTabOrder(self.visa_radioButton, self.cur1_lineEdit)
        CVCryptoTracker.setTabOrder(self.cur1_lineEdit, self.cur2_lineEdit)
        CVCryptoTracker.setTabOrder(self.cur2_lineEdit, self.rate_lineEdit)
        CVCryptoTracker.setTabOrder(self.rate_lineEdit, self.add_pushButton)
        CVCryptoTracker.setTabOrder(self.add_pushButton, self.history_treeWidget)
        CVCryptoTracker.setTabOrder(self.history_treeWidget, self.history_tabWidget)
        CVCryptoTracker.setTabOrder(self.history_tabWidget, self.buy1_lineEdit)
        CVCryptoTracker.setTabOrder(self.buy1_lineEdit, self.buy2_lineEdit)
        CVCryptoTracker.setTabOrder(self.buy2_lineEdit, self.buy3_lineEdit)
        CVCryptoTracker.setTabOrder(self.buy3_lineEdit, self.buy_pushButton)
        CVCryptoTracker.setTabOrder(self.buy_pushButton, self.lineEdit_5)
        CVCryptoTracker.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        CVCryptoTracker.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        CVCryptoTracker.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        CVCryptoTracker.setTabOrder(self.lineEdit_8, self.sell_push)

    def retranslateUi(self, CVCryptoTracker):
        CVCryptoTracker.setWindowTitle(QtWidgets.QApplication.translate("CVCryptoTracker", "CV Crypto Tracker v.0.0.1", None, -1))
        self.filter_label_5.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Filter: ", None, -1))
        self.active_checkBox.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Hide zero coin", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Search", None, -1))
        self.portfolio_treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("CVCryptoTracker", "Crypto", None, -1))
        self.portfolio_treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("CVCryptoTracker", "Amount", None, -1))
        self.portfolio_treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("CVCryptoTracker", "Avg", None, -1))
        self.portfolio_treeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("CVCryptoTracker", "Last", None, -1))
        self.portfolio_treeWidget.headerItem().setText(4, QtWidgets.QApplication.translate("CVCryptoTracker", "Cost", None, -1))
        self.portfolio_treeWidget.headerItem().setText(5, QtWidgets.QApplication.translate("CVCryptoTracker", "Curr Val", None, -1))
        self.portfolio_treeWidget.headerItem().setText(6, QtWidgets.QApplication.translate("CVCryptoTracker", "%Unrl", None, -1))
        self.portfolio_treeWidget.headerItem().setText(7, QtWidgets.QApplication.translate("CVCryptoTracker", "Unrl Profit/Loss", None, -1))
        self.title1_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "% Profit / Loss", None, -1))
        self.value2_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "-", None, -1))
        self.title2_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Profit / Loss", None, -1))
        self.title3_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Total Cost", None, -1))
        self.value1_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "-", None, -1))
        self.title4_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Total Cost (THB)", None, -1))
        self.value3_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "-", None, -1))
        self.value4_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "-", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.portfolio_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Portfolio", None, -1))
        self.channel_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Channel", None, -1))
        self.p2p_radioButton.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "P2P", None, -1))
        self.visa_radioButton.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Visa", None, -1))
        self.cur1_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "THB : ", None, -1))
        self.cur2_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "USDT : ", None, -1))
        self.rate_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Rate : ", None, -1))
        self.add_pushButton.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Add", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wallet_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Wallet", None, -1))
        self.buy_label.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "USDT: ", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Amount THB", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Receive USDT", None, -1))
        self.buy_pushButton.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Submit", None, -1))
        self.history_tabWidget.setTabText(self.history_tabWidget.indexOf(self.buy_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Buy", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Crypto", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Amount", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Price", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "USDT", None, -1))
        self.sell_push.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Submit", None, -1))
        self.history_tabWidget.setTabText(self.history_tabWidget.indexOf(self.sell_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Sell", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.buy_sell_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Buy / Sell History", None, -1))
        self.filter_label_3.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Filter: ", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("CVCryptoTracker", "Search", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tracking_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Tracking", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), QtWidgets.QApplication.translate("CVCryptoTracker", "Setting", None, -1))

