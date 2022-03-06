from pycat.window import Window

window = Window()

print("Animal Driver")

oh=input("Choose a power!(Wind, animal, ckickenking):")

ohw=input("Choose a form!(owl, heat, pigmou):")



w = window.create_sprite()
w.image = "forest_background.jpg"
w.scale=1.125
w.x=600
w.y=325

wow = window.create_sprite()
wow.x=400
wow.y=400

woww = window.create_sprite()
woww.x=800
woww.y=400

ww = window.create_sprite()
ww.image = "fireball.gif"
ww.x=800
ww.y=180
ww.is_visible = False 

www = window.create_sprite()
www.image = "rat.png"
www.x=400
www.y=180
www.is_visible = False 

if oh == "wind":
    wow.image = "owl.png"

if oh == "animal":
    wow.image = "fireball.gif"
    

if oh == "chickenking":
    wow.image = "rooster.png"
    print("Regular chicken! (For sure.)")

if ohw == "owl":
    woww.image = "owl.gif"

if ohw == "fire":
    woww.image = "fireball.gif"

if ohw == "pigmou":
    woww.image = "pig.png"


window.run()
