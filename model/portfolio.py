import os
import sys
import logging
from collections import OrderedDict
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from . import utils

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
dirname = os.path.dirname(__file__).replace('\\', '/')


class Config:
    crypto = 'Crypto'
    volumn = 'Volumn'
    avg = 'Price / Avg'
    last = 'Last'
    trade_volumn = 'Cost'
    current_value = 'Curr Val'
    unrl_percent = '%Unrl'
    unrl_profit_loss = 'Unrl Profit/Loss'
    real_profit_loss = 'Real Profit/Loss'
    headers = [crypto, volumn, avg, last, trade_volumn, current_value, unrl_percent, unrl_profit_loss, real_profit_loss]


class Portfolio(object):
    """TreeWidget class utilities"""
    def __init__(self, main_widget):
        super(Portfolio, self).__init__()
        self.main_widget = main_widget
        self.tree_widget = main_widget.ui.portfolio_treeWidget
        self.trade_file = None
        self.tree_widget.setHeaderLabels(Config.headers)

    def init_signals(self):
        self.main_widget.ui.crypto_filter_comboBox.currentIndexChanged.connect(self.display)
        self.main_widget.ui.text_search_lineEdit.textChanged.connect(self.display)
        self.main_widget.ui.active_checkBox.stateChanged.connect(self.display)

    def load(self):
        self.records = self.load_trade_data()
        self.sum_record_dict = sum_record(self.records)
        if self.records:
            self.display()

    def load_trade_data(self):
        data = utils.yml_loader(self.trade_file) if os.path.exists(self.trade_file) else list()
        return data

    def display(self):
        self.load_filters()
        self.set_display()
        self.update_price()

    def load_filters(self):
        coins = ['All']
        coins.extend(sorted(list(set([a['crypto'] for a in self.records]))))
        self.main_widget.ui.crypto_filter_comboBox.addItems(coins)

    def update_price(self):
        import random
        childs = [self.root.child(a) for a in range(self.root.childCount())]

        for item in childs:
            record = RecordItem(item)
            coin = record.coin()
            pair = 'USDT'
            # price = utils.get_latest_price('ETH', compare_coin=pair)
            # record.set_last(price['ETH'][pair])
            record.set_last(random.randint(3, 4))
            # self.update_realtime_column(item)

    def update_realtime_column(self, item):
        # update current_value unrl_percent unrl_profit_loss from last price
        # calculation current_value = last * volumn
        record = RecordItem(item)
        current_price = record.last()
        current_value = current_price * record.volumn()
        unrl_profit_loss = current_value - record.cost()
        unrl_percent = (unrl_profit_loss / record.cost()) * 100
        record.set_current_value(current_value)
        record.set_unrl_profit_loss(unrl_profit_loss)
        record.set_unrl_percent(unrl_percent)

    def set_display(self):
        key1 = self.main_widget.ui.crypto_filter_comboBox.currentText()
        key2 = self.main_widget.ui.text_search_lineEdit.text()
        active = self.main_widget.ui.active_checkBox.isChecked()

        # display
        self.tree_widget.clear()
        self.root = self.tree_widget.invisibleRootItem()
        self.tree_widget.addTopLevelItem(self.root)

        for crypto, data in self.sum_record_dict.items():
            # top item display summary
            top_item = QtWidgets.QTreeWidgetItem(self.root)
            self.add_tree_item(top_item, [(Config.headers.index(Config.crypto), crypto)])

            cycle_data = data['cycles']
            if cycle_data:
                for name, value in cycle_data.items():
                    chunk = value['volumn']
                    profit = value['profit']
                    total_cost = value['cost']
                    total_sell = value['sell']
                    total_vol = value['total_vol']
                    avg = value['avg']
                    sum_vol = value['sum_vol']
                    if not chunk:
                        continue
                    chunk_item = QtWidgets.QTreeWidgetItem(top_item)
                    chunk_item.setText(Config.headers.index(Config.crypto), str(name))
                    chunk_record = RecordItem(chunk_item)
                    chunk_record.set_avg(avg)
                    chunk_record.set_cost(total_cost)
                    chunk_record.set_profit(profit)
                    chunk_record.set_volumn(sum_vol)

                    if name == 'active':
                        top_record = RecordItem(top_item)
                        top_record.set_volumn(sum_vol)
                        top_record.set_avg(avg)
                        top_record.set_cost(value['active_cost'])

                    for record in chunk:
                        trade_item = QtWidgets.QTreeWidgetItem(chunk_item)
                        if record.action == record.buy:
                            trade_volumn_index = Config.headers.index(Config.trade_volumn) #4
                            trade_price_index = Config.headers.index(Config.avg)
                        elif record.action == record.sell:
                            trade_volumn_index = Config.headers.index(Config.real_profit_loss)
                            trade_price_index = Config.headers.index(Config.last)
                        data_list = [
                            (Config.headers.index(Config.crypto), record.action),
                            (Config.headers.index(Config.volumn), record.volumn),
                            (trade_price_index, record.trade_price),
                            (trade_volumn_index, record.trade_volumn)]

                        self.add_tree_item(trade_item, data_list)


                        # print(record.action, record.volumn, record.trade_price, record.trade_volumn,
                        #         '||', record.sum_volumn, record.sum_trade_volumn,
                        #         record.avg)

                        # if i == len(data['active']) - 1:
                        #     sum_list = [
                        #         (Config.headers.index(Config.volumn), record.sum_volumn),
                        #         (Config.headers.index(Config.avg), record.avg),
                        #         (Config.headers.index(Config.trade_volumn), record.sum_trade_volumn)]

                        #     self.add_tree_item(top_item, sum_list)
                        #     self.add_tree_item(active_item, sum_list)

            # i = 1
            # for cycle_count, value in data['cycles'].items():
            #     chunk = value['volumn']
            #     profit = value['profit']

            #     chunk_item = QtWidgets.QTreeWidgetItem(top_item)
            #     chunk_item.setText(0, str(cycle_count))

            #     for record in chunk:
            #         transaction_item = QtWidgets.QTreeWidgetItem(chunk_item)
            #         # print(record.action, record.volumn, record.trade_price, record.trade_volumn,
            #         #     '||', record.sum_volumn, record.sum_trade_volumn,
            #         #     record.avg)
            #         if record.action == record.buy:
            #             trade_volumn_index = Config.headers.index(Config.trade_volumn) #4
            #             trade_price_index = Config.headers.index(Config.avg)
            #         elif record.action == record.sell:
            #             trade_volumn_index = Config.headers.index(Config.real_profit_loss)
            #             trade_price_index = Config.headers.index(Config.last)
            #         data_list = [
            #             (Config.headers.index(Config.crypto), record.action),
            #             (Config.headers.index(Config.volumn), record.volumn),
            #             (trade_price_index, record.trade_price),
            #             (trade_volumn_index, record.trade_volumn)]
            #         self.add_tree_item(transaction_item, data_list)

            #         if record == chunk[-1]:
            #             sum_list = [
            #                 (Config.headers.index(Config.volumn), record.sum_volumn),
            #                 (Config.headers.index(Config.avg), record.avg),
            #                 (Config.headers.index(Config.real_profit_loss), profit)]
            #             self.add_tree_item(chunk_item, sum_list)

            #     print('profit', profit)

            #     print('----')
            #     i += 1
            # print('Active')
            # for record in data['active']:
            #     print(record.action, record.volumn, record.trade_price, record.trade_volumn,
            #             '||', record.sum_volumn, record.sum_trade_volumn,
            #             record.avg)
            # print('====')

    def add_tree_item(self, item, data_list):
        for data in data_list:
            index = data[0]
            value = data[1]
            display = round(value, 4) if isinstance(value, float) else value


            item.setText(index, str(display))
            item.setData(index, QtCore.Qt.UserRole, value)

        return item


