class Hissi:
    def __init__(self, alimman_kerroksen_numero, ylimman_kerroksen_numero):
        self.alimman_kerroksen_numero = alimman_kerroksen_numero
        self.ylimman_kerroksen_numero = ylimman_kerroksen_numero
        self.kerros = alimman_kerroksen_numero

    def siirry_kerrokseen(self, tavoite_kerros):
        while self.kerros < tavoite_kerros:
            self.kerros_ylös()
        while self.kerros > tavoite_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylimman_kerroksen_numero:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alimman_kerroksen_numero:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")
if __name__ == "__main__":
    hissi = Hissi(1, 10)
    print("Siirretään hissi kerrokseen 5:")
    hissi.siirry_kerrokseen(5)
    print("\nSiirretään hissi alimpaan kerrokseen:")
    hissi.siirry_kerrokseen(1)