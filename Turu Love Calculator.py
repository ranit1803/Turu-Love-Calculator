#love calculator
import pyjokes
import pyttsx3
print("Welcome to Turu Love Calculator!!")
def love_calculator(name1, name2):
    combined_name = (name1+name2).lower()
    true_word = "true"
    love_word = "love"
    true_word_count=0
    love_word_count=0
    for letter in true_word:
        true_word_count+=combined_name.count(letter)
    for letter in love_word:
        love_word_count+=combined_name.count(letter)
    turu_love = str(true_word_count)+str(love_word_count)
    return turu_love
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
joke = pyjokes.get_joke(language="en", category="neutral")
user_a = input("Please Enter The First Name:\n")
user_b= input("Please Enter The Second Name:\n")
print(f"Your Turu Love Percentage is {love_calculator(user_a,user_b)} %")
choice = input(f"Want to know what our turu love baba says? (Y/N):\n").lower()
if choice == 'Y' or choice =='y':
    print("Turu Love Baba Concludes that!!")
    if int(love_calculator(user_a,user_b))>=95:
        print(f"\t{user_a} and {user_b} are made for each other!!")
    elif int(love_calculator(user_a,user_a))>=60 and int(love_calculator(user_a,user_b))<95:
        print(f"\tThere are chances!! Keep trying!!")
    else:
        print(f"\t{user_a} and {user_b} are not made for each other")
        print(joke)
        engine.say(joke)
        engine.runAndWait()
        engine.stop()
    print("Thanks for using the our calculator!!")
elif choice=='N' or choice=='n':
    print("Thanks for using the our calculator!!")
else:
    print("Invalid!!")