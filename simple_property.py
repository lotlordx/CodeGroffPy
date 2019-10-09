import datetime as d
from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return self.expires > NOW


something = Promo('Voilin', NOW + d.timedelta(days=1))
print(something.expired)
