class Stockroom:
    def __init__(self):
        self.dict = {}

    def add_to_stock(self, peripheral_device):
        self.dict.setdefault(peripheral_device.group_name(), []).append(peripheral_device)

    def get_info(self, device_name):
        if self.dict[device_name]:
            self.dict.setdefault(device_name).pop(0)


class Periphery:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f"{self.group}"

    def __repr__(self):
        return f"{self.name} {self.year}"


class Printer(Periphery):
    def __init__(self, name, year, print_type, print_color):
        super().__init__(name, year)
        self.print_type = print_type
        self.print_color = print_color

    def __repr__(self):
        return f"{self.name} {self.year} {self.print_type} {self.print_color}"


class Scan(Periphery):
    def __init__(self, name, year, dpi):
        super().__init__(name, year)
        self.dpi = dpi

    def __repr__(self):
        return f"{self.name} {self.year} {self.dpi}"


class Xerox(Periphery):
    def __init__(self, name, year, all_in_one, print_color):
        super().__init__(name, year)
        self.all_in_one = all_in_one
        self.print_color = print_color

    def __repr__(self):
        return f"{self.name} {self.year} {self.all_in_one} {self.print_color}"


my_stock = Stockroom()
printer_1 = Printer("Canon", "2020", "Laser", "RGBb print")
my_stock.add_to_stock(printer_1)
printer_2 = Printer("Philips", "2019", "Laser", "Grayscale")
my_stock.add_to_stock(printer_2)
scan_1 = Scan("Epson", "2020", "3200x4000 dpi")
my_stock.add_to_stock(scan_1)
xerox_1 = Xerox("Xerox", "2020", "Yes", "RGBb")
my_stock.add_to_stock(xerox_1)

print(my_stock.dict)
