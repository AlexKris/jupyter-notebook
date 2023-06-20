import sys
from datetime import datetime

from tabulate import tabulate


def print_title(s):
    """
    Print a string as a title with a strong underline

    Args:
        s: string to print as a title
    """
    print(s)
    print(len(s) * "=")
    print("")

def print_collection(title, entities, columns):
    """
    Print a collection of entities with specified headers and formatters

    Args:
        title: The title to print
        entities: The collection to print, one per row in the table
        columns:  Tuple of column header name and column row formatter to be
                  applied to each entity in the collection
    """

    if len(entities) == 0:
        return

    if title is not None and len(title) > 0:
        print_title(title)

    headers = [c[0] for c in columns]
    tablefmt = "rst"
    body = []

    for e in entities:
        body.append([c[1](e) for c in columns])

    getattr(sys.stdout, 'buffer', sys.stdout).write(
        tabulate
        (
            body,
            headers,
            tablefmt=tablefmt,
        ).encode('utf-8')
    )
    print("")

class CandlePrinter(object):
    def __init__(self):
        self.width = {
            'time': 19,
            'type': 4,
            'price': 8,
            'volume': 6,
        }
        # setattr(self.width, "time", 19)
        self.time_width = 19

    def print_header(self):
        print(
            "{:<{width[time]}} {:<{width[type]}} {:<{width[price]}} "
            "{:<{width[price]}} {:<{width[price]}} {:<{width[price]}} "
            "{:<{width[volume]}}".format(
                "Time",
                "Type",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                width=self.width
            )
        )

        print("{} {} {} {} {} {} {}".format(
            "=" * self.width['time'],
            "=" * self.width['type'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['price'],
            "=" * self.width['volume']
        ))

    def print_candle(self, candle):
        try:
            time = str(
                datetime.strptime(
                    candle.time,
                    "%Y-%m-%dT%H:%M:%S.000000000Z"
                )
            )
        except Exception:
            time = candle.time.split(".")[0]

        volume = candle.volume

        for price in ["mid", "bid", "ask"]:
            c = getattr(candle, price, None)

            if c is None:
                continue

            print(
                "{:>{width[time]}} {:>{width[type]}} {:>{width[price]}} "
                "{:>{width[price]}} {:>{width[price]}} {:>{width[price]}} "
                "{:>{width[volume]}}".format(
                    time,
                    price,
                    c.o,
                    c.h,
                    c.l,
                    c.c,
                    volume,
                    width=self.width
                )
            )

            volume = ""
            time = ""

def price_to_string(price):
    return "{} ({}) {}/{}".format(
        price.instrument,
        price.time,
        price.bids[0].price,
        price.asks[0].price
    )

def heartbeat_to_string(heartbeat):
    return "HEARTBEAT ({})".format(
        heartbeat.time
    )
