import numpy as np
import numpy.random as random

class BinaryChromosome:

    def __init__(self, n_genes):
        self.n_genes = n_genes
        self.value = random.randint(0, 2, n_genes)

    def mutate(self, prob=0.2):
        """Perform random mutation.

        Parameters
        ----------
        prob : float in [0,1]
            Description of parameter `prob` (the default is 0.2).

        Returns
        -------
        None
            Perform mutation on the self.value attribute
        """

        mutation = np.where(random.rand(self.n_genes) < prob)
        self.value[mutation] ^= 1

class IntegerChromosome:

    def __init__(self, n_genes, max_):
        self.n_genes = n_genes
        self.max_ = max_
        self.value = random.randint(0, max_ + 1, n_genes)

    def mutate(self, prob=0.2):
        """Perform random mutation.

        Parameters
        ----------
        prob : float in [0,1]
            Description of parameter `prob` (the default is 0.2).

        Returns
        -------
        None
            Perform mutation on the self.value attribute
        """

        mutation = np.where(random.rand(self.n_genes) < prob)
        self.value[mutation] = random.randint(0, self.max_ + 1)
