class OneorMore:
    def __init__(self, rest = None): #This will run when the class OneorMore runs
        self.rest = rest             # and stores the next pattern later
    
    def match(self, text, start = 0): # This function will test if the pattern matches text
        if start >= len(text):
            return False
        
        for end in range(start + 1, len(text) + 1): # This for loop will try different lengths of matches
            if self.rest: # This if else condition will check if another pattern exists.
                if self.rest.match(text, end): 
                    return True
            else:
                if end == len(text):
                    return True
        return False #it will return false, if the loop finished and no valid match was found