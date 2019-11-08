from mycroft import MycroftSkill, intent_file_handler


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('furby.control.intent')
    def handle_furby_control(self, message):
        self.speak_dialog('furby.control')


def create_skill():
    return ControlFurby()

