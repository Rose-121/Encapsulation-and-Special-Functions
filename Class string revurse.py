class Word:
    
    def __init__(self, w):
        self.w = w  
        
    def revStr(self):
        return self.w[::-1] 

word = input("Enter a Word: ")

o1 = Word(word)
print("Reversed Word:", o1.revStr())
