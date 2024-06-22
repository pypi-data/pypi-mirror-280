import socket
import ssl
from .const import const
from . import errors


class WhoisServer:

    @classmethod
    def get_whois_server(cls, domain_name, print_iana_info_flag=False):

        query = const.QUERY_URL + domain_name
        req = ("GET {0} HTTP/1.1\r\n"
               "Host: {1}\r\n"
               "User-Agent: {2}\r\n"
               "Connection: close\r\n"
               "\r\n")
        req = req.format(query, const.HOST_IANA, const.USER_AGENT).encode("utf-8")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(const.SOCKET_TIMEOUT)
        client.connect((const.HOST_IANA, const.PORT_SSL))
        # client = ssl.wrap_socket(client,
        #                          keyfile=None,
        #                          certfile=None,
        #                          server_side=False,
        #                          cert_reqs=ssl.CERT_NONE,
        #                          ssl_version=ssl.PROTOCOL_SSLv23)

        # Compatible with Python3.12
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        client = context.wrap_socket(client, server_hostname=None)
        client.sendall(req)

        res = []
        while True:
            buf = client.recv(const.MAX_BUF_LEN)
            if buf == b'':
                break
            res.append(buf)

        client.close()

        s = b''.join(res).decode("utf-8").split("\n")

        if len(s) >= 0:
            if s[0].find(" 200 OK") == -1:
                raise errors.WhoisError("could not get whois server: [HTTP error]")

        iana_info = []
        if print_iana_info_flag:
            print_flag = False
            for x in s:
                if x.find("</pre>") >= 0:
                    print_flag = False
                if print_flag:
                    # print(x)
                    iana_info.append(x)
                if x.find("<pre>") >= 0:
                    print_flag = True
                    # print(x[x.find("<pre>") + 5:])
                    iana_info.append(x[x.find("<pre>") + 5:])

        whois_server = ""
        for x in s:
            if x.find("whois:") != -1:
                x = x.split(" ")
                if len(x) >= 2:
                    whois_server = x[-1]

        if whois_server == "":
            raise errors.WhoisError("could not get whois server: [whois server parse error]")

        return iana_info, whois_server
