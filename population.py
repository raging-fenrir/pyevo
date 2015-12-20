import numpy as np

class Population:

    class phenoType:
        ID = 0
        def __init__(self, spread, attractiveness, initial_distribution):

            self.my_ID = Population.phenoType.ID
            self.spread = spread
            self.attractiveness = attractiveness
            self.initial_distribution = initial_distribution
            Population.phenoType.ID += 1
            
    def __init__(self):

        self.pheno_types = []
    
    def add_pheno_type(self, spread, attractiveness, initial_distriubtion):

        pheno = Population.phenoType(
                spread, 
                attractiveness, 
                initial_distriubtion)
        self.pheno_types.append(pheno)
    
    def initialize_population (self, initial_number):

        number_of_phenos = len(self.pheno_types)
        self.individuals = np.zeros((initial_number,number_of_phenos)) 
        for i in range(0,number_of_phenos):
            self.individuals[:,i] = np.random.binomial(
                    n=self.pheno_types[i].spread,
                    p=0.5,
                    size=initial_number)/self.pheno_types[i].spread

    def reproduction(self):
        
        


if __name__ == '__main__':
    A = Population()
    A.add_pheno_type(10,1,1)
    A.add_pheno_type(100,2,2)
    A.add_pheno_type(1000,3,3)
    A.add_pheno_type(10000,4,4)
    A.add_pheno_type(100000,5,5)
    A.initialize_population (10)
    #print(A.individuals)
    #for i in A.pheno_types:
    #    print(i.my_ID)
