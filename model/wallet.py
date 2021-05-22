import os
import sys
import logging
from collections import OrderedDict
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import stylesheet
from . import utils
from . import summary

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
dirname = os.path.dirname(__file__).replace('\\', '/')


class Wallet(object):
    """Wallet listWidget utilities"""
    def __init__(self, main_widget):
        super(Wallet, self).__init__()
        self.main_widget = main_widget
        self.tree_widget = main_widget.ui.wallet_treeWidget
        self.record_file = None
        self.input_currency = ''
        self.channel = 'Channel'
        self.volumn = 'Cost (THB)'
        self.price = 'Exchange rate'
        self.receive_volumn = 'Receive USDT'
        self.fee = 'Fee'
        self.headers = [self.channel, self.volumn, self.price, self.receive_volumn, self.fee]
        self.total_channel = ''
        self.total_volumn = 'Total Cost'
        self.avg = 'Average'
        self.total_receive_volumn = 'Total USDT'
        self.total_fee = 'Total Fees'
        self.summary_headers = [self.total_channel, self.total_volumn, self.avg, self.total_receive_volumn, self.total_fee]
        self.header_size = {
            self.channel: 120,
            self.volumn: 120,
            self.price: 120,
            self.receive_volumn: 120,
            self.fee: 120
            }

        self.summary_header_size = {
            self.total_channel: 120,
            self.total_volumn: 120,
            self.avg: 120,
            self.total_receive_volumn: 120,
            self.total_fee: 120
            }
        self.set_header()
        self.create_summary_widget()

        self.records = list()

    def create_summary_widget(self):
        # create summary tree widget
        self.summary_widget = summary.Summary()
        self.summary_widget.set_header(self.summary_headers)
        index, parent_layout = summary.find_parent_layout(self.tree_widget)
        parent_layout.insertWidget(index + 1, self.summary_widget)

        # resize column
        for i, header in enumerate(self.summary_headers):
            self.summary_widget.set_column_size(i, self.summary_header_size[header])

    def load(self):
        """ load data and display """
        self.records = self.load_history() or list()
        if self.records:
            self.display_wallet(self.records)

    def load_history(self):
        buy_crypto_data = utils.yml_loader(self.record_file)
        return buy_crypto_data

    def display_wallet(self, records):
        self.tree_widget.clear()
        self.add_records([BuyRecord(a) for a in records])

    def set_currency(self, input_currency, buy_currency):
        volumn = 'Volumn {}'.format(input_currency)
        receive_volumn = 'Receive {}'.format(buy_currency)
        self.headers[self.headers.index(self.volumn)] = volumn
        self.headers[self.headers.index(self.receive_volumn)] = receive_volumn
        self.volumn = volumn
        self.receive_volumn = receive_volumn
        self.set_header()

    def set_header(self):
        self.tree_widget.setHeaderLabels(self.headers)
        for i, header in enumerate(self.headers):
            self.tree_widget.header().resizeSection(i, self.header_size[header])

    def add_history(self, record):
        item = QtWidgets.QTreeWidgetItem(self.tree_widget)
        column_order = [self.channel, self.volumn, self.price, self.receive_volumn, self.fee]
        data = [record.channel, record.volumn, record.trade_price, record.trade_volumn, record.fee]

        for i in range(len(column_order)):
            item.setText(self.headers.index(column_order[i]), str(data[i]))
            item.setData(i, QtCore.Qt.UserRole, data[i])

    def add_records(self, records):
        sum_cost = 0.0
        sum_receive_volumn = 0.0
        for record in records:
            sum_cost += record.volumn
            sum_receive_volumn += record.trade_volumn
            self.add_history(record)

        # sum Cost
        self.summary_widget.add_value(self.headers.index(self.volumn), sum_cost)
        self.summary_widget.add_value(self.headers.index(self.receive_volumn), round(sum_receive_volumn, 4))
        self.summary_widget.add_value(self.headers.index(self.price), round(sum_cost / sum_receive_volumn, 4))

    def sum_column(self, column):
        count = self.tree_widget.topLevelItemCount()
        sum_value = 0.0
        for i in range(count):
            item = self.tree_widget.itemAt(i, column)
            print(item.text(0), item.text(1), item.text(2))
            print(item)
            value = item.data(column, QtCore.Qt.UserRole)
            print('value', value, column)
            sum_value += value

        self.summary_widget.add_value(column, sum_value)
        return sum_value

    def add_new_record(self, channel, currency, volumn, fee, trade_coin, trade_price, trade_volumn):
        data = OrderedDict()
        data['channel'] = channel
        data['currency'] = currency
        data['volumn'] = volumn
        data['fee'] = fee
        trade_coin_dict = OrderedDict()
        trade_coin_dict['crypto'] = trade_coin
        trade_coin_dict['price'] = trade_price
        trade_coin_dict['volumn'] = trade_volumn
        data['tradeCoin'] = trade_coin_dict
        self.write(data)

    def write(self, data):
        self.records.append(data)
        utils.yml_dumper(Data.buy_crypto, self.records)


class BuyRecord(object):
    """docstring for BuyRecord"""
    def __init__(self, record):
        super(BuyRecord, self).__init__()
        self.channel = record['channel']
        self.currency = record['currency']
        self.volumn = record['volumn']
        self.fee = record['fee']
        self.trade_currency = record['tradeCoin']['crypto']
        self.trade_price = record['tradeCoin']['price']
        self.trade_volumn = record['tradeCoin']['volumn']
