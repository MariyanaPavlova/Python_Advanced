def say(n):
    if n ==0: # дефинираме дъно
        return
    print("Hey")
    say(n-1) # осигуряваме намаляване за да стигне дъното

say(5)