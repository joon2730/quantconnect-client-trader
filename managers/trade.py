import math

class TradeManager:
    def __init__(self, qca):
        self.qca = qca
        self.debug = qca.debug

        self.portfolio = qca.portfolio
        self.securities = qca.securities
        self.symbol = qca.symbol

    def execute_order(self, order):
            price = self.securities[self.symbol].Price
            buffer = 0.95
            lot_size = 0.00001

            # Trade full position if buy order
            if order.get("buy", 0) > 0:
                if not self.portfolio[self.symbol].invested:
                    raw_quantity = (self.portfolio.Cash * buffer) / price
                    quantity = math.floor(raw_quantity / lot_size) * lot_size
                    self.qca.market_order(self.symbol, quantity, tag="Full position buy")
                    self.debug(f"BUY → full position: {quantity:.6f} of {self.symbol}")
                else:
                    self.debug(f"Already invested in {self.symbol}. No buy.")
            # Liquidate full position if sell order
            elif order.get("sell", 0) > 0:
                if self.portfolio[self.symbol].invested:
                    self.qca.liquidate(self.symbol, tag="Full liquidation")
                    self.debug(f"SELL → liquidated all {self.symbol}")
                else:
                    self.debug(f"Not holding {self.symbol}. No sell.")
            else:
                self.debug("Hold position. No action.")




        # self.log(order)

        # lot_size = 0.00001
        # # Execute trade based on response from server
        # # buy proportioanl to current cash balance
        # if order.get("buy", 0) > 0:
        #     proportion = order["buy"]
        #     raw_quantity = (self.portfolio.Cash * proportion) / self.securities[self.symbol].Price
        #     qty = math.floor(raw_quantity / lot_size) * lot_size
        #     self.market_order(self.symbol, qty)

        # elif order.get("sell", 0) > 0:
        #     proportion = order["sell"]
        #     raw_quantity = (self.portfolio.Cash * proportion) / self.securities[self.symbol].Price
        #     qty = math.floor(raw_quantity / lot_size) * lot_size
        #     self.market_order(self.symbol, -qty)