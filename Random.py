import random

stars = random.randint(1,10)
#randint generates a random integer
print (stars, "stars")

death = random.randint(1,11)

hokage = ["Hashirama" , "Tobirama", "Hiruzen", "Minato", "Tsunade", "Kakashi", "Naruto"]

print(hokage)
print(death)
if death == 1:
    hokage.remove("Hashirama")
    print(hokage) 
elif death == 2: 
    hokage.remove("Tobirama")
    print(hokage)
elif death == 3: 
    hokage.remove("Hiruzen")
    print(hokage)
elif death == 4: 
    hokage.remove("Minato")
    print(hokage)
elif death == 5: 
    hokage.remove("Tsunade")
    print(hokage)
elif death == 6: 
    hokage.remove("Kakashi")
    print(hokage)
elif death == 7: 
    hokage.remove("Naruto")
    hokage.append("Shikamaru")
    print(hokage)
else:
    print("Nobody dies")
