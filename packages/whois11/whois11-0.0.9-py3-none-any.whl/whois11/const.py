class Const:
    MAX_BUF_LEN = 4096
    SOCKET_TIMEOUT = 3
    HOST_IANA = "www.iana.org"
    PORT_WHOIS = 43
    PORT_SSL = 443
    QUERY_URL = "/whois?q="
    USER_AGENT = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko"

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        raise self.ConstError("Can't rebind const (%s)" % name)


const = Const()
