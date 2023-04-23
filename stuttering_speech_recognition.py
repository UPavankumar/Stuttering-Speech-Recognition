import speech_recognition as sr
import requests
from gtts import gTTS
import os
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Initialize SpeechRecognition
r = sr.Recognizer()

# Initialize the microphone
mic = sr.Microphone()

# Initialize the speaker
speaker = os.system("sudo amixer cset numid=3 1")

# Define the URL of the online dataset
url = "https://raw.githubusercontent.com/datasets/speech-accent-archive/master/speakers.csv"

# Retrieve the dataset from the URL
response = requests.get(url)

# Parse the dataset into a list of words
words = response.content.decode().splitlines()[1:]
words = [word.split(",")[-1] for word in words]

# Define the passing level accuracy
passing_level = 0.8

# Train a logistic regression model on the dataset
X_train = [[len(w), w.count("a"), w.count("e"), w.count("i"), w.count("o"), w.count("u")] for w in words]
y_train = [int(w[0] == "a") for w in words]
model = LogisticRegression().fit(X_train, y_train)

# Loop to continuously recognize speech
while True:
    # Listen for speech with the microphone
    with mic as source:
        audio = r.listen(source)

    try:
        # Recognize the speech using Google Speech Recognition
        text = r.recognize_google(audio)

        # Display the recognized text (optional)
        print("You said: ", text)

        # Calculate the accuracy of the speech using the machine learning model
        accuracy = model.predict_proba([[len(text), text.count("a"), text.count("e"), text.count("i"), text.count("o"), text.count("u")]])[0][1]

        # Display the accuracy of the speech
        print("Accuracy: ", accuracy)

        # Check if the speech is correct
        if accuracy >= passing_level:
            print("Great job! You said it correctly.")
        else:
            # Generate the correct pronunciation using gTTS
            tts = gTTS(text=words[0], lang='en')
            # Save the correct pronunciation to a file
            tts.save('correct.mp3')
            # Play the correct pronunciation through the speaker
            os.system("mpg321 correct.mp3")

    except sr.UnknownValueError:
        # Display an error message if the speech cannot be recognized
        print("Could not understand audio")
    except sr.RequestError as e:
        # Display an error message if there is an issue with the speech recognition service
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
