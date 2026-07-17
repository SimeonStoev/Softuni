class EntertainmentDeviceViaHDMI:
    def connect_to_device_via_hdmi_cable(self, device): pass


class EntertainmentDeviceViaRCA:
    def connect_to_device_via_rca_cable(self, device): pass


class EntertainmentDeviceViaEthernet:
    def connect_to_device_via_ethernet_cable(self, device): pass


class EntertainmentDevice:

    def connect_device_to_power_outlet(self, device): pass

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Television(EntertainmentDevice, EntertainmentDeviceViaHDMI, EntertainmentDeviceViaRCA):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)


class DVDPlayer(EntertainmentDevice, EntertainmentDeviceViaHDMI):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)


class GameConsole(EntertainmentDevice, EntertainmentDeviceViaHDMI, EntertainmentDeviceViaEthernet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)


class Router(EntertainmentDevice, EntertainmentDeviceViaEthernet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)
