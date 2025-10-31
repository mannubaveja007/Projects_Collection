import textwrap
name = input("Enter your name:  ").strip()
profession = input("Enter your profession:  ").strip()
passion = input("Enter your passion: ").strip()
emoji = input("Enter your emoji: ").strip()
website = input("Enter your website: ").strip()

print("\n choose your style: ")
print("1.simple Letter ")
print("2. vertical flair ")
print("3.Emoji Sandwich ")
style = input("Enter 1,2,3: ").strip()
def generator_style(style):
    if style == "1":
        return f"{emoji} {name} | {profession}\n {passion}\n {website}"
    elif style == "2":
        return f"{emoji} {name}\n {profession}\n{passion}\n {website}"
    elif style == "3":
        return f"{name} {emoji} \n {profession} \n {passion}"
bio = generator_style(style)
print("\nyour stylish bio")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)
save = input("DO yu want to save file").lower()
if save == 'y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename,"w",encoding="utf-8")as f:
        f.write(bio)
    print("file saved")    
