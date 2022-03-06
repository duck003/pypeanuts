from pycat.window import Window

window = Window()

oh=input("what do you want to eat?:")

ohw=input("Then where do you want to see it, left or right? Enter a number.:")

ohwo=input("Then where do you want to see it, up or down? Enter a number.:")

ohwow=input("Which size do you want? enter it.:")

w = window.create_sprite()
w.image = "forest_background.jpg"
w.scale=1.125
w.x=600
w.y=325

wow = window.create_sprite()
wow.x=600
wow.y=300

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

if oh == "owl":
    wow.image = "owl.png"
    print("Bird's egg.")

if oh == "fireball":
    wow.image = "fireball.gif"
    print("Don't you really want to eat fireball. (I prefer meatball.)")

if oh == "rooster":
    wow.image = "rooster.png"
    print("Regular chicken! (For sure.)")

if oh == "flyingowl":
    wow.image = "owl.gif"
    print("I think you have to catch first.")

if oh == "fireball":
    wow.image = "fireball.gif"

if oh == "rooster":
    wow.image = "rooster.gif"

wow.x=float(ohw)

wow.y=float(ohwo)

wow.scale=float(ohwow)


print("position", wow.x, ",", wow.y, wow.scale )

print("Enjoy your meal.")

window.run()
