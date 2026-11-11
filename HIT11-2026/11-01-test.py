import turtle

turtle.shape("turtle")
turtle.color("pink")

# strg +x 
a = "asoziale Schildkröte"
# print(a) # print gibt im Terminal aus
turtle.forward(len(a)) # turtle soll Anzahl der Zeichen im string laufen
turtle.write(a) # turtle soll den string schreiben

turtle.done()