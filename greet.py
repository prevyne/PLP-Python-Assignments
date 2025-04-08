#!/usr/bin/env  python

userName=str(input("Input your User Name: "))
favoriteColor=str(input("Input your favorite colour: "))
processedGreeting="Hello {}! Your favorite color {}, is awesome".format(userName, favoriteColor)
print(processedGreeting)
