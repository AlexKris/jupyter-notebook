import v20
from oanda_common import print_collection
from oanda_config import OandaConfig


def main():
    api = v20.Context(
        OandaConfig.hostname,
        OandaConfig.port,
        token=OandaConfig.token
    )

    response = api.account.instruments(
        accountID=OandaConfig.active_account
    )

    print("Response: {} ({})".format(response.status, response.reason))
    instruments = response.get('instruments', '200')

    instruments.sort(key=lambda i: i.name)

    def marginFmt(instrument):
        return "{:.0f}:1 ({})".format(
            1.0 / float(instrument.marginRate),
            instrument.marginRate
        )

    def pipFmt(instrument):
        location = float(10 ** instrument.pipLocation)
        return "{:.4f}".format(location)

    print_collection(
        "{} Instruments".format(len(instruments)),
        instruments,
        [
            ("Name", lambda i: i.name),
            ("Type", lambda i: i.type),
            ("Pip", pipFmt),
            ("Margin Rate", marginFmt),
        ]
    )

if __name__ == "__main__":
    main()
