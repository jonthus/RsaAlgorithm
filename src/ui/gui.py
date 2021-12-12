
import tkinter as tk
import Primes
import RSA

class GUI:

    def __init__(self):
        self.init = Primes.Primes()
        self.p = self.init.primeGeneration(1024)
        self.q = self.init.primeGeneration(1024)
        self.e, self.d, self.n = RSA.generateKeys(self.p, self.q)

    def getValues(self):
        return self.e, self.d, self.n

    def run(self):
        self.root = tk.Tk()
        self.root.title('RSA-salaus')

        self.label = tk.Label(master=self.root,text='Syötä viesti enkryptoitavaksi')
        self.label.pack()

        self.value1 = tk.Entry(master=self.root)
        self.value1.pack()

        self.button = tk.Button(master=self.root, text="Enkryptoi", command=self._encrypt)
        self.button.pack()

        self.show = tk.Label(master=self.root, text="Enkryptoitu teksti:")
        self.show.pack()

        self.listbox = tk.Listbox(master=self.root, height=10, width=200)
        self.listbox.pack()

        self.label = tk.Label(master=self.root,text='Syötä enkryptoitu teksti purettavaksi')
        self.label.pack()

        self.value2 = tk.Entry(master=self.root)
        self.value2.pack()

        self.button2 = tk.Button(master=self.root,text="Dekryptoi", command=self._decrypt)
        self.button2.pack()

        self.show2 = tk.Label(master=self.root,text='Dekryptoitu teksti:')
        self.show2.pack()
        self.listbox2 = tk.Listbox(master=self.root, height=10, width=200)
        self.listbox2.pack()

        self.root.mainloop()

    def _encrypt(self):
        e, d, n = init.getValues()
        plaintext = self.value1.get()
        enc = RSA.encryption(plaintext, e, n)
        self.listbox.insert(0, enc)

    def _decrypt(self):
        e, d, n = init.getValues()
        plaintext = self.value1.get()
        ciphertext = RSA.encryption(plaintext, e, n)
        dec = RSA.decryption(ciphertext, d, n)
        self.listbox2.insert(0, dec)

if __name__ == '__main__':
    init = GUI()
    init.run()