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
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.sleep')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "862"])

    @intent_file_handler('furby.laugh.intent')
    def handle_furby_laugh(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.laugh')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "863"])

    @intent_file_handler('furby.burp.intent')
    def handle_furby_burp(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.burp')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "864"])

    @intent_file_handler('furby.fart.intent')
    def handle_furby_fart(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.fart')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "865"])

    @intent_file_handler('furby.purr.intent')
    def handle_furby_purr(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.purr')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "866"])

    @intent_file_handler('furby.sneeze.intent')
    def handle_furby_sneeze(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.sneeze')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "867"])

    @intent_file_handler('furby.sing.intent')
    def handle_furby_sing(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.snide_remark')
        self.speak_dialog('furby.sing')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "868"])

    @intent_file_handler('furby.talk.intent')
    def handle_furby_talk(self, message):
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        self.speak_dialog('furby.talk')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "869"])

    def stop(self):
        pass


def create_skill():
    return ControlFurby()
