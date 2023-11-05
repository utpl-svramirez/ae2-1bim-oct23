class empresa:
    def __init__(self, nombre, sector_economico, cant_sucursales):
        self.nombre = nombre
        self.sector_economico = sector_economico
        self.cant_sucursales = cant_sucursales

    def get_nombre(self):
        return self.nombre

    def get_sector_economico(self):
        return self.get_sector_economico

    def get_cant_sucursales(self):
        return self.cant_sucursales

    def set_nombre(self, nombre_registro):
        self.nombre = nombre_registro

    def set_sector_economico(self, sector_economico_registro):
        self.sector_economico = sector_economico_registro

    def set_cant_sucursales(self, cant_sucursales_act):
        self.cant_sucursales = cant_sucursales_act