import streamlit
import pandas as pd

df = pd.read_csv()

"""
Hausaufgabe bis 24.11.:
Daten importieren
Widget für Zutat eingeben erstellen und nutzen
passende Cocktails ausgeben
wenn ihr gut genug seid, die komplette stripped liste da rein bauen, auslesen und die passenden Cocktails
anzeigen

"""


"""
Aufgaben für November und Dezember
# Cocktail Streamlit Aufgaben
1. Lege ein GUI an, was sich an populären Cocktail Websites orientiert (die schlauerweise im Schulnetz wegen Alkoholwerbung verboten sind)
2. If skill issue: denke Dir dein eigenes GUI aus. Folgende Ziele sind gegeben:
    2.1 Nach Cocktailkategorien filtern und alle Informationen zum Cocktail ausgeben
    2.2 Bilder zu den Cocktails ausgeben (cocktail_images.zip)
    2.3 Unique Zutaten anzeigen (insofern öfter als x-mal vorhanden) und danach passende Cocktails anzeigen "What's in your cupboard?" Modus
    2.4 Arrrrrgh allergy: Ausschluss bestimmter Zutaten der ausgewählten Cocktails (schwierig). Also erstmal passende Cocktails anzeigen lassen, dann unique Zutaten von denen anzeigen lassen und mit multiselect oder so abwählen lassen, was gar nicht geht.
3. Alkoholgehalt kalkulieren
4. Cocktail Rating einführen
5. OMG, das GUI: es ist zu diesem Zeitpunkt sicherlich hässlich geworden. Überarbeite es komplett!

# Cocktail Pandas Only Übungsaufgaben
1. CSV-Datei einlesen:
Lese die Datei in ein Pandas DataFrame ein und zeige die ersten 5 Zeilen an.

2. Spaltennamen anzeigen:
Zeige die Spaltennamen des DataFrames an.

3. Daten filtern:
Filtere die Daten nach der Kategorie "Contemporary Classics" und zeige das Ergebnis an.

4. Bestimmte Spalten auswählen:
Wähle nur die Spalten "name" und "ingredients" aus und zeige sie an.

5. Zeilen zählen:
Zähle die Anzahl der Zeilen im DataFrame.

6. Zeilen mit leeren Werten filtern:
Finde alle Zeilen, bei denen die Spalte "garnish" leer ist.

7. Garnish-Werte auffüllen:
Fülle leere Werte in der Spalte "garnish" mit "No garnish".

8. Neue Spalte hinzufügen:
Füge eine neue Spalte "difficulty" mit dem Wert "easy" für alle Zeilen hinzu.

9. Zeilen mit bestimmten Text filtern:
Finde alle Rezepte, die "Vodka" als Zutat enthalten, und zeige sie an.

10. Zeilen nach Name sortieren:
Sortiere die Zeilen nach dem Namen der Cocktails in aufsteigender Reihenfolge und zeige das Ergebnis an.

11. Datensatz speichern:
Speichere das DataFrame in eine neue CSV-Datei mit dem Namen "sorted_cocktails.csv".
"""