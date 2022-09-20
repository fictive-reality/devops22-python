from cmd import Cmd
from ipaddress import ip_address, ip_network


class NetworkTool(Cmd):
    intro = 'Welcome to the Amazing Network Tool.\tType help or ? to list commands.\n'
    prompt = '(net) '

    def do_bye(self, arg):
        'Stop the tool and exit:  BYE'
        print('Thank you for using Amazing Network Tool')
        return True

    def do_valid_ip(self, arg):
        'Validate a ip address'
        try:
            ip_address(arg)
            print(f"Your ip {arg} is amazing!!")
        except Exception as e:
            print(e)

    def do_get_network(self, arg):
        'Get network hosts'
        try:
            network = ip_network(arg)
            print("\n".join(map(str, network)))
        except Exception as e:
            print(e)

    def precmd(self, line):
        line = line.lower()
        return line


if __name__ == '__main__':
    NetworkTool().cmdloop()
