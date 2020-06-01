# python2_strategiapeli

## 1. Esittely
    Peli on vuoropohjainen strategiapeli, jossa kahdella pelaajalla on useampia omia hahmoja. Oma vuoro koostuu hahmon liikuttamisesta
    ja hahmolla hyökkäämisestä. Peli ohjeistaa käyttäjää hyvin. Omia asetuksia voi tehdä ulkoisten tekstitiedostojen kautta.
    
## 2. Tiedosto- ja kansiorakenne
    Kaksi ylintä kansiota ovat nimillä doc ja src. Doc-kansiosta löytyy kaikki dokumentaatioon liittyvä ja src-kansiosta itse peliin
    liittyvät tiedostot. Src-kansiossa on alakansiona graphics ja maps, toisesta löytyy käytetyt grafiikkatiedostot ja toisesta pelikenttiä.
    Pelikenttä luetaan tällä hetkellä tiedostosta map2.txt.
    Muuten src-kansio sisältää python-tiedostot sekä asetustiedoston settings.txt.
    Kaikki python-tiedostot ovat itseni kirjoittamia, poislukien muutamia ylijäämämetodeja kurssin robots-tehtävästä, mitä käytin muutamassa luokassa mallina.
      
## 3. Asennusohje
    Ei vaadi muuta python3:n ja PyQt5:n lisäksi.
    
## 4. Käyttöohje
    Ohjelma käynnistyy ajamalla game.py-tiedosto. Omia asetuksia ja pelikenttiä tehdessä tulee noudattaa tekstitiedostojen formaatteja.
    Olemassa olevasta muodosta kannattaa ottaa mallia, tarkemmat ohjeet ovat dokumentaatiossa.
    Pelin teksti-ikkuna kertoo ihmispelaajalle, mitä toimintoa häneltä odotetaan. Kaikki interaktio tapahtuu klikkaamalla.
