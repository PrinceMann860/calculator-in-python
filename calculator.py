import speech_recognition as sr
import pyttsx3
import re
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty ('voice', voices[1].id)
engine.setProperty("rate", 150)

def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listning...")
    r.pause_threshold = 1
    audio =  r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}\n")
  except Exception as e:
    print("Say that again please...")
    return "None"
  return query    
if __name__ == "__main__":
  speak("Hello i am your personal calculator on your voice command")
  while True:
    query = takecommand().lower()
    numbers = re.findall(r'\d+',query)
    numbers = [int(num) for num in numbers]
    if len(numbers) >= 1:
        num1 = numbers[0]
    if len(numbers) >= 2:
        num2 = numbers[1]
    if "add" in query or "plus" in query or "+" in query:
      print(num1+num2)
      speak(num1+num2)
    elif "subtract" in query or "minus" in query or "-" in query:
      print(num1-num2)
      speak(num1-num2)
    elif "multiply" in query or "into" in query or "*" in query:
      print(num1*num2)
      speak(num1*num2)
    elif "devide" in query or "by" in query or "/" in query:
      print(num1/num2)
      speak(num1/num2)
    elif "square of" in query:
      print(num1*num1)
      speak(num1*num1)
    elif "square root" in query:
      print(num1**1/2)
      speak(num1**1/2)
    elif "cube of" in query:
      print(num1*num1*num1)
      speak(num1*num1*num1)    
    elif "cube root" in query:
      print(num1**(1/3))
      speak(num1**(1/3))
    elif "sum" in query or "total" in query:
      print(sum(numbers))
      speak(sum(numbers))
    elif "stop" in query:
      break
      