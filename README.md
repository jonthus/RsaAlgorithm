## RSA Algoritmi
RSA Algoritmin toteutus Pythonilla HY:n Tietorakenteet ja Algoritmit harjoitustyökurssia varten.

### Dokumentaatio:
[Määrittelydokumentti](./dokumentaatio/Määrittelydokumentti.md)  
[Toteutusdokumentti](./dokumentaatio/Toteutusdokumentti.md)  
[Testausdokumentti](./dokumentaatio/Testausdokumentti.md)

### Viikkoraportit:
[Viikkoraportti 1](./dokumentaatio/Viikkoraportti1.md)  
[Viikkoraportti 2](./dokumentaatio/Viikkoraportti2.md)  
[Viikkoraportti 3](./dokumentaatio/Viikkoraportti3.md)  
[Viikkoraportti 4](./dokumentaatio/Viikkoraportti4.md)  
[Viikkoraportti 5](./dokumentaatio/Viikkoraportti5.md)  
[Viikkoraportti 6](./dokumentaatio/Viikkoraportti6.md)  

### Ohjelman suoritus:

#### Asennus

    Jos poetry ei asennettu, niin ->
    pip3 install poetry
    
    Muussa tapauksessa ->
    poetry install
    poetry shell
    pip3 install -r requirements.txt

#### Aloitus

    poetry run invoke start

#### Ohjelman testaus

    poetry run invoke test
    poetry run invoke coverage-report
    poetry run invoke pylint
