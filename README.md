# team_SEB

## Case: Amstelheage
Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.  

Omdat de Duivendrechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

### Vereisten van het project
De wijk komt te staan op een stuk land van 180x160 meter (breed x diep). Er wordt door de planologen gerekend in hele meters.

Het aantal woningen in de wijk bestaat voor 60% uit eengezinswoningen, 25% uit bungalows en 15% uit maisons.

**Karakteristieken huizen:**
- Een eengezinswoning is 8x8 meter (breed x diep) en heeft een waarde van €285.000,- De woning heeft rondom twee meter vrijstand nodig; iedere meter extra levert een prijsverbetering op van 3%.
- Een bungalow is 11x7 meter (breed x diep) en heeft een waarde van €399.000,-. De woning heeft rondom drie meter vrijstand nodig, iedere meter extra levert een prijsverbetering op van 4%.
- Een Maison is 12x10 meter (breed x diep) en heeft een waarde van €610.000,- De woning heeft rondom zes meter vrijstand nodig, iedere meter extra levert een prijsverbetering op van 6%.

De vrijstand van een woning is de kleinste afstand tot de dichtstbijzijnde andere woning in de wijk. Oftewel, voor een vrijstand van 6 meter moeten alle andere woningen in de wijk op minimaal 6 meter afstand staan. Deze afstand is bepaald als de kortste afstand tussen twee muren, dus niet vanuit het centrum van de woning.

De verplichte vrijstand voor iedere woning moet binnen de kaart vallen. Overige vrijstand mag buiten de kaart worden meegerekend.

In geval van percentuele waardevermeerdering per meter is de toename niet cumulatief. Een maison met twee meter extra vrijstand is dus 12.0% meer waard, niet 12.36%.

De wijk bestaat voor een deel uit oppervlaktewater. Huizen mogen niet op het water worden geplaatst, maar hun vrijstand mag daar wel op vallen (zowel de verplichte als die voor de waarde berekening).

**Doel:**
Plaats de huizen zo op de kaart dat de woonwijk de hoogst mogelijke waarde oplevert.

