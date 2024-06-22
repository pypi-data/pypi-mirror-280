class EuropeanSocket:
    def plug_in(self):
        return "220V"

class AmericanSocket:
    def plug_in(self):
        return "110V"

class Adapter:
    def __init__(self, socket):
        self.socket = socket

    def plug_in(self):
        if isinstance(self.socket, EuropeanSocket):
            return "Adapter converts 220V to 110V -> " + self.socket.plug_in()
        else:
            return self.socket.plug_in()

# Usage
european_socket = EuropeanSocket()
adapter = Adapter(european_socket)
print(adapter.plug_in())

american_socket = AmericanSocket()
adapter = Adapter(american_socket)
print(adapter.plug_in())
