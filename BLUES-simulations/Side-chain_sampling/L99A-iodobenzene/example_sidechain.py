from blues.moves import SideChainMove
from blues.moves import MoveEngine
from blues.simulation import *
import json
from blues.settings import *
from blues.simulation import *
import json
from blues.settings import *

# Parse a YAML configuration, return as Dict
cfg = Settings('sidechain_cudayaml').asDict()
structure = cfg['Structure']

#Select move type
sidechain = SideChainMove(structure, [1])
#Iniitialize object that selects movestep
sidechain_mover = MoveEngine(sidechain)

#Generate the openmm.Systems outside SimulationFactory to allow modifications
systems = SystemFactory(structure, sidechain.atom_indices, cfg['system'])

#Generate the OpenMM Simulations
simulations = SimulationFactory(systems, sidechain_mover, cfg['simulation'], cfg['md_reporters'],
                                cfg['ncmc_reporters'])

# Run BLUES Simulation
blues = BLUESSimulation(simulations, cfg['simulation'])
blues.run()

#Analysis
import mdtraj as md
import numpy as np

traj = md.load('step8.rst7', top='complex.prmtop')

indicies = np.array([ [ 1733, 1735, 1737, 1739 ],   # val111
                      [ 1827, 1829, 1831, 1834 ] ]) # leu118

dihedraldata = md.compute_dihedrals(traj, indicies)
with open("dihedrals.txt", 'w') as output:
    for value in dihedraldata:
        output.write("%s\n" % str(value)[1:-1])

