class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

        def kiihdyta(self, nopeuden_muutos):
            uusi_nopeus = self.nopeus + nopeuden_muutos
            if uusi_nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif uusi_nopeus < 0:
                self.nopeus = 0
            else:
                self.nopeus = uusi_nopeus


if __name__ == "__main__":
    auto = Auto("ABC-123", 142)
    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)
    print(f"Auton nopeus: {auto.nopeus} km/h")
    auto.kiihdyta(-200)
    print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")