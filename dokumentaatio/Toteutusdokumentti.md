## Ohjelman toteutus

### Ohjelman yleisrakenne

Ohjelma koostuu yhdestä luokasta, jossa on 4 metodia alkulukujen generointiin, ja toisesta RSA:n laskemisesta vastaavasta tiedostosta, sekä UI:sta.
1. `Primes`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Metodit:
    - `lowPrimes`  
      - Generoi listan pienistä alkuluvuista lukujen 2 ja 1000 väliltä.
    - `millerRabin`
      - Tarkistaa, onko annettu luku alkuluku käyttäen Miller-Rabin-testiä.
    - `checkPrimality`
      - Tarkistaa annetun alkuluvun laskutoimituksen "n modulo alkuluku" avulla, jolla voidaan
        poistaa suuri määrä jaollisia lukuja ennen Miller-Rabinin suorittamista sen nopeuttamiseksi.
    - `primeGeneration`
      - Generoidaan luku, ja tarkistetaan, onko se alkuluku.
2. `RSA`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Funktiot:
    - `generateKeys`
      - Funktio, joka generoi avaimet Primes-luokan ja RSA-algoritmin laskutoimituksilla.
    - `encrypt`
      - Funktio, joka enkryptoi selkokielisen viestin.
    - `decrypt`
      - Funktio, joka dekryptoi salatun viestin.
3. `GUI`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Funktiot:
    - `getValues`
      - Palauttaa generateKeys ja primeGeneration avulla luodut luvut.
    - `run`
      - Ajaa ohjelman ja käynnistää käyttöliittymän.
    - `_encrypt`
      - Enkryptoi ja tulostaa tuloksen käyttöliittymään.
    - `_decrypt`
      - Dekryptoi ja tulostaa tuloksen käyttöliittymään.

### Lähteet
Wikipedia: https://en.wikipedia.org/wiki/Miller-Rabin_primality_test  
Cormen, T. H., Leiserson, C. E., Rivest , R. L., Stein, C. Introduction to Algorithms (2001): section 33.8: Rabin-Miller primality test  
Weissman, M. H., & American Mathematical Society,. (2017). An illustrated theory of numbers (& notebooks)  



