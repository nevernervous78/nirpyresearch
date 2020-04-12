class Bootstrap:

    '''Essential bootstrap cross validator, consistent with other splitter classes
       in sklearn.model_selection.

    Example:

    boot = Bootstrap(n_bootstraps = 3, random_state=1)

    for train, test in boot.split(X):
        print("Train:", X[train],"  Test:", X[test])
    '''

    def __init__(self,n_bootstraps=5, random_state=None):
        self.nb = n_bootstraps
        self.rs = random_state

    def split(self, X, y=None):
        '''"""Generate indices to split data into training and test set.'''
        rng = check_random_state(self.rs)
        iX = np.mgrid[0:X.shape[0]]
        for i in range(self.nb):
            train = resample(iX, random_state=rng)
            test = [item for item in iX if item not in train]
            yield (train,test)
