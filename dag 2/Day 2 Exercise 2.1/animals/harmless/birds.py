class Birds:
    def __init__(self):
        ''' Constructor of this class'''
        self.members = ['Talgoxe','Bofink', 'Blåmes']


    def printMembers(self):
        print('Printing members of the harmless Birds class')
        for member in self.members:
            print('\t%s ' % member)
