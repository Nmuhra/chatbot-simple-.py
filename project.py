#Let's program together!! we are going to build a learning platform for you using python!!

#let's build robot 

print("Hello welcome to Nmuhra learning!!")

name= input("Name?\n")

print("Hello "+ name +", thank you for joining us today.")

menu = "Python, Javascript, R, CSS"

print(name + ", what do you wanna learn today? Here are the options.\n "+ menu)

order = input()

print("Great " + name + ", We will start shortly with your " + order +" course, get your coffee ready")

language = "English, French, Spanish, Arabic"

print(name + ", what language do you want your course to be in? Here are the ones currently available.\n"+ language)

language = input()

if language == "English":
 
    print("thanks " + name + ", we are finalizing your  " + order +" course, making sure we are using " + language)

if language == "French":

    print("merci " + name + ", nous finalisons votre cours " + order + ", en nous assurant que nous utilisons " + language)

if language == "Spanish":

    print("gracias " + name + ", estamos finalizando su " + order +" curso, asegurándonos de que estamos usando " + language)
