## Työn aihe
Työn aiheena on RSA-salausalgoritmi (Rivest-Shamir-Adleman, 1978). RSA-salaus on asymmetrinen (kaksiavaiminen) kryptografian algoritmi, jolla on mahdollista
enkryptoida ja dekryptoida viestejä. Algoritmin salausteho perustuu alkulukuihin, ja siihen, että alkulukujen tekijöihin jako on vaikeaa, varsinkin kun kyseesssä on suuria alkulukuja.\
\
Ohjelmointikieli: Työssä käytetty kieli on Python. Hallitsen myös Java, C# 
vertaisarviointia varten.\
Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma\
Dokumentointikieli: Suomi
##### Algoritmin rakenne on seuraavanlainen:
- Generoidaan kaksi alkulukua p ja q, joiden tulo on vähintään. 
 (2^1024).
##### Generointi tehdään seuraavasti:
- Generoidaan alkuluku.
- Testataan, onko generoitu alkuluku Miller-Rabin -testin avulla.
##### Kun alkuluvut löydetty: 
- Lasketaan N, joka on lukujen p ja q tulo.
- Lasketaan phi(N) = (p-1)*(q-1).
- Valitaan e, joka on suurempi kuin 1 ja jolla ei ole yhteisiä tekijöitä (GCD)
termien (p-1) ja (q-1) kanssa. Tässä työssä e = 65537.
- (e, N) on julkinen avain.
- Lasketaan d kaavan 1 = ed mod phi(N) (EEA, Extended Euclidean
Algorithm) avulla.
- (d, N) on salainen avain.
##### Enkryptio ja dekryptio:
- Enkryptoidaan viesti kaavalla C = M^e mod N
- Dekryptoidaan viesti kaavalla M = C^d mod N
- Verrataan, ovatko viestit C ja M samat.

### Työssä käytetyt tietorakenteet ja algoritmit:
- Työssä käytetään RSA algoritmia viestien enkryptioon ja dekryptioon.
- Alkulukujen primaalisuuden tarkistamiseen käytetään Miller-Rabin -testiä.
- Käytetään yhteisten tekijöiden laskemiseksi Extended Euclidean Algorithm (EEA).

### Ohjelman syötteet:
- Ohjelmaan syötetään pitkähkö merkkijono, joka on mahdollista enkryptoida ja
dekryptoida ohjelman avulla. Syöte tarkistetaan oikeanlaiseksi (ei sisällä
erikoismerkkejä tai muita kuin UTF-8). Ohjelma palauttaa enkryptoidun merkkijonon, ja tiedon siitä,
onnistuiko enkryptio sekä dekryptio.

### Aika- ja tilavaativuuksien tavoitteet:
- RSA Algoritmin aika- ja tilavuusvaativuudet riippuvat suurilta osin sen 
toteutusmetodista. O-analyysi tehdään tässä suunnitellun rakenteen perusteella.
- Oletetaan, että RSA algoritmin laskeminen on jaettu seuraaviin vaiheisiin:
##### 1. Alkulukujen P ja Q generointi
- Python-dokumentaation mukaan random.randint(0, N) on O(log n).
- Alkuluvun primaalisuuden tarkistamiseen käytetään Miller-Rabin -testiä, jonka
aikakompleksisuus on O(k log^3 n). (Wikipedia).
##### 2. Alkulukujen tulo N = P*Q
- Kertolaskun aikakompleksisuus on O(n*n) eli O(n^2) (Wikipedia).
##### 3. EEA (Extended Euclidean Algorithm).
- EEA:n aikavaativuus on O(log^3 n) pahimmassa tapauksessa. (Knuth, D.E. 1997)
##### 4. Enkryptio ja dekryptio:
- Enkryptiolla sekä dekryptiolla on modulaarilaskennan mukaisesti pahimmassa
tapauksessa aikavaativuus O(M(n)2^k). (Wikipedia)\
Tässä esitetyt aikavaativuudet ovat arvioita, jotka tulevat muuttumaan
projektin kehittyessä eteenpäin.\
\
Lähteet:
Python-dokumentaatio: 'https://hg.python.org/cpython/file/3.4/Modules/_randommodule.c#l93' \
Knuth, D. E. (1997), The Art of Computer Programming, Volume 2: Seminumerical
Algorithms (3rd ed.).\
https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations
