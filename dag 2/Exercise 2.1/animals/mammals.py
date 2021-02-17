class Mammals:
    def __init__(self):
        ''' Constructor of this class'''
        self.members = ['Tiger','Elefant', 'Vildkatt']


    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
