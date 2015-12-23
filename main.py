import population as pop
import pheno as ph
import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    A = pop.Population ()
    B = ph.PhenoType ('Tail')
    C = ph.PhenoType ('Throat')
    A.add_pheno_type (B.my_ID, 0.1, 1, 1)
    A.add_pheno_type (C.my_ID, 0.3, 1, 1)
    A.initialize_population (10000, 0.5, 0.1)
    print(ph.PhenoType.ID) 
    
    for i in range(0,20):
        print(i)
        print(np.size(A.individuals))
        A.reproduction()

    fig, ax = plt.subplots(1,1)
    ax.hist(A.individuals[:,1],bins=100)
    plt.show()
