from easygui import *
from playsound import playsound
import time
import sys
vraag=0
fout=0
goed=0

msgbox(" ", image="images/TOP.gif")

name= enterbox(" Wat is je naam?")

msgbox("Welkom {}\n"
       "Bedankt voor je deelname\n"
       "Success ermee".format(name), image="images/welkom.gif")

antwoorden= ["afsluitdijk",
"denhelder",
 "texel","waddenzee",
             "ijsselmeer",
             "enkhuizen",
             "alkmaar",
             "purmerend",
             "purmerend",
 "markeermeer",
 "zaandam",
 "noordzeekanaal",
 "haarlem",
 "schiphol",
 "amsterdam",
"amstelveen",
 "hilversum",
 "haarlemmeer",
             "nordzee",
             "leiden",
             "denhaag",
             "nieuwe waterweg",
             "rijnmond",
            "delft",
             "rotterdam",
             "alphen aan den rijn",
             "zoetermeer",
             "gouda",
             "lek",
             "dordrecht",
             "biesbos",
             "amsterdam-rijnkanaal",
             "utrecht",
             "amersfoort",]



def toets(img, antwoord):
    global goed
    global fout
    global vraag

    a= enterbox("Waar is de gemarkeerde plaats op de kaart?",image=img,title="Vraag-{}".format(vraag))
    if a==antwoord:
        playsound("sounds/applaus.mp3")
        msgbox("GOED ZO! {}".format(name), image="images/super.gif")
        goed+=1

    elif a== None:
        exit()

    else:
         playsound("sounds/fout.mp3")
         msgbox("HELAAS\nHet is fout\nHet goede antwoord is {}".format(antwoord), image="images/huilen.GIF")
         fout+=1


for x in range (len(antwoorden)):
    vraag+=1

    toets('images/{}.png'.format(antwoorden[x]), antwoorden[x])
    percentage= (100/vraag)*goed

if percentage<=55:
    text="Helaas je bent  gezakt"
    img= "images/gezakt.gif"
else:
    text="Goed zo je bent geslaagd"
    img="images/geslaagd.gif"


msgbox("GOED: {}\n"
       "FOUT: {}\n"
       "PERCENTAGE: {:.1f}\n"
       "{}".format(
    goed,fout,percentage,text
), image=img)
sys.exit(0)
   


