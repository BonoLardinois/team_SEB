# team_SEB

## Case: Amstelheage
Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.  

Omdat de Duivendrechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

## Installatie
Om dit programma te laten werken, installeer eerst Python (zie https://www.python.org/downloads/)  
In de requirements.txt staan vervolgens nog twee extra packages (Shapely en Matplotlib) die moeten worden gedownload om de code te laten runnen.  
Dit kan via het volgende command:  

pip install -r requirements.txt

Of via conda:  

conda install --file requirements.txt

## Gebruik
Om dit programma te laten runnen, moet het volgende in de terminal worden aangeroepen:  

python main.py [type wijk] [aantal huizen] [algoritme]

- [type wijk] staat de ligging van het water in de wijk en kan bestaan uit wijk_1, wijk_2 of wijk_3 (zie het mapje 'data' voor de exacte coördinaten).
- [aantal huizen] staat voor de huizenvariant: dit kan 20, 40 of 60 zijn.
- [algoritme] staat voor het algoritme wat gebruikt wordt. De volgende algoritmes zijn beschikbaar: random, hillclimber, hillclimber_swap, genetic of simulated_annealing.

## Omschrijving Algoritmes

### Random
Zoals de naam al zegt, worden bij het random algoritme willekeurige huizen op de kaart geplaatst (de huizen krijgen willekeurige coördinaten toegewezen). Vervolgens wordt uit een bepaalde hoeveelheid kaarten de beste kaart gekozen.
Wel zit er een kleine bias in dit algoritme: de grote huizen worden namelijk eerst geplaatst, zodat random iets makkelijker tot een resultaat kan komen.

### HillClimber

### HillClimber Swap

### Genetic
Dit algoritme werkt volgens het principe van "survival of the fittest" (waarbij 'fitness' de waarde van de kaart is).  

Genetic is een population-based algoritme en er wordt dus gebruikgemaakt van meerdere generaties kaarten: 
- Elke generatie heeft een initiële populatie (voor de allereerste generatie zijn dit random kaarten). 
- Op de initiële populatie kaarten worden er per kaart een aantal mutaties toegepast (onder 'mutaties' verstaan we hier willekeurige verplaatsingen van huizen).
- Het algoritme houdt vervolgens een top X van kaarten bij en print de nummer 1 hiervan (voor de volgende generaties vormt deze top X de initiële populatie).


### Simulated Annealing


## Structuur
De structuur van de code is als volgt:

/project_code: bevat alle code van dit project
/project_code/algorithms: bevat de code voor algoritmes
/project_code/classes: bevat de benodigde classes voor deze case
/project_ode/visualisation: bevat de matplotlib code voor de visualisatie
/data: bevat drie verschillende databestanden die nodig zijn om het water in de wijk te visualiseren

## Auteurs 
- Sebastiaan Schlundt Bodien
- Ellemijn Galjaard
- Bono Lardinois






