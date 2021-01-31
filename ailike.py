import random
import time

user_is_ok_responses = ["\nLet's talk about our hobbies.",
                        "\nDo you play games?",
                        "\nDo you like anime?"]
random_index = random.randint(0,2)

def release_sama_ng_loob():
    time.sleep(1)
    print("\nIlabas mo lahat, makikinig ako. :)")
    print("Leave lines blank and press enter twice lang to let me know kung tapos ka na. :)")
    while input():
        input()

print("Hi, I would love to know you!")
user_name = input("What's your name? ")
print(f"\nHey, {user_name}! Nice to meet you! How's your day going? Is it going fine?")

while True:
    how_is_user = input("(Yes/No): ").lower()
    if how_is_user == "yes":
        print("\nThat's really great to hear!")
        print(user_is_ok_responses[random_index])
        if random_index == 0:
            hobby = input("What do you like to do with your free time? ")
            print(f"\n{hobby} sounds fun!")
            print(f"I have to go now! Your day seems too nice to be disturbed my be. Have a nice day, {user_name}!")
            break

        elif random_index == 1:
            while True:
                games = input("(Yes/No): ").lower()
                if games == "yes":
                    print("\nReally? I like games too!")
                    play = input("What's your favorite game? ")
                    print(f"{play} sounds really fun! We should play sometimes!")
                    print(f"Would you look at the time, I have to go. Take care, {user_name}!")
                    break

                elif games == "no":
                    print("\nOh okay. I do, but I understand that we have our own likings.")
                    print(f"Oh no, I'm late for work! I have to go now. Bye {user_name}! Have a nice day!")
                    break

                else:
                    print("I'm sorry, I don't quite understand.")
                    continue
        else:
            while True:
                anime = input("(Yes/No): ").lower()
                if anime == "yes":
                    print(f"Really?! I love anime!")
                    title = input("What's your favorite? ")
                    if title.lower() == "boku no pico" or title.lower() == "hentai":
                        print("ew")
                        break
                    else:
                        print(f"{title} sounds really cool! Let's go watch together sometimes!")
                        print(f"I have to go now. May your day be the best, {user_name}!")
                        break

                elif anime == "no":
                    print("You're a bad bad person if you don't like anime. I hate you!")
                    print(f"Bye, {user_name}! >:(")
                    break

                else:
                    print("I'm sorry, I don't quite understand.")
                    continue
        break

    elif how_is_user == "no":
        time.sleep(1)
        print("\nEveryone has bad days, but trust me it's going to get better.")
        print("If you need someone na mapaglalabasan ng sama ng loob, you have me.")
        print("Gusto mo ba ilabas yang sama ng loob mo?")
        while True:
            sama_ng_loob = input("(Yes/No): ").lower()
            if sama_ng_loob == "yes":
                release_sama_ng_loob()
                print("\nMahirap yung may sama ka ng loob. Kaya gusto ko sanang ilabas mo.")
                print("There's always light in the dark that will lead you to the right place.")
                print("Sana mahanap mo kaagad yung light na yon.")
                print("Sana ngayon, kahit papaano gumaan pakiramdam mo.")

            elif sama_ng_loob == "no":
                time.sleep(1)
                print("I fully respect your decision.")

            else:
                print("I'm sorry, I don't quite understand.")
                continue

            time.sleep(5)
            print("\nI know how much pain you're going through now.")
            print("Pero whatever happens, don't give up, okay?")
            print("There are people out there who need you. ")
            print("And please remember that you will never be alone.")
            print("Kung ngayon hindi ka okay, take the time para i-build ulit yung sarili mo.")
            print("Keep on going, there will be that time na magiging okay ang lahat.")
            print("And if ever hindi mo na talaga kaya, please seek professional help.")
            print("Pero I asure you everything is going to be alright. I'll give you your time now.")
            print("Please be safe and sound. Don't hurt yourself, okay? I trust you.")

            break
        break

    else:
        print("I'm sorry, I don't quite understand.")
        continue