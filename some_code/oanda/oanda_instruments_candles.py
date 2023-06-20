import v20
from oanda_common import CandlePrinter, print_collection
from oanda_config import OandaConfig


def main():
    """
    AUD_USD: 澳元/美元
    EUR_USD: 欧元/美元
    USD_JPY: 美元/日元
    GBP_USD: 英镑/美元
    NZD_USD: 新西兰元/美元
    USD_CHF: 美元/瑞士法郎
    USD_CAD: 美元/加元
    USD_CNH: 美元/人民币（离岸）
    """
    api = v20.Context(
        OandaConfig.hostname,
        OandaConfig.port,
        token=OandaConfig.token
    )

    kwargs = {
        'fromTime': '2023-05-01',
        # 'toTime': '2023-05-02 00:00:00',
        'granularity': 'M1'
    }

    response = api.instrument.candles(
        'AUD_USD',
        **kwargs
    )

    print("Response: {} ({})".format(response.status, response.reason))

    if response.status != 200:
        print(response)
        print(response.body)
        return

    print("Instrument: {}".format(response.get("instrument", 200)))
    print("Granularity: {}".format(response.get("granularity", 200)))

    printer = CandlePrinter()

    printer.print_header()

    for candle in response.get("candles", 200):
        printer.print_candle(candle)

if __name__ == "__main__":
    main()
