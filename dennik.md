# Dennik #
**Skupina:** Pandy

---
*Datum:* 29.3.2021
* Stiahli sme vsetky data
* Vytvorili sme funkciu na spracovavanie vsetkych tabuliek
* Funkcia ma vstup typ tabulky a rok(2015 - 2020), validne typy tabulky su:
    * all - Rebríček spotreby humánnych liekov
    * insurance - Rebríček spotreby humánnych liekov vydaných na recept hradených z verejného zdravotného poistenia
    * no prescription - Rebríček spotreby humánnych liekov predaných z verejnej lekárne bez receptu občanom
    * no insurance - Rebríček spotreby humánnych liekov vydaných z verejnej lekárne na recept bez úhrady z verejného zdravotného poistenia
    * detailed - Spotreba humánnych liekov v SR
* Pre vstupy:
    * kde je rok 2018 alebo 2019 okrem typu detailed
    * kde je rok 2020 a typ detailed 
Vracia funkcia asociativne pole, rozdelene podla stvrt rokov
---