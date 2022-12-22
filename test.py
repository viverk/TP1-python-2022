import csv


class Airport:
    def __init__(self, name: str, code: str, lat: float, long: float) -> None:
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long


class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float) -> None:
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration


class FlightMap:

    def __init__(self) -> None:
        self.listAirports = []
        self.listFlights = []

    def import_airports(self, csv_file: str) -> None:
        listAirports = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='"')
            for row in reader:
                """ print(row[0]) """
                a = Airport(row[0], row[1], row[2], row[3])
                self.listAirports.append(a)

    def import_flights(self, csv_file: str) -> None:
        listFlights = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='"')
            for row in reader:
                """ print(row[0]) """
                f = Flight(row[0], row[1], row[2])
                self.listFlights.append(f)

    def airports(self) -> list[Airport]:
        self.import_airports("aeroports.csv")
        """ print(self.listAirports[0].name) """
        return self.listAirports

    def flights(self) -> list[Flight]:
        self.import_flights("flights.csv")
        """ print(self.listFlights[0].src_code) """
        return self.listFlights

    def airport_find(self, airport_code: str) -> Airport:
        for x in self.airports():
            """ print(x.code) """
            if (airport_code in x.code):
                return x

        return None

    def flight_exist(self, src_airport_code: str, dst_airport_code: str):
        for x in self.flights():
            if (src_airport_code in x.src_code):
                if (dst_airport_code in x.dst_code):
                    return True
            if (src_airport_code in x.dst_code):
                if (dst_airport_code in x.src_code):
                    return True
        return False

    def flights_where(self, airport_code: str) -> list[Flight]:
        listVol = []
        for x in self.flights():
            if (airport_code in x.src_code):
                listVol.append(x)
            if (airport_code in x.dst_code):
                listVol.append(x)

        return listVol

    def airports_from(self, airport_code: str) -> list[Airport]:
        listAirport = []
        for x in self.flights():
            if (airport_code in x.src_code):
                for y in self.airports():
                    if (x.dst_code in y.code):
                        if (y not in listAirport):
                            listAirport.append(y)
        return listAirport


class FlightPathBroken(Exception):
    pass


class FlightPathDuplicate(Exception):
    pass


class FlightPath:
    def __init__(self, src_airport: Airport) -> None:
        self.path = [src_airport]

    def add(self, dst_airport: Airport, via_flight: Flight) -> None:
        if self.path[-1] != via_flight.src_airport:
            raise FlightPathBroken(
                "erreur flightPathBroken")
        self.path.append(via_flight)
        self.path.append(dst_airport)

    def flights(self) -> list[Flight]:
        return [self.path[i] for i in range(1, len(self.path), 2)]

    def airports(self) -> list[Airport]:
        return [self.path[i] for i in range(0, len(self.path), 2)]

    def steps(self) -> float:
        return len(self.flights())

    def duration(self) -> float:
        return sum(f.duration for f in self.flights())


obj = FlightMap()

""" obj.airports() """

""" obj.flights() """

""" print(obj.airport_find("FRA")) """

""" print(obj.flight_exist("FRA", "LOS")) """

""" print(obj.flights_where("FRA")) """

""" print(obj.airports_from("FRA")[2].name) """
