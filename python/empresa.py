class empresa:
    def __init__(self, nombre, sector, cant_sucursales):
        self.nombre = nombre
        self.sector = sector
        self.cant_sucursales = cant_sucursales

    def get_nombre(self):
        return self.nombre

    def get_sector(self):
        return self.sector

    def get_cant_sucursales(self):
        return self.cant_sucursales

    def set_nombre(self, nombre_registro):
        self.nombre = nombre_registro

    def set_sector(self, sector_registro):
        self.sector = sector_registro

    def set_cant_sucursales(self, cant_sucursales_act):
        self.cant_sucursales = cant_sucursales_act