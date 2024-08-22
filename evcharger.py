class ChargingStation:
    def __init__(self, name, location, total_slots, available_slots, charger_type):
        self.name = name
        self.location = location
        self.total_slots = total_slots
        self.available_slots = available_slots
        self.charger_type = charger_type

    def book_slot(self):
        if self.available_slots > 0:
            self.available_slots -= 1
            print(
                f"Slot booked successfully at {self.name}. {self.available_slots} slots remaining."
            )
        else:
            print(f"No slots available at {self.name}.")


class EVChargingSystem:
    def __init__(self):
        self.stations = []

    def register_station(self, name, location, total_slots, charger_type):
        station = ChargingStation(
            name, location, total_slots, total_slots, charger_type
        )
        self.stations.append(station)
        print(f"Charging station '{name}' registered successfully.")

    def find_stations(self, location=None, charger_type=None):
        filtered_stations = self.stations
        if location:
            filtered_stations = [
                station for station in filtered_stations if station.location == location
            ]
        if charger_type:
            filtered_stations = [
                station
                for station in filtered_stations
                if station.charger_type == charger_type
            ]

        if not filtered_stations:
            print("No stations found with the given filters.")
        else:
            for station in filtered_stations:
                print(
                    f"Station: {station.name}, Location: {station.location}, Available Slots: {station.available_slots}, Charger Type: {station.charger_type}"
                )

    def book_slot(self, station_name):
        for station in self.stations:
            if station.name == station_name:
                station.book_slot()
                return
        print(f"No station found with the name {station_name}.")


# Dynamic input and program execution
def main():
    system = EVChargingSystem()

    while True:
        print("\n1. Register Charging Station")
        print("2. Find Charging Stations")
        print("3. Book a Charging Slot")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter station name: ")
            location = input("Enter station location: ")
            total_slots = int(input("Enter total number of slots: "))
            charger_type = input("Enter charger type (e.g., fast, slow): ")
            system.register_station(name, location, total_slots, charger_type)

        elif choice == "2":
            location = input("Enter location to filter (or press Enter to skip): ")
            charger_type = input(
                "Enter charger type to filter (or press Enter to skip): "
            )
            system.find_stations(
                location if location else None, charger_type if charger_type else None
            )

        elif choice == "3":
            station_name = input("Enter the name of the station to book a slot: ")
            system.book_slot(station_name)

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
