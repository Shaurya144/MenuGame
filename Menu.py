print("We have a Vegetarian menu (V), Carnivore diet (C)")
preference = input("Hello There! Which Menu would you like to look at? ").lower()
cutOffPoint = int(input("Is there any specific cut off point? If so just enter the value: "))

WholeMenu = {
    "Stir fry": 7.55,
    "Fajitas": 6.85,
    "Halloumi fries": 3.55,
    "Chicken": 19.99,
    "Duck": 8.99,
    "Veg Lasagne": 7.25,
    "Apple": 5.88
}

VegMenu = {
    "Stir fry": 7.55,
    "Halloumi fries": 3.55,
    "Veg Lasagne": 7.25,
    "Apple": 5.88
}

if preference == "v":
    for key, value in VegMenu.items():
        if VegMenu.values() <= cutOffPoint:
            print(key + " - " + str(value))
elif preference == "c":
    for key, value in WholeMenu.items() - VegMenu.items():
            print(key, value)
else:
    print("I did not get that. Or we have no items that are below this value")