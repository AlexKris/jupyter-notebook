import v20
from oanda_common import print_collection
from oanda_config import OandaConfig


def main():
    api = v20.Context(
        OandaConfig.hostname,
        OandaConfig.port,
        token=OandaConfig.token
    )

    response = api.account.list()

    print("Response: {} ({})".format(response.status, response.reason))
    accounts = response.get('accounts', '200')
    print_collection(
        "{} Accounts".format(len(accounts)),
        accounts,
        [
            ("id", lambda a: a.id),
            ("tags", lambda a: a.tags)
        ]
    )

if __name__ == "__main__":
    main()
