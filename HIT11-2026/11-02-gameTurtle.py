"""
Time to play!

Zwei turtles wollen Verstecken spielen. Eine soll sich am Anfang "unsichtbar" machen und
ein Versteck suchen, die andere dann mit Eingabe von Koordinaten (x,y) die andere finden.

Um den Abstand zwischen zwei turtles zu ermitteln nutzen wir eine neue Funktion
names turtle1.distance(turtle2) und fragen dies in einer if-Abfrage ab. 

Teste erst das if/else Beispiel und versuche dann mit python in cmd + python in vs
code am Versteckspiel.
"""

#if else Beispiel
wert = 25

a = 10
b = 40

if a > wert:
    print("a ist größer als Wert")
else:
    print("b ist grö0er als Wert")

"""
Wenn du das verstanden hast, spiel ein wenig mit den Zahlen rum oder anderen Operatoren,
für verschiedene Ergebnisse:
Operatoren: > < >= <= != ==

Es gibt auch noch elif, was dann wie folgt aussieht:
"""

if a == b:
    print("a ist gleich b")
elif b != a:
    print("b ist ungleich a")
else:
    print("a und b sind irgendwas")