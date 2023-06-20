import v20
from oanda_common import heartbeat_to_string, price_to_string
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
        token=OandaConfig.token,
    )

    instruments = 'AUD_USD,EUR_USD,USD_JPY,GBP_USD,NZD_USD,USD_CHF,USD_CAD,USD_CNH'

    response = api.pricing.stream(
        OandaConfig.active_account,
        snapshot=True,
        instruments=instruments
    )

    for msg_type, msg in response.parts():
        if msg_type == "pricing.Heartbeat":
            print(heartbeat_to_string(msg))
        elif msg_type == "pricing.Price":
            print(price_to_string(msg))

if __name__ == "__main__":
    main()
