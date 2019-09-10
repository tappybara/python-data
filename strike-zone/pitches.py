class Pitches:
    def __init__(self):
        self.glossary = {}
        self.glossary['FA'] = 'Fastball'
        self.glossary['FF'] = 'Four-seam Fastball'
        self.glossary['FT'] = 'Two-seam Fastball'
        self.glossary['FC'] = 'Cutter'
        self.glossary['SI'] = 'Sinker'
        self.glossary['SF'] = 'Split-finger Fastball'
        self.glossary['FS'] = 'Splitter'
        self.glossary['SL'] = 'Slider'
        self.glossary['CH'] = 'Changeup'
        self.glossary['CU'] = 'Curveball'
        self.glossary['KC'] = 'Knuckle-curve'
        self.glossary['KN'] = 'Knuckleball'
        self.glossary['EP'] = 'Eephus'

    def get_pitch(self, abbr):
        return self.glossary[abbr]
