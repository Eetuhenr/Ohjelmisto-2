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


class Talo:
    def __init__(self, alimman_kerroksen_numero, ylimman_kerroksen_numero, hissien_lukumaara):
        self.alimman_kerroksen_numero = alimman_kerroksen_numero
        self.ylimman_kerroksen_numero = ylimman_kerroksen_numero
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit = [Hissi(alimman_kerroksen_numero, ylimman_kerroksen_numero) for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 1 <= hissin_numero <= self.hissien_lukumaara:
            hissi = self.hissit[hissin_numero - 1]
            print(f"\nAjetaan hissi {hissin_numero} kerrokseen {kohde_kerros}:")
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virheellinen hissin numero.")
            if __name__ == "__main__":
                talo = Talo(1, 10, 3)
                talo.aja_hissiä(1, 5)
                talo.aja_hissiä(2, 7)
                talo.aja_hissiä(3, 3)
                talo.aja_hissiä(1, 1)