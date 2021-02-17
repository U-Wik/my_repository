class Fish:
    def __init__(self):
        ''' Constructor of this class'''
        self.members = ['Drakfisk','Haj', 'Darrål']


    def printMembers(self):
        print('Printing members of the dangerous Fish class')
        for member in self.members:
            print('\t%s ' % member)
