class ArgumentationDecisionGraph:
    '''
    arguments is a set of tuples of (x, y), ((fi,vi), y)
    relations is a set of tuples of (x1, x2), (((fi,vi),yi), ((fj,vj),yj))
    x is a tuple of (fi,vi), fi is the feature index and vi is the value of the feature 
    y is the prediction, can be a value or und
    '''
    def __init__(self, ar, r):
        #ar is nodes
        self.arguments = ar
        #r is edges
        self.relations = r

    # define string representation of the class
    def __str__(self) -> str:
        result = "Arguments\n"
        for arg in self.arguments:
            result += str(arg) + "\n"

        result += "\nRelations\n"
        for r in self.relations:
            result += str(r) + "\n"
        return result