import os
import sys
import logging
from collections import OrderedDict
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
import stylesheet
import ui
from model import wallet
from model import trade
from model import portfolio

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
dirname = os.path.dirname(__file__).replace('\\', '/')


class Data:
    buy_crypto = '{}/_data/buy_crypto.yml'.format(dirname)
    trade = '{}/_data/trade.yml'.format(dirname)


class CVTracker(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CVTracker, self).__init__(parent)
        self.ui = ui.Ui_CVCryptoTracker()
        self.ui.setupUi(self)
        self.buy_currency = 'THB'
        self.trade_coin = 'USDT'

        self.portfolio = portfolio.Portfolio(self)
        self.portfolio.trade_file = Data.trade
        self.portfolio.load()
        self.wallet = wallet.Wallet(self)
        self.wallet.record_file = Data.buy_crypto
        self.wallet.load()

        self.trade = trade.TradeHistory(self)
        self.trade.trade_file = Data.trade
        self.trade.load()

        self.init_signals()

    def init_signals(self):
        self.ui.add_pushButton.clicked.connect(self.add_wallet_value)


    def add_wallet_value(self):
        if self.ui.p2p_radioButton.isChecked():
            channel = 'P2P'
        elif self.ui.visa_radioButton.isChecked():
            channel = 'VISA'

        buy_volumn = self.ui.cur1_lineEdit.text()
        receive_volumn = self.ui.cur2_lineEdit.text()
        trade_price = self.ui.rate_lineEdit.text()

        self.wallet.add_new_record(
            channel=channel,
            currency=self.buy_currency,
            volumn=float(buy_volumn), fee=0,
            trade_coin=self.trade_coin,
            trade_price=float(trade_price),
            trade_volumn=float(receive_volumn)
            )

        self.wallet.load()













class Currency(object):
    """Currency class"""
    def __init__(self, currency, volumn):
        super(Currency, self).__init__()
        self.currency = currency
        self.volumn = volumn

    def __repr__(self):
        return self.currency

    def __str__(self):
        return self.currency

    @property
    def value(self):
        return self.volumn





def show():
    logger.info('Run in standalone\n')
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    myApp = CVTracker()
    myApp.show()
    stylesheet.set_default(app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    show()
