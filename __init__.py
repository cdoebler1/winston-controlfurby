from mycroft import MycroftSkill, intent_file_handler


class TellFurby(MycroftSkill1):
    def __init__(self):
        MycroftSkill1.__init__(self)

    @intent_file_handler('furby.tell.intent')
    def handle_furby_tell(self, message):
        self.speak_dialog('furby.tell')


class DanceFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('furby.dance.intent')
    def handle_furby_dance(self, message):
        self.speak_dialog('furby.dance')


def create_skill():
    return DanceFurby()
    return TellFurby()
