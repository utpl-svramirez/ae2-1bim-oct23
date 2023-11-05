class empresa:
    def __init__(self, nombre, sector, años_activa):
        self.nombre = nombre
        self.sector = sector
        self.años_activa = años_activa

    def get_nombre(self):
        return self.nombre

    def get_sector(self):
        return self.sector

    def get_años_activa(self):
        return self.años_activa

    def set_nombre(self, nombre_registro):
        self.nombre = nombre_registro

    def set_sector(self, sector_registro):
        self.sector = sector_registro

    def set_años_activa(self, años_activa_act):
        self.faños_activa = años_activa_act