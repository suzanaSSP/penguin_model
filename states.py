def cold(penguin):
    if penguin.temperature < 10:
        penguin.move_to_center()
    else:
        penguin.state = warm(penguin)
        
def warm(penguin):
    if penguin.temperature > 10:
        penguin.move_away
    else:
        penguin.state = cold(penguin)