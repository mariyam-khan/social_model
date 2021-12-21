
# An abstract government defining the Interface. 
class AbstractGovernment():
    def __init__(self):
        raise NotImplementedError()

    # Given a population sample, we want to get a policy decision
    def computePolicy(self, pops):
        raise NotImplementedError()

    # A Method to print our governemnt structure
    def __str__(self):
        raise NotImplementedError()

# A member of our population. might be extended with updating rules etc
class Pop():
    def __init__(self, Ocenter, I, bias, candidate=False):
        self.Ocenter = O
        self.I = I
        self.bias = bias
        self.candidate = candidate

    # find the local optimizer given the utility. should debate if utility should be fixed in constructor or here, but not too important I guess
    def findOptimum(self, utility):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

# A general population class. We might implement different realizations of populations or use samples from different populations in a single simulation
class AbstractPopulation():
    def __init__(self):
        raise NotImplementedError()
    
    # When we define specific populations, we just want to input a sample size to get a collection of members specified by our population instance
    def sample(self, samplesize):
        raise NotImplementedError()
    
    def __str__(self):
        raise NotImplementedError()


# Needs Population and Pop classes to have a working prototype
class BitMajDirectDemocracy(AbstractGovernment):
    def __init__(self):
        pass

    