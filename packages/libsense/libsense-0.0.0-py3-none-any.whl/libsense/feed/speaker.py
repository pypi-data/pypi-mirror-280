import speech_recognition as sr

from roadguard.feed import parameter


def trigger_and_run(func: callable,
                    start_phrase: str = parameter.start_phrase,
                    stop_phrase: str = parameter.stop_phrase):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"Listening for '{start_phrase}' and "
              f"'{stop_phrase}' command...")
        text = ""
        try:
            while parameter.stop_phrase not in text.lower():
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                try:
                    text = recognizer.recognize_sphinx(audio)

                    print(f"Recognized: {text}")
                    if start_phrase in text.lower():
                        func()

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from recognizer; {e}")
        except KeyboardInterrupt:
            print("Stopped listening")
