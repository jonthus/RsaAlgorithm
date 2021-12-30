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
  - RSA:n avulla generoidaan avaimet, sekä enkryptoidaan selkoteksti, ja dekryptoidaan salattu viesti.  
  - ##### Funktiot:
    - `generateKeys`
      - Funktio, joka generoi avaimet Primes-luokan ja RSA-algoritmin laskutoimituksilla.
    - `encrypt`
      - Funktio, joka enkryptoi selkokielisen viestin.
    - `decrypt`
      - Funktio, joka dekryptoi salatun viestin.
3. `GUI`
  - Käyttöliittymä, joka tulostaa salatun tekstin ja avaimet.    
  - ##### Funktiot:
    - `getValues`
      - Palauttaa generateKeys ja primeGeneration avulla luodut luvut.
    - `run`
      - Ajaa ohjelman ja käynnistää käyttöliittymän.
    - `_encrypt`
      - Enkryptoi ja tulostaa tuloksen käyttöliittymään.
    - `_decrypt`
      - Dekryptoi ja tulostaa tuloksen käyttöliittymään.

### Miller-Rabin-testin O-analyysi pseudokoodista

#### Pseudokoodi

Jos kumpikaan seuraavista ehdoista tosi, niin n on todennäköisesti alkuluku:  
  - a^d*2^r on kongruentti -1 (mod n), kun 0 < r < s  
  - a^d on kongruentti 1 (mod n)
Muutoin luku on jaollinen luku.

Alla oleva pseudokoodi on omaan työhön sovellettu versio Wikipedian Miller-Rabin -testin pseudokoodista.  
Koodin syötteeksi oletetaan:
  - n: 1024-bittinen generoitu luku, josta testataan, onko se alkuluku.
  - k: testikierrosten määrä, joka vaikuttaa testin tarkkuuteen.  
       Miller-Rabin testin tarkkuus luvulle n on noin 4^-k, eli se on 
       4^-k todennäköisyydellä mahdollisesti alkuluku.
```
write n as 2^r·d + 1 with d odd (by factoring out powers of 2 from n − 1)

repeat k times  
  pick a random integer a in the range [2, n − 2]  
    x = a^d mod n  
    if x = 1 or x = n − 1 then  
        continue  
    repeat r − 1 times:  
        x = x^2 mod n  
        if x = n − 1 then  
            continue  
    return “composite”  
return “prime”  
```


Algoritmin nopeus on O(k log^3 n), jossa k on testien määrä, log n modulaarikertolaskusta ja ^3 kertolaskujen määrästä.





### Parannusehdotuksia
Alkulukujen generoinnin aikavaativuudessa on suuria heittelyitä 1024-bittisistä alkuluvuista eteenpäin, johtuen todennäköisesti `millerRabin` -metodin implementaatiosta. Tämä on huomattavissa tapauksissa, jossa se joutuu käymään kaikki 40 testikierrosta läpi, ennen kuin se löytää alkuluvun.

### Lähteet
Wikipedia: https://en.wikipedia.org/wiki/Miller-Rabin_primality_test  
Cormen, T. H., Leiserson, C. E., Rivest , R. L., Stein, C. Introduction to Algorithms (2001): section 33.8: Rabin-Miller primality test  
Weissman, M. H., & American Mathematical Society,. (2017). An illustrated theory of numbers (& notebooks)  



