# Stuttering Speech Recognition
This project is a Python-based solution for recognizing the speech of a stuttering child and determining if they are pronouncing words correctly. The program uses a Raspberry Pi with a microphone to capture speech and convert it to text. The text is then compared to a list of words using a machine learning model to determine if the child pronounced the word correctly. If the word is pronounced incorrectly, the program will repeat the word until the child pronounces it correctly. The target language for the model is English.

## Dependencies
- Python 3.x
- speech_recognition module
- gTTS module
- mpg321 package
- PyAudio package
- Scikit-learn module

## Installation
1. Install Python 3.x on your Raspberry Pi.
2. Install the required packages by running the following command:
```
pip install speechrecognition gtts pyaudio scikit-learn
```

3.Download or clone the project from this repository.
4.Connect the microphone to the Raspberry Pi.

## Usage
1.Open the terminal and navigate to the project directory.
2.Run the following command to start the program:

```
python stuttering_speech_recognition.py
```
3.Speak into the microphone and the program will convert your speech to text and compare it with the pre-defined list of words.
4.If a word is pronounced incorrectly, the program will repeat the word until the child pronounces it correctly.
5.The program will display the accuracy of each word pronounced by the child. The passing accuracy level is set to 80%.

## Contributors
- ### U Pavan kumar
## License
This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).
