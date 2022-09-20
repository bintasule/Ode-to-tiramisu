# i <3 tiramisu
tirami = input("Hey friend, I love Tiramisu! Do you like Tiramisu?(Yes/No) ")

if tirami.lower() == "Yes" or tirami.lower() == "yes" :
    print("I'm so happy to hear we have the same taste!") 
elif tirami.lower() == "No" or tirami.lower() == "no":
    print("Wow I'm disappointed, Tous Les Jours is my favorite bakery and they make it the best, you should try it again there.")
else:
    response = input("Have you ever tried Tiramisu? ")
    if response.lower() =="yes":
        print("I'm glad you have!")
    elif response.lower() =="no":
        print("You should definetly try it sometime. You won't regret it!")
    else:
        print("Ok")


