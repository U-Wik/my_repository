# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:30:42 2021

@author: Urban
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("This is process ", rank)

