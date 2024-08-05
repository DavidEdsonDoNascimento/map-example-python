class Place:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_name(self):
        return self.name

    def get_coord(self):
        return [self.lat, self.lon]
