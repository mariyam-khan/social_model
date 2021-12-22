import numpy as np
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
        self.Ocenter = Ocenter
        self.I = I
        self.bias = bias
        self.candidate = candidate
        self.optimum = Ocenter
        self.policysize = len(Ocenter)


    # find the local optimizer given the utility. should debate if utility should be fixed in constructor or here, but not too important I guess
    def findOptimum(self, utility):
        raise NotImplementedError()

    def __str__(self):
        ret = "Center: " + str(self.Ocenter) + "\n"
        ret += "Radius: " + str(self.I) + "\n"
        ret += "Bias: " + str(self.bias) + "\n"
        if self.candidate:
            ret += "Is a Candidate" + "\n"
        ret += "Optimal Opinion: " + str(self.optimum) + "\n"
        ret += "Size of Policy: " + str(self.policysize) + "\n"
        
        return ret

# A general population class. We might implement different realizations of populations or use samples from different populations in a single simulation
class AbstractPopulation():
    def __init__(self):
        raise NotImplementedError()
    
    # When we define specific populations, we just want to input a sample size to get a collection of members specified by our population instance
    def sample(self, samplesize):
        raise NotImplementedError()
    
    def __str__(self):
        raise NotImplementedError()
class UniformPopulation(AbstractPopulation):
    def __init__(self):
        pass
    def sample(self, samplesize, policysize):
        I=0
        bias=0
        return [Pop(np.random.randint(0,2,policysize), I, bias) for k in range(samplesize)]

# Needs Population and Pop classes to have a working prototype
class BitMajDirectDemocracy(AbstractGovernment):
    def __init__(self):
        pass
    def computePolicy(self, pops):
        n = len(pops)
        d = pops[0].policysize
        result = np.zeros(d, dtype=int)
        for pop in pops:
            result += pop.optimum
        result = (result > n//2)
        return result 

a = UniformPopulation()
pops = a.sample(3, 1)
b = BitMajDirectDemocracy()
print(b.computePolicy(pops))
for pop in pops:
    print(pop)    