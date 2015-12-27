import numpy as np

class Population:

    class phenoType:

        def __init__(self, ID, spread, attractiveness, initial_distribution):

            self.my_ID = ID
            self.spread = spread
            self.attractiveness = attractiveness
            self.initial_distribution = initial_distribution
            
    def __init__(self):

        self.pheno_types = []
    
    def add_pheno_type(self, ID, spread, attractiveness, initial_distriubtion):

        pheno = Population.phenoType(
                ID,
                spread, 
                attractiveness, 
                initial_distriubtion)
        self.pheno_types.append(pheno)
     
    def initialize_population (self, initial_number, reproductivity_loc,
            reproductivity_std):
    
        self.number_of_individuals = initial_number
        self.reproductivity_loc = reproductivity_loc
        self.reproductivity_std = reproductivity_std
        number_of_phenos = len(self.pheno_types)
        individuals = np.zeros((initial_number,number_of_phenos)) 

        for i in range(0,number_of_phenos):
            temp_phenos = []
            for j in range(0,len(individuals[:,i])):
                dist_number = -1
                while dist_number > 1 or dist_number < 0:
                    dist_number = np.random.normal(
                            loc=0.5,
                            scale=self.pheno_types[i].spread,
                            size=1)
                temp_phenos.append(dist_number)

            
            individuals[:,i] = temp_phenos

        self.individuals = individuals
        self.number_of_phenos = number_of_phenos

    def reproduction(self):

        number_of_old = self.number_of_individuals 
        number_of_new = int(np.floor(
                np.random.normal(
                    loc=self.reproductivity_loc,
                    scale=self.reproductivity_std,
                    size=1)*number_of_old)[0])

        self.number_of_individuals += number_of_new
        self.individuals.resize(
                self.number_of_individuals,
                #number_of_old+number_of_new,
                self.number_of_phenos)

        for i in range(0, self.number_of_phenos):
            self.individuals[number_of_old:,i] = np.random.normal(
                    loc=0.5+self.pheno_types[i].attractiveness,
                    scale=self.pheno_types[i].spread,
                    size=number_of_new)


        self.individuals[self.individuals > 1] = 1
        self.individuals[self.individuals < 0] = 0

#if __name__ == '__main__':
#
#    A = Population()
#    A.add_pheno_type(0.1,1,1)
#    #A.add_pheno_type(0.0132,1,1)
#    A.initialize_population (100000,0.5,0.1)
#    for i in range(0,100):
#        print(i)
#        print(np.size(A.individuals))
#        A.reproduction()
#
#    fig, ax = plt.subplots(1,1)
#    ax.hist(A.individuals[:,0],bins=100)
#    plt.show()