## Installatie
Om dit programma te laten werken, installeer eerst Python (zie https://www.python.org/downloads/)  
In de requirements.txt staan vervolgens nog twee extra packages (Shapely en Matplotlib) die moeten worden gedownload om de code te laten runnen.  
Dit kan via het volgende command:  

> pip install -r requirements.txt

Of via conda:  

> conda install --file requirements.txt


## Gebruik
Om dit programma te laten runnen, moet het volgende in de terminal worden aangeroepen:  

> python main.py [type wijk] [aantal huizen] [algoritme]

- [type wijk] staat voor de ligging van het water in de wijk en kan bestaan uit wijk_1, wijk_2 of wijk_3 (zie het mapje 'data' voor de exacte coördinaten).
- [aantal huizen] staat voor de huizenvariant: dit kan 20, 40 of 60 zijn.
- [algoritme] staat voor het algoritme wat gebruikt wordt. De volgende algoritmes zijn beschikbaar: random, hillclimber, hillclimber_swap, genetic of simulated_annealing.

## Omschrijving Algoritmes

### Random
Zoals de naam al zegt, worden bij het random algoritme willekeurige huizen op de kaart geplaatst (de huizen krijgen willekeurige coördinaten toegewezen). Vervolgens wordt uit een bepaalde hoeveelheid kaarten de beste kaart gekozen.
Wel zit er een kleine bias in dit algoritme: de grote huizen worden namelijk eerst geplaatst, zodat random iets makkelijker tot een resultaat kan komen.

### HillClimber
Dit algoritme krijgt als startpunt de uitkomst van het Random algoritme, vervolgens pakt het algoritme steeds 1 huis en kijkt naar de 8 bewegingen die het huis kan maken. Van alle geldige stappen wordt de meest waardevolle uiteindelijk uitgevoerd. Alle huizen worden afgegaan met een for loop. Er worden 55 for loops gedaan waar de eerste stappen beginnen met 8 vakjes en het bouwt af tot aan 1 vakje per stap.

### HillClimber Swap
Dit algoritme kiest random 2 huizen die niet van hetzelfde type zijn en verwisseld deze met elkaar. Daarna wordt er gecheckt of deze wissel wel kan zonder dat er overlap wordt veroorzaakt. Als een wissel heeft plaatsgevonden dan wordt de waarde vergeleken met de tot dan toe best scorende kaart. Is de waarde hoger dan wordt de nieuwe kaart de best scorende kaart. Dit proces vind x keer plaats, x kan de gebruiker zelf bepalen door het in te vullen in main. 

### Genetic
Dit algoritme werkt volgens het principe van "survival of the fittest" (waarbij 'fitness' de waarde van de kaart is).  

Genetic is een population-based algoritme en er wordt dus gebruikgemaakt van meerdere generaties kaarten: 
- Elke generatie heeft een initiële populatie (voor de allereerste generatie zijn dit random kaarten). 
- Op de initiële populatie kaarten worden er per kaart een aantal mutaties toegepast (onder 'mutaties' verstaan we hier willekeurige verplaatsingen van huizen).
- Het algoritme houdt vervolgens een top X van kaarten bij en print de nummer 1 hiervan (voor de volgende generaties vormt deze top X de initiële populatie).


### Simulated Annealing
Het startpunt voor de simulated annealing komt voor uit het random algoritme dat 400 keer wordt gerunt en de beste kaart uit wordt gekozen. Daarna maakt het algoritme op verschillende manieren wijzigingen aan de kaart:
- Het eerste dat het algoritme doet is het kiezen van een random huis en deze draaien. 
- Daarna wordt er weer een random huis gekozen en gekeken of dit verplaatst kan worden met 1 of 2 meter.
- Als laatste stap worden er twee random huizen geselecteerd en deze met elkaar verwisseld. 
Bij alle drie de stappen wordt er aan het einde gecheckt of deze stap wel daadwerkelijk kan of dat er dan ‘overlap’ wordt veroorzaakt. Mocht er ‘overlap’ zijn dan kan deze aanpassing niet plaatsvinden. 

Wanneer er een verbetering van prijs is zal de simulated annealing deze altijd aannemen. Echter kan een verslechtering van de prijs ook worden aangenomen. Dit hangt af van de volgende vergelijking: random_number < probability. Hierbij is random nummer een nummer tussen 0 en 1. Probability krijgt zijn waarde uit de volgende formule: 
e^((prijs van de nieuwe kaart - prijs van de oude kaart)/ huidige temperatuur)).
De starttemperatuur is bij ons een temperatuur van 76001. Dit getal komt voor uit een berekening waarbij we uitgaan van een hele negatieve uitkomst uit het verschil tussen de nieuwe en oude kaart. Een van de grootste verschillen bij onze case is een verschil van -300.000, dit willen we dus maar heel af en toe aannemen (1% kans dat we deze aannemen). Dit hebben we ingevuld in de formule: 
e^(-300.000/ huidige temperatuur) = 0.01 → huidige temperatuur is: 76001. 

Elke keer wanneer de prijs hoger of lager is zal de huidige temperatuur met 1 zakken. Dit gebeurt totdat de temperatuur bij 0 is, dan zal van de huidige kaart een visualisatie worden gemaakt.

## Structuur
De structuur van de code is als volgt:

- **/project_code**: bevat alle code van dit project  
-- **/project_code/algorithms**: bevat de code voor algoritmes  
-- **/project_code/classes**: bevat de benodigde classes voor deze case  
-- **/project_ode/visualisation**: bevat de matplotlib code voor de visualisatie  
- **/data**: bevat drie verschillende databestanden die nodig zijn om het water in de wijk te visualiseren

## Auteurs 
- Sebastiaan Schlundt Bodien
- Ellemijn Galjaard
- Bono Lardinois






