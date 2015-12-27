import population as pop
import pheno as ph
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    A = pop.Population ()
    B = ph.PhenoType ('Tail')
    C = ph.PhenoType ('Throat')
    A.add_pheno_type (B.my_ID, 0.15, 0.003, 1)
    A.add_pheno_type (C.my_ID, 0.12, 0.0005, 1)
    A.initialize_population (10000, 0.5, 0.1)
    print(ph.PhenoType.ID) 
    
    #fig, ax = plt.subplots(1,1)
    #ax.hist(A.individuals[:,1],bins=100)
    #plt.show()
    for i in range(0,10):
        fig, ax = plt.subplots(1,1)
        ax.hist(A.individuals[:,1],bins=100)
        ax.hist(A.individuals[:,0],bins=100)
        plt.show()
        print(i)
        print(np.size(A.individuals))
        A.reproduction()

