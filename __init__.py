from mycroft import MycroftSkill, intent_file_handler
import subprocess


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('furby.tell.intent')
    def handle_furby_tell(self, message):
        self.speak_dialog('furby.tell')

    @intent_file_handler('furby.dance.intent')
    def handle_furby_dance(self, message):
        self.speak_dialog('furby.dance')

    @intent_file_handler('furby.sleep.intent')
    def handle_furby_sleep(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.sleep')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "862"])

    @intent_file_handler('furby.laugh.intent')
    def handle_furby_laugh(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "863"])
        self.speak_dialog('furby.laugh')

    @intent_file_handler('furby.burp.intent')
    def handle_furby_burp(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "864"])
        self.speak_dialog('furby.burp')

    @intent_file_handler('furby.fart.intent')
    def handle_furby_fart(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "865"])
        self.speak_dialog('furby.fart')

    @intent_file_handler('furby.purr.intent')
    def handle_furby_purr(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "866"])
        self.speak_dialog('furby.purr')

    @intent_file_handler('furby.sneeze.intent')
    def handle_furby_sneeze(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "867"])
        self.speak_dialog('furby.sneeze')

    @intent_file_handler('furby.sing.intent')
    def handle_furby_sing(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "868"])
        self.speak_dialog('furby.snide_remark')
        self.speak_dialog('furby.sing')

    @intent_file_handler('furby.talk.intent')
    def handle_furby_talk(self, message):
#        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "869"])
        self.speak_dialog('furby.talk')

    def stop(self):
        pass


def create_skill():
    return ControlFurby()
