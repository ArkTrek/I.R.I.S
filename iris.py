import speech_recognition as sr
from transformers import MT5ForConditionalGeneration, MT5Tokenizer
from gtts import gTTS
import os
import json

# Initialize the mT5 model and tokenizer for Malayalam
model = MT5ForConditionalGeneration.from_pretrained("google/mt5-base")
tokenizer = MT5Tokenizer.from_pretrained("google/mt5-base")

# Initialize speech recognition
recognizer = sr.Recognizer()

# Load the commands data
if os.path.exists("commands.json"):
    with open("commands.json", "r") as f:
        commands = json.load(f)
else:
    commands = {}

# Function to recognize speech in Malayalam
def listen_to_malayalam():
    with sr.Microphone() as source:
        print("Listening for Malayalam command...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language='ml-IN')
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

# Function to generate a response using the mT5 model
def generate_response(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Function to speak response using gTTS in Malayalam
def speak_malayalam(text):
    tts = gTTS(text=text, lang='ml')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

# Function to store interaction for continuous learning
def store_interaction(user_input, response):
    interaction = {"input": user_input, "response": response}
    with open("user_data.json", "a") as f:
        f.write(json.dumps(interaction) + "\n")

# Function to process a command
def process_command(command):
    if command in commands:
        action_type, action_data = commands[command]
        
        # Perform the saved action
        if action_type == "run":
            os.system(action_data)  # Runs a command in terminal
            speak_malayalam(f"{command} ഓടുന്നു.")  # Running the software/file.
        elif action_type == "open":
            os.startfile(action_data)  # Opens a file
            speak_malayalam(f"{command} തുറക്കുന്നു.")  # Opening the file.
        elif action_type == "close":
            os.system(f"taskkill /f /im {action_data}")  # Closes a software (Windows)
            speak_malayalam(f"{command} അടച്ചിരിക്കുന്നു.")  # Closing the software.
    else:
        # If the command is not recognized, ask if the user wants to save it
        speak_malayalam("ആ കല്പന പുതുതായാണ്. നിങ്ങൾ ഈ കല്പനയെ ഒരു പ്രവർത്തനമായി സംഭരിക്കണമോ?")  # "This command is new. Do you want to save it as an action?"
        confirmation = listen_to_malayalam()

        if "അതെ" in confirmation:  # "Yes" in Malayalam
            speak_malayalam("ഈ കല്പനയുടെ പ്രവർത്തനം എന്താണ്? ഓടിക്കുക, തുറക്കുക, അല്ലെങ്കിൽ അടയ്ക്കുക?")  # "What should this command do? Run, Open, or Close?"
            action_type = listen_to_malayalam()

            if "ഓടിക്കുക" in action_type:  # "Run" in Malayalam
                speak_malayalam("എന്ത് കമാൻഡ് ഓടിക്കണം?")  # "Which command should be run?"
                action_data = listen_to_malayalam()
                commands[command] = ("run", action_data)
            elif "തുറക്കുക" in action_type:  # "Open" in Malayalam
                speak_malayalam("തുറക്കേണ്ട ഫയലിന്റെ പാത്ത് എന്താണ്?")  # "What is the path of the file to open?"
                action_data = listen_to_malayalam()
                commands[command] = ("open", action_data)
            elif "അടയ്ക്കുക" in action_type:  # "Close" in Malayalam
                speak_malayalam("അടയ്ക്കേണ്ട സോഫ്റ്റ്വെയറിന്റെ പേര് എന്താണ്?")  # "What is the name of the software to close?"
                action_data = listen_to_malayalam()
                commands[command] = ("close", action_data)
            else:
                speak_malayalam("അറിയാതെ പോയി. വീണ്ടും ശ്രമിക്കൂ.")  # "I didn't understand. Please try again."
                return

            # Save the new command
            with open("commands.json", "w") as f:
                json.dump(commands, f)

            speak_malayalam(f"{command} ചിട്ടീകരിച്ചു.")  # "{command} saved as a new action."

# Main loop for listening and processing commands
def main():
    while True:
        print("Awaiting command...")
        user_command = listen_to_malayalam()
        if user_command:
            process_command(user_command)

if __name__ == "__main__":
    main()