def get_prices(cryptos, compare_coin):
    price_dict = dict()
    for crypto in cryptos:
        price = utils.get_latest_price(crypto, compare_coin=compare_coin)
        price_dict[crypto] = price
    return price_dict


def sum_record(records):
    cryptos = list(set([TradeRecord(record).crypto for record in records]))
    crypto_dict = OrderedDict()

    for crypto in cryptos:
        i = 0
        crypto_dict[crypto] = list()
        for record in records:
            record = TradeRecord(record)
            if crypto == record.crypto:
                crypto_dict[crypto].append(record)

    sum_dict = OrderedDict()

    for crypto, records in crypto_dict.items():
        vols = list()
        cycles = OrderedDict()
        cycles['active'] = dict()
        cycle_count = 1
        active_vol = list()
        total_cost = 0.0
        total_sell = 0.0
        total_vol = 0.0
        avg = 0.0
        sum_vol = 0.0
        profit = 0.0
        # count items
        i = 0
        # count for buy / sell iteration
        ii = 0
        for record in records:
            if record.action == record.buy:
                if not ii == 0:
                    prev_record = records[i-1]
                    record.sum_volumn = prev_record.sum_volumn + record.volumn
                    record.sum_trade_volumn = prev_record.sum_trade_volumn + record.trade_volumn
                else:
                    record.sum_volumn = record.volumn
                    record.sum_trade_volumn = record.trade_volumn
                record.avg = record.sum_trade_volumn / record.sum_volumn
                total_cost += record.trade_volumn
                total_vol += record.volumn
                avg = record.avg
                sum_vol += record.volumn

            if record.action == record.sell:
                last_record = records[i-1]
                record.sum_volumn = last_record.sum_volumn - record.volumn
                record.sum_trade_volumn = last_record.sum_trade_volumn - record.trade_volumn
                record.avg = last_record.avg
                total_sell += record.trade_volumn
                sum_vol -= record.volumn

            vols.append(record)
            print('add', record.action)

            ii += 1
            if record.sum_volumn <= 0:
                profit = total_sell - total_cost
                cycles[cycle_count] = {
                    'volumn': vols, 'profit': profit,
                    'cost': total_cost, 'sell': total_sell,
                    'total_vol': total_vol, 'avg': avg, 'sum_vol': sum_vol}
                vols = list()
                total_sell = 0.0
                total_cost = 0.0
                total_vol = 0.0
                avg = 0.0
                ii = 0
                sum_vol = 0.0
                profit = 0.0
                cycle_count += 1

            i += 1

        active_cost = sum_vol * avg
        cycles.update({'active': {
                'volumn': vols, 'profit': profit,
                'cost': total_cost, 'sell': total_sell,
                'total_vol': total_vol, 'avg': avg, 'sum_vol': sum_vol,
                'active_cost': active_cost}})

        sum_dict[crypto] = {'cycles': cycles}

    return sum_dict

