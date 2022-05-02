class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing 
    two instances accoring to the rank.
    for example b1 < b2 if  b1.rank < b2.rank 
    '''
    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank) 
        self.similar = similar

    
    def __lt__(self, a) :  
        '''
        This function allows to make direct comparation using the operator <
        '''
        return self.title.lower() < a.title.lower()

    def __gt__(self, a) :  
        '''
        This function allows to make direct comparation using the operator >
        '''
        return self.title.lower() > a.title.lower()

    # describes less than or equal to (<=)
    def __le__(self, a):
        if self.title.lower() == a.title.lower():
            return True
        if self.title.lower() < a.title.lower():
            return True
        return False


    def __ge__(self, a):
        if self.title.lower() == a.title.lower():
            return True
        if self.title.lower() > a.title.lower():
            return True
        return False

    def __eq__(self, a):
        longest = ""
        shortest = ""
        if len(self.title) > len(a.title):
            longest = self.title.lower()
            shortest = a.title.lower()
        elif len(self.title) < len(a.title):
            longest = a.title.lower()
            shortest = self.title.lower()
        else:
            return False
        return longest.__contains__(shortest)


    def __str__(self):
        '''
        function returns a string containting the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}\n\tSimilar: {self.similar}"

    def getTitle(self):
        return self.title

