import subprocess
from itertools import product

import numpy as np
import triangle as tr
from scipy.sparse import save_npz
from stl import mesh

from config import CFG
from utils import is_positive_definite

from multiprocessing import Pool

def process_matrix(idx):
    # Run simulation and dump matrix.
    #subprocess.call(['../foam/sim/Allrun'])
    l_matrix = is_positive_definite('/home/zulinx/Projects/Ayano/code/tgsl/projects/lagrangian_fem/build/output/matrix_'+str(idx)+'.csv')
    save_npz('./data/L'+str(idx).zfill(3)+'.npz', l_matrix)

def lagrangian_fem():
    """Elastic FEM matrices"""
    #np.random.seed(CFG['SEED'])
    #for idx in range(CFG['DATA_COUNT']):
    with Pool() as p:
        p.map(process_matrix, [i for i in range(1000)])

    return True


def main():
    lagrangian_fem()
    return True


if __name__ == '__main__':
    main()