def print_sum(sum_dict):

    for crypto, data in sum_dict.items():
        i = 1
        for chunk, profit in data['cycles']:
            print(i)
            for record in chunk:
                print(record.action, record.volumn, record.trade_price, record.trade_volumn,
                    '||', record.sum_volumn, record.sum_trade_volumn,
                    record.avg)
            print('profit', profit)

            print('----')
        print('Active')
        i += 1
        for record in data['active']:
            print(record.action, record.volumn, record.trade_price, record.trade_volumn,
                    '||', record.sum_volumn, record.sum_trade_volumn,
                    record.avg)
        print('====')



class TradeRecord(object):
    """docstring for TradeRecord"""
    def __init__(self, record):
        super(TradeRecord, self).__init__()
        self.record = record
        self.action = record['action']
        self.timestamp = record['timestamp']
        self.crypto = record['crypto']
        self.volumn = record['volumn']
        self.trade_coin = record['tradeCoin']['crypto']
        self.trade_price = record['tradeCoin']['price']
        self.trade_volumn = record['tradeCoin']['volumn']
        self.buy = 'buy'
        self.sell = 'sell'


class RecordItem(object):
    """docstring for RecordItem"""
    def __init__(self, item):
        super(RecordItem, self).__init__()
        self.item = item

    def coin(self):
        return self.item.data(Config.headers.index(Config.crypto), QtCore.Qt.UserRole)

    def volumn(self):
        return self.item.data(Config.headers.index(Config.volumn), QtCore.Qt.UserRole)

    def avg(self):
        return self.item.data(Config.headers.index(Config.avg), QtCore.Qt.UserRole)

    def last(self):
        return self.item.data(Config.headers.index(Config.last), QtCore.Qt.UserRole)

    def cost(self):
        return self.item.data(Config.headers.index(Config.trade_volumn), QtCore.Qt.UserRole)

    def current_value(self):
        return self.item.data(Config.headers.index(Config.current_value), QtCore.Qt.UserRole)

    def unrl_percent(self):
        return self.item.data(Config.headers.index(Config.unrl_percent), QtCore.Qt.UserRole)

    def unrl_profit_loss(self):
        return self.item.data(Config.headers.index(Config.unrl_profit_loss), QtCore.Qt.UserRole)

    def profit(self):
        return self.item.data(Config.headers.index(Config.real_profit_loss), QtCore.Qt.UserRole)

    def set_last(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.last), display)
        self.item.setData(Config.headers.index(Config.last), QtCore.Qt.UserRole, value)

    def set_coin(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.crypto), display)
        self.item.setData(Config.headers.index(Config.crypto), QtCore.Qt.UserRole, value)

    def set_volumn(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.volumn), display)
        self.item.setData(Config.headers.index(Config.volumn), QtCore.Qt.UserRole, value)

    def set_avg(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.avg), display)
        self.item.setData(Config.headers.index(Config.avg), QtCore.Qt.UserRole, value)

    def set_last(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.last), display)
        self.item.setData(Config.headers.index(Config.last), QtCore.Qt.UserRole, value)

    def set_cost(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.trade_volumn), display)
        self.item.setData(Config.headers.index(Config.trade_volumn), QtCore.Qt.UserRole, value)

    def set_current_value(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.current_value), display)
        self.item.setData(Config.headers.index(Config.current_value), QtCore.Qt.UserRole, value)

    def set_unrl_percent(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.unrl_percent), display)
        self.item.setData(Config.headers.index(Config.unrl_percent), QtCore.Qt.UserRole, value)

    def set_unrl_profit_loss(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.unrl_profit_loss), display)
        self.item.setData(Config.headers.index(Config.unrl_profit_loss), QtCore.Qt.UserRole, value)

    def set_profit(self, value):
        display = str(value)
        if isinstance(value, float):
            display = str(round(value, 4))
        self.item.setText(Config.headers.index(Config.real_profit_loss), display)
        self.item.setData(Config.headers.index(Config.real_profit_loss), QtCore.Qt.UserRole, value)

    def update(self):
        pass
