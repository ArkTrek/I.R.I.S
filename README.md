# I.R.I.S. (Intelligent Response Interaction System)

I.R.I.S. is an intelligent voice-activated assistant that understands and executes commands in Malayalam. The assistant can recognize spoken commands, run or open software, and learn new commands over time. It integrates with Google mT5 for natural language processing and `gTTS` for generating responses in Malayalam.

## Features
- **Speech recognition in Malayalam** using Google Speech API.
- **Text generation and response** using mT5 model from Hugging Face.
- **Text-to-speech (TTS)** functionality in Malayalam using `gTTS`.
- **Command execution** for opening, running, or closing software or files.
- **Learning capability**: I.R.I.S. learns new commands and saves them automatically.

## Project Structure
I.R.I.S/ 

├── iris.py # Main script to run the assistant
├── commands.json # Stores learned commands and actions (auto-generated) 
├── user_data.json # Logs user interactions (auto-generated)  
├── response.mp3 # Temporary file for audio response (dynamically created)  
├── requirements.txt # List of dependencies  
└── README.md # Documentation


## Setup Instructions

### 1. Clone the Repository
bash
```
git clone https://github.com/arktrek/I.R.I.S.git
cd I.R.I.S
```

### 2.  Set Up a Virtual Environment
For Windows:
``` 
python -m venv venv
.\venv\Scripts\activate
```
For macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```Install the necessary Python packages using the following command:
pip install -r requirements.txt
```

### 4. Required External Tools
Ensure you have mpg321 or any other MP3 player installed to play the audio response.

For Linux:
```
sudo apt-get install mpg321
```

### 5. Running I.R.I.S.
``` After setting up the virtual environment and installing dependencies, you can run I.R.I.S. by executing the main script:
python iris.py
```

### 6. Saving and Using Commands
I.R.I.S. listens for commands in Malayalam. If it doesn't recognize a command, it will ask if you want to save it and let you define what action (run, open, or close) the command should perform. The learned commands are saved in commands.json.

Example Commands (in Malayalam)
Open Notepad: "നോട്ട് പാഡ് തുറക്കുക"
Close Chrome: "ക്രോം അടയ്ക്കുക"
Run a specific command: "ഈ കമാൻഡ് ഓടിക്കുക"

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are always welcome!
