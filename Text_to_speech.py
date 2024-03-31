from gtts import gTTS
import os
import pyttsx3


def text_to_speech(text, voice_index=0, rate=200):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice[voice_index].id)
    engine.say(text)
    engine.runAndWait()
    print('')

def Run_main_file():
    rate = 200
    in_put_rate = 1
    Voice_check = 1
    print("\nThis program will convert your text into file according to your needs \n")
    while(True):
        text = input("Enter the text you want to convert to speech: ")
        if Voice_check == 1 :
            print("Choose voice:")
            print("1. Male")
            print("2. Female")

            voice_choice = input("Enter your choice (1/2): ")

            if voice_choice == '1':
                voice = 0
            elif voice_choice == '2':
                voice = 1
            else:
                voice = 2
        if in_put_rate == 1 :
            rate = int(input("Enter speech rate (words per minute): "))
        print("\nConverting text to speech...")
        text_to_speech(text, voice, rate)

        print("\nSpeech generated successfully!")

        input_to_quit = int(input("Want to Convert more ? \n '0' to continue \n '1' to quit \nEnter you choice : "))
        if input_to_quit == 1:
            print("Thank you for Using")
            text_to_speech("Thank you for Using")
            break
        else:
            print("Ok we will Continue ")
            if in_put_rate == 1:
                text_to_speech("Ok we will Continue . Would you like to use same rate as before or you want to edit it ? ")
                print("Would you like to use same rate as before or edit it ? ")
                in_put_rate = int(input("'1' to Change \n'0' to Keep simiar \nEnter you choice : "))

            if Voice_check == 1:
                text_to_speech("Would you like to use same Voice as before or edit it ?")
                print("Would you like to use same Voice as before or edit it ? ")
                Voice_check = int(input("'1' to Change \n'0' to Keep simiar \nEnter you choice : "))

if __name__ == "__main__":
    Run_main_file()
