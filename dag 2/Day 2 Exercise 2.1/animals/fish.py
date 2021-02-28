class Fish:
    def __init__(self):
        ''' Constructor of this class'''
        self.members = ['Gädda','Gös', 'Makrill']


    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)
