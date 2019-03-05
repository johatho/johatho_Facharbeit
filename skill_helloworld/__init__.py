#import der libraries
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.skills.core import intent_handler
from mycroft.util.log import LOG

class FacharbeitSkill(MycroftSkill):

    #Konstruktor
    def __init__(self):
        supported_languages = ["en-us", "de-de"]
        if self.lang not in supported_languages:
            self.speak_dialog("lang_unsupported")
            self.log.warning("unsupported language for " + self.name + ", skill wont be loaded")
            raise NotImplementedError

        super(FacharbeitSkill, self).__init__(name="FacharbeitSkill")
        
        # anzahl der Variablen
        self.count = 0

    #Wenn der Nutzer einen Satz der sich aus einer Zeile der "Hello.voc" und einer Zeile der 
    #"World.voc" Datei zusammensetzt 
    @intent_handler(IntentBuilder("").require("Hello").require("World"))
    def handle_hello_world_intent(self, message):

        #Mycroft spricht jeweils eine zufällige Zeile aus "hello.dialog" und "world.dialog"
        self.speak_dialog("hello", "world")

    #Wenn der Nutzer einen Satz der sich aus einer Zeile aus "duplicate.voc" und "Number_.rx"
    #zusammensetzt spricht
    @intent_handler(IntentBuilder("").require("duplicate").require("Number_"))
    def handle_duplicate_intent(self, message):

        #Mycroft multipliziert die Zahl die gesagt wurde mal 2 und spricht sie zusammen
        # mit einer zufälligen Zeile aus "duplicated.dialog" aus. 
        output = message.data.get("Number_") * 2
        self.speak_dialog("duplicated" , data={'value': output})
        

def create_skill():
    return FacharbeitSkill()
