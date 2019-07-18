favFruits = ["mango", "avocado", "pinapple", "pomegranate", "grapes"]
print(favFruits)

###### .append() adds stuff to the list ######
favFruits.append("orange")
print(favFruits)

nFav = favFruits[2]
print(nFav)

###### removes ######
#favFruits.pop(2)
#print (favFRuits)

###### 
# favFruits.remove("avocado")
# print(favFruits)

# for fruit in favFruits:
#     print("I like " + fruit + ".")
    
# for fruit in range(0, len(favFruits)):
#     print("I like " + favFruits[fruit])
    
# for fruit in range(0, len(favFruits)):
#     print("I like " + str(fruit))
    
    
#fruitCriteria = [True, 0.20, True, True, 100, "banana", True]

########### Dictionary - where every element has two parts
########### "key" and "value"
fruitCriteria = {"isFresh": True, "costPerPound": 0.20, "isRipe": True, "inSeason": True, "howMuchLikey": 100, "whatIsIt": "banana", "isAllergic": False}
print(fruitCriteria)
print(fruitCriteria["isAllergic"])

fruitCriteria["specialFeature"] = "GMO"
print(fruitCriteria)

for key in fruitCriteria:
    print("The answer to " + str(key) + " is " + str(fruitCriteria[key]) + ".")
    
print(fruitCriteria["specialFeature"])