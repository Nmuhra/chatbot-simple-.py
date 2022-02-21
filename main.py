print("Hello welcome to Nmuhra learning!!")
name= input("Name?\n")
print("Hello "+ name +", thank you for joining us today.")
for PL in ["python, javascript, R, react"]:
  choice = input(f"which programming language do you want to learn: {PL}\n").lower
  print(f"Great {name}, We will start shortly with your {choice} course, get your coffee ready")
language = "English, French, Spanish"
print(name + ", what language do you want your course to be in? Here are the ones currently available.\n"+ language)
language = input().lower()
if language == "english":
    print(f"thanks {name}, we are finalizing your {choice} course, making sure we are using {language}")
if language == "french":
    print(f"merci {name}, nous finalisons votre cours {choice}, en nous assurant que nous utilisons {language}")
if language == "spanish":
    print(f"gracias {name}, estamos finalizando su {choice} curso, asegurándonos de que estamos usando {language}")
