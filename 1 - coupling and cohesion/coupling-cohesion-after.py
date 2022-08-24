import string
import random


class VehicleInfo:
    def __init__(self, brand: str, is_electric: bool, catalogue_price: float) -> None:
        self.brand: str = brand
        self.is_electric: bool = is_electric
        self.catalogue_price: float = catalogue_price

    def compute_tax(self) -> float:
        tax_percentage: float = 0.05
        if self.is_electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    def __init__(self, vehicle_id: str, license_plate_id: str, info: VehicleInfo):
        self.vehicle_id: str = vehicle_id
        self.license_plate_id: str = license_plate_id
        self.info: VehicleInfo = info

    def print(self) -> None:
        print(f"Id: {self.vehicle_id}")
        print(f"License plate: {self.license_plate_id}")
        self.info.print()


class VehicleRegistry:
    def __init__(self):
        self.vehicle_info: dict[str:float] = {}
        self.add_vehicle_info("Tesla Model 3", True, 60000.0)
        self.add_vehicle_info("Volkswagen ID3", True, 35000.0)
        self.add_vehicle_info("BMW 5", False, 45000.0)
        self.add_vehicle_info("Tesla Model Y", True, 75000.0)

    def add_vehicle_info(
        self, brand: str, is_electric: bool, catalogue_price: float
    ) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand, is_electric, catalogue_price)

    @staticmethod
    def generate_vehicle_id(length: int):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(vehicle_id: str):
        return (
            f"{vehicle_id[:2]}-"
            + f"{''.join(random.choices(string.digits, k=2))}-"
            + f"{''.join(random.choices(string.ascii_uppercase, k=2))}"
        )

    def create_vehicle(self, brand: str):
        vehicle_id: str = self.generate_vehicle_id(12)
        license_plate: str = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    @staticmethod
    def register_vehicle(brand: str):
        # create a registry instance
        registry = VehicleRegistry()

        vehicle: Vehicle = registry.create_vehicle(brand)

        # print out the vehicle information
        vehicle.print()


app = Application()
app.register_vehicle("Volkswagen ID3")
