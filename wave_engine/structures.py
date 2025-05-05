class Wave:
    def __init__(self,start,end,label,level):
        self.start=start
        self.end=end
        self.label=label
        self.level=level

    def length(self):
        return self.end-self.start
    
    def __repr__(self):
        return f"<Wave {self.label} L{self.level} [{self.start},{self.end}]>"
