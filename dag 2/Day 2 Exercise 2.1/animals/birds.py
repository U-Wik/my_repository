class Birds:
       
    def __init__(self):
        ''' Constructor of this class'''
        self.members = ['Sparv','Rödhake', 'Anka']


    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)
