import speech_recognition as sr

class VoiceText:
    """Classe pour convertir la voix en texte à l'aide de la bibliothèque SpeechRecognition"""

    def __init__(self, language='fr-FR'):
        """
        Initialise une nouvelle instance de VoiceText avec la langue spécifiée.

        Args:
            language (str, optionnel): la langue utilisée pour la reconnaissance vocale. La valeur par défaut est 'fr-FR'.
        """
        self.language = language
        self.recognizer = sr.Recognizer()
    def listen(self):
        """
        Ecoute l'entrée audio à partir du microphone et retourne le texte reconnu.

        Returns:
            str: le texte reconnu à partir de la voix.

        Raises:
            UnknownValueError: si la reconnaissance vocale ne peut pas reconnaître l'entrée audio.
            RequestError: si la reconnaissance vocale ne peut pas se connecter au service.
        """
        with sr.Microphone() as source:
            print("Dites quelque chose!")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            print("Vous avez dit : ", text)
            return text
        except sr.UnknownValueError:
            print("Je n'ai pas compris ce que vous avez dit")
        except sr.RequestError as e:
            print("Erreur de service: {0}".format(e))
