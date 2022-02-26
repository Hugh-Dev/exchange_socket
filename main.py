#!/usr/bin/python3
import websocket
from settings import SOCKET_HOST, MSG
import pandas as pd
from prettytable import PrettyTable

class Wsocket:

    def __init__(self):
        self.ws = websocket.WebSocket()

    def on_open(self):
        self.ws.connect(SOCKET_HOST)

    def on_send(self):
        self.ws.send(MSG)

    def on_data(self):
        return self.ws.recv()

    def on_date(self):
        return self.ws.getheaders()

class Serializers:

    def formatting(self, data):
        self.data = pd.read_json(data, orient='index')
        USDMXN = self.data['USDMXN']
        self.prices = USDMXN[0]
        self.bid = self.prices['bid']
        self.ask = self.prices['ask']
        return self.bid, self.ask

    def formatter_date(self, date):
        self.date = date['date']
        return self.date

    def calculate_spread(self, bid, ask, date):

        self.spread = bid - ask
        self.spread = '{:4f}'.format(self.spread)
        self.table = PrettyTable()

        if self.spread > '0':
            self.buy = 'Buy' 
            self.table.field_names = ["Date", "Bid price", "Ask price", "Spread", 'Action']
            self.table.add_row([date, bid, ask, self.spread, 'Buy'])
            print(self.table)

        elif self.spread < '0':
            self.sell = 'Sell'
            self.table.field_names = ["Date", "Bid price", "Ask price", "Spread", 'Action']
            self.table.add_row([date, bid, ask, self.spread, 'Sell'])
            print(self.table)

        else:
            self.without_change = 'Without change'
            self.table.field_names = ["Date", "Bid price", "Ask price", "Spread", 'Action']
            self.table.add_row([date, bid, ask, self.spread, 'Without change'])
            print(self.table)

        return self.spread


class Queue(Serializers):

    def __init__(self):
        self.bid_long = []
        self.ask_long = []

    def loop(self, data):
        while True:
            bid, ask = Serializers.formatting(self, data=data)
            self.bid_long.append(bid)
            self.ask_long.append(ask)
            if len(self.bid_long) == 10 and len(self.ask_long) == 10:
                break
        return self.bid_long, self.ask_long

    def calculate_long_spread(self):
        self.count_ask = 0
        self.count_bid = 0
        for ask in ask_long:
            self.count_ask += ask
        for bid in bid_long:
            self.count_bid += bid
        self.mean = self.count_ask - self.count_bid
        return self.mean, self.count_ask, self.count_bid






if __name__ == "__main__":
    
    try:
        """ Websocket"""
        ws = Wsocket()
        on_open = ws.on_open()
        on_send = ws.on_send()
        data = ws.on_data()
        on_date = ws.on_date()

        """ Formatting"""
        sls = Serializers()
        bid, ask = sls.formatting(data=data)
        date = sls.formatter_date(on_date)
        spread = sls.calculate_spread(bid=bid, ask=ask, date=date)

        """Queue"""
        q = Queue()
        bid_long, ask_long = q.loop(data)
        mean, count_ask, count_bid = q.calculate_long_spread()

        """Table"""
        table = PrettyTable()
        table.field_names = ["date", "last", "Bid price", "Ask price", "Spread"]
        table.add_row([date, 10, '{0:4f}'.format(count_bid), '{0:4f}'.format(count_ask), '{0:4f}'.format(mean)])
        print(table)

        """End"""
        # ws.shutdown()
        
    except ValueError:
        print("Oops!  Failed to open websocket...")

    

else:
    """Render template"""
    print('test...')
    class Render():

        def __init__(self, bid, ask, date):
            self.bid = bid
            self.ask = ask
            self.date = date


        def test():
            return bid, ask, date

    """ Websocket"""
    ws = Wsocket()
    on_open = ws.on_open()
    on_send = ws.on_send()
    data = ws.on_data()
    on_date = ws.on_date()

    """ Formatting"""
    sls = Serializers()
    bid, ask = sls.formatting(data=data)
    date = sls.formatter_date(on_date)

    Render(bid, ask, date)