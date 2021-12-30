### Käyttöohje:

Ohjelman suoritus ja asennus tapahtuu `src`-kansiossa.

#### Asennus

    Jos poetry ei asennettu, niin ->
    pip3 install poetry
    
    Tämän jälkeen ->
    poetry install
    
#### Ohjelman suoritus

    Varmista, että olet `src`-kansiossa!
    poetry run invoke start

Ohjelma käynnistää yllä olevalla komennolla. Ohjelmaan syötetään enkryptoitavaksi haluttu merkkijono. Painamalla Enkryptoi-nappia kyseinen viesti salataan. Salattu viesti tulostetaan näytölle. Salatun viestin voi purkaa kopioimalla ja liittämällä salatun viestin tekstikenttään, ja painamalla Dekryptoi-nappia. Purettu viesti tulostetaan näytölle. Ohjelma hyväksyy numero- ja tekstimuotoisia syötteitä. Huomioitavaa on kuitenkin, että ohjelman toiminta hidastuu suurilla syötteillä.  

#### Ohjelman testaus
    
    poetry run invoke test
    poetry run invoke coverage-report
    poetry run invoke pylint
    
Ohjelmaa voi testata yllä olevien komentojen avulla. Ensimmäinen komento näyttää unittestien tulokset. Toinen komento tulostaa unittestien kattavuuden
graafisessa muodossa kansioon `htmlcov/index.html`. Kolmas komento näyttää koodin laatutestauksen tulokset.
    
