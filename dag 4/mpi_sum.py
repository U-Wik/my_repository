# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:30:42 2021

@author: Urban
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    sum = 0
    sum = sum + comm.recv(source=1)
    sum = sum + comm.recv(source=2)
    print('Process 0 reports: the sum of all involved ranks is', sum)
    
if rank == 1:
    comm.send(rank, dest=0)
    
if rank == 2:
    comm.send(rank, dest=0)

