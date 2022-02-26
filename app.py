#!/usr/bin/python3
from flask import Flask, request, render_template, url_for
from settings import PORT, DEBUG
from socket_test import Serializers, Wsocket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Trading(self):
    if request.method == 'GET':

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
        spread = sls.calculate_spread(bid=bid, ask=ask)

        return render_template('template.index.html', date=date)

    else:
        return render_template('template.400.html')

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)