import tkinter


def hideIndicators(readingIndicator,grammarIndicator,pronunciationIndicator):
    readingIndicator.config(bg="#008ECC")
    grammarIndicator.config(bg="#008ECC")
    pronunciationIndicator.config(bg="#008ECC")
    
def indicate(lb , page):
    hideIndicators()
    lb.config(bg="white")
    page()
