from blues.moves import RandomLigandRotationMove
from blues.engine import MoveEngine
from blues.simulation import *
import json
from blues.settings import *

def rotmove_cuda(yaml_file):
    # Parse a YAML configuration, return as Dict
    cfg = Settings('rotmove_cuda.yaml').asDict()
    structure = cfg['Structure']

    #Select move type
    ligand = RandomLigandRotationMove(structure, 'MOL')
    #Iniitialize object that selects movestep
    ligand_mover = MoveEngine(ligand)

    #Generate the openmm.Systems outside SimulationFactory to allow modifications
    systems = SystemFactory(structure, ligand.atom_indices, cfg['system'])

    #Freeze atoms in the alchemical system to speed up alchemical calculation
    cfg['freeze'] = { 'freeze_distance' : 12 ,
                      'freeze_center' : ':MOL',
                      'freeze_solvent': ':HOH,NA,CL'}

    systems.alch = systems.freeze_radius(structure, systems.alch, **cfg['freeze'])

    #Generate the OpenMM Simulations
    simulations = SimulationFactory(systems, ligand_mover, cfg['simulation'], cfg['md_reporters'],
                                    cfg['ncmc_reporters'])

    # Run BLUES Simulation
    blues = BLUESSimulation(simulations, cfg['simulation'])
    blues.run()


if __name__ == "__main__":
    rotmove_cuda('rotmove_cuda.yaml')
