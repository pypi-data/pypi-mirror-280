import socket
from .const import const
from .whois_server import WhoisServer


class Whois:

    @classmethod
    def get_whois_info(cls, domain_name, print_iana_info_flag=False):

        iana_info, whois_server = WhoisServer.get_whois_server(domain_name, print_iana_info_flag)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(const.SOCKET_TIMEOUT)
        client.connect((whois_server, const.PORT_WHOIS))
        client.send((domain_name + "\r\n").encode("utf-8"))
        
        ref = []
        while True:
            buf = client.recv(const.MAX_BUF_LEN)
            if buf == b'':
                break
            ref.append(buf)

        client.close()

        whois_info = b''.join(ref).decode("utf-8")

        iana_info_str = ""
        if print_iana_info_flag:
            iana_info_str = "\n".join(iana_info) + "-*"*50 + "-\n\n"

        return iana_info_str + whois_info
