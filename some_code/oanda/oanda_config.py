import configparser

config = configparser.ConfigParser()
config.read('../config/oanda.ini', encoding='utf-8')

class OandaConfig(object):

    hostname = config.get('oanda', 'hostname')
    streaming_hostname = config.get('oanda', 'streaming_hostname')
    port = config.getint('oanda', 'port')
    ssl = config.getboolean('oanda', 'ssl')
    token = config.get('oanda', 'token')
    username = None
    accounts = config.get('oanda', 'accounts').split(',')
    active_account = config.get('oanda', 'active_account')
    path = None
    datetime_format = config.get('oanda', 'datetime_format')

    def __str__(self):
        """
        Create the string (YAML) representation of the Config instance
        """

        s = ""
        s += "hostname: {}\n".format(self.hostname)
        s += "streaming_hostname: {}\n".format(self.streaming_hostname)
        s += "port: {}\n".format(self.port)
        s += "ssl: {}\n".format(str(self.ssl).lower())
        s += "token: {}\n".format(self.token)
        s += "username: {}\n".format(self.username)
        s += "datetime_format: {}\n".format(self.datetime_format)
        s += "accounts:\n"
        for a in self.accounts:
            s += "- {}\n".format(a)
        s += "active_account: {}".format(self.active_account)

        return s

if __name__ == '__main__':
    print(OandaConfig())