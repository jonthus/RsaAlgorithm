## Ohjelman toteutus

### Ohjelman yleisrakenne

Ohjelma koostuu yhdestä luokasta, jossa on 4 metodia alkulukujen generointiin, ja toisesta RSA:n laskemisesta vastaavasta tiedostosta, sekä UI:sta.
1. `Primes`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Metodit:
    - `lowPrimes`
    - `millerRabin`
    - `checkPrimality`
    - `primeGeneration`
2. `RSA`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Metodit:
    - `generateKeys`
    - `encrypt`
    - `decrypt`
3. `GUI`
  - Luokka, jonka avulla generoidaan alkulukuja.  
  - ##### Metodit:
    - `getValues`
    - `run`
    - `_encrypt`
    - `_decrypt`

### Saavutetut aika- ja tilavaativuudet

### Suorituskyky- ja O-analyysivertailu

### Lähteet
Wikipedia: https://en.wikipedia.org/wiki/Miller-Rabin_primality_test  
Cormen, T. H., Leiserson, C. E., Rivest , R. L., Stein, C. Introduction to Algorithms (2001): section 33.8: Rabin-Miller primality test  
Weissman, M. H., & American Mathematical Society,. (2017). An illustrated theory of numbers (& notebooks)  



