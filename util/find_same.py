class TagWord(str):
    ''' map tagalog text for matching purposes

    maps letters to lower-case ascii and hyphens to single spaces
    '''
    def __init__(self, original):
        self.original = original

    def mappo(self):
        self.mapped = ''
        for l in self.original:
            if l in 'aAáàâ': l = 'a'
            if l in 'eEé': l = 'e'
            if l in 'iIíìî': l = 'i'
            if l in 'oOóòô': l = 'o'
            if l in 'uUú': l = 'u'
            if l in '-': l = ' '
            self.mapped += l
        return self.mapped.lower()

    def __eq__(self, other):
        return self.mappo() == other.mappo()

