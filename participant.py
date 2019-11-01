
'''

################## PARTICIPANT.PY ########################
      © Jack Leonard 2019
      117372043 - Iowa Gambling Task Project

    Two classes: Participant and TrialParticipant.
    A cleaned up version of /older/117372043_Week4Lab1Assignment.py

##########################################################
'''


class Participant:
    #This is the main Participant Class; Trial Participant Inherits from this

    howManyParticipants = 0

    def __init__(self, firstName, lastName):
        # Participants First Name
        self.firstName = firstName

        # Participants Last Name
        self.lastName = lastName

        #Participants Full Name
        self.fullName = self.firstName + " " + self.lastName

        ##todo: not sure if this is needed for project or not (Not in req statement) clarify with Laura Maye

        # AIII | Variable that counts how many instances of class created
        Participant.howManyParticipants += 1
        # AIV Participants Number
        self.participantsNumber = Participant.howManyParticipants

    #Getters & Setters

    def setFirstName(self, new_firstName):
        self.firstName = new_firstName

    def setLastName(self, new_lastName):
        self.lastName = new_lastName

    # Class String Representation
    def __str__(self):
        return "Object Info - Participants Full Name: %s, Participant Number:  %d" % (self.fullName, self.participantsNumber)


class trialParticipant(Participant):

    #Initializer for trialParticipant Class
    def __init__(self):

        self.charsPressed = {"a": 0, "b": 0, "c": 0, "d": 0, }

        #Dragging in initializer from Participant Class
        super(Participant).__init__()

    pass




