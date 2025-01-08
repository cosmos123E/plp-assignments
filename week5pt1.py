class Device:
    """
    A base class for all devices.
    """
    def __init__(self, brand, model, price):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.price = price  # Public attribute

    # Getter for brand
    def get_brand(self):
        return self.__brand

    # Getter for model
    def get_model(self):
        return self.__model

    # Method to display device info
    def display_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Price: ${self.price}"


class Smartphone(Device):
    """
    A class representing a smartphone, inheriting from Device.
    """
    def __init__(self, brand, model, price, os, storage):
        super().__init__(brand, model, price)  # Initialize parent class attributes
        self.os = os  # Public attribute
        self.storage = storage  # Public attribute

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.get_model()}..."

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, OS: {self.os}, Storage: {self.storage}GB"


class GamingSmartphone(Smartphone):
    """
    A class representing a gaming smartphone, inheriting from Smartphone.
    """
    def __init__(self, brand, model, price, os, storage, gpu):
        super().__init__(brand, model, price, os, storage)
        self.gpu = gpu  # Additional attribute for gaming smartphones

    def play_game(self, game_name):
        return f"Playing {game_name} with {self.gpu} on {self.get_model()}..."

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, GPU: {self.gpu}"


# Creating objects
basic_phone = Device("Generic", "D100", 50)
smartphone = Smartphone("Samsung", "Galaxy S21", 799, "Android", 128)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 999, "Android", 256, "Adreno 730")

# Using methods
print(basic_phone.display_info())
print(smartphone.display_info())
print(smartphone.install_app("WhatsApp"))
print(gaming_phone.display_info())
print(gaming_phone.play_game("Genshin Impact"))
