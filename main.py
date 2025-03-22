from AlgorithmImports import *

from managers.communication import ComminucationManager
from managers.trade import TradeManager

from datetime import timedelta
import json

class ClientTrader(QCAlgorithm):
    def initialize(self):
        # Backtest settings
        self.set_start_date(2024, 9, 1)
        self.set_end_date(2024, 12, 31)
        self.set_cash(10000)
        self.days_count = 0

        # security settings
        self.symbol = self.add_crypto("BTCUSD", Resolution.DAILY).Symbol
        self.securities[self.symbol].fee_model = BinanceFeeModel()
        
        # algorithm settings
        self.set_time_zone(TimeZones.UTC)

        # schedule routine
        self.schedule.on(
            self.date_rules.every_day(),
            self.time_rules.midnight,
            self.routine
        )

        # instantiate managers
        self.cmm = ComminucationManager(self)
        self.tdm = TradeManager(self)

    def routine(self):
        self.days_count += 1

        self.debug(f"Day {self.days_count} / {self.Time.strftime('%Y-%m-%d %H:%M:%S')}: current price - {self.securities[self.symbol].Price}")
        self.log(f"Day {self.days_count} / {self.Time.strftime('%Y-%m-%d %H:%M:%S')}: current price - {self.securities[self.symbol].Price}")
        
        # Fetch order from server and execute
        order = self.cmm.fetch_order()
        self.tdm.execute_order(order)
        
    # def on_order_event(self, order_event):
    #     # report result to server if order is filled or cancelled
    #     if order_event.status in [OrderStatus.FILLED, OrderStatus.CANCELED, OrderStatus.INVALID]:
    #         self.cmm.report_order_event(order_event=order_event)
    #     else:
    #         self.log(f"Order Status: {order_event.Status}")



    