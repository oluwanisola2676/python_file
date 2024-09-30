# personal bot
print ("Hello what is your name")
name = input()

print("What is the weather condition in your location, " + name)
print("Is it raining, cloudy, sunny, fair or cold")
weather = input().capitalize()

if weather == "Rainy":
    print(" Dear " + name + "i'll advise you to wear a rain coat or use a rain coat when going out")

elif weather == "Cloudy":
    print("Such a nice weather but its advsible to wear body warming clothes because there is more chance of rainfall")

elif weather == "Sunny":
    print("It's must be pretty hot, please use an umbrella while going out")

elif weather == "Fair":
    print("Very nice weather, dress as you wish " + name + " the weather is very favourble")

elif weather == "Cold":
    print("Ohh please wear a sweater or cardigan to avoid catching cold and shivering")

print(" Have a nice day," +  name)
