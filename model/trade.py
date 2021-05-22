import os
import sys
import logging
from collections import OrderedDict
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import stylesheet
from . import utils

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
dirname = os.path.dirname(__file__).replace('\\', '/')


class Config:
    action = 'Action'
    time = 'Time'
    crypto = 'Crypto'
    volumn = 'Volumn'
    pairCoin = 'Pair Coin'
    price = 'Price'
    tradeVolumn = 'Amount USDT'
    titles = [action, time, crypto, volumn, pairCoin, price, tradeVolumn]


class TradeHistory(object):
    """docstring for TradeHistory"""
    def __init__(self, main_widget):
        super(TradeHistory, self).__init__()
        self.main_widget = main_widget
        self.tree_widget = main_widget.ui.history_treeWidget
        self.trade_file = None
        self.tree_widget.setHeaderLabels(Config.titles)

    def load(self):
        self.records = self.load_trade_history() or list()
        if self.records:
            self.display_trade_history(self.records)

    def load_trade_history(self):
        """ load data and display """
        trade_data = utils.yml_loader(self.trade_file)
        return trade_data

    def display_trade_history(self, records):

        self.tree_widget.clear()
        root = self.tree_widget.invisibleRootItem()
        self.tree_widget.addTopLevelItem(root)

        for record in records:
            action = record['action']
            timestamp = record['timestamp']
            crypto = record['crypto']
            volumn = record['volumn']
            trade_coin = record['tradeCoin']['crypto']
            trade_price = record['tradeCoin']['price']
            trade_volumn = record['tradeCoin']['volumn']
            data_order = [action, timestamp, crypto, volumn, trade_coin, trade_price, trade_volumn]

            item = QtWidgets.QTreeWidgetItem(root)

            for i, data in enumerate(data_order):
                item.setText(i, str(data))
                item.setData(i, QtCore.Qt.UserRole, data)



