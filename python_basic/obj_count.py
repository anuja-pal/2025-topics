class ObjectCounter:
    no_of_objects = 0

    def __init__(self):
        type(self).no_of_objects+=1