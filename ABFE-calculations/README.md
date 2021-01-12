We performed absolute binding free energy simulations on L99A complexed with the following ligands: iodobenzene, toluene, o-xylene, p-xylene, ethylbenzene, propylbenzene, butylbenzene, 3-iodotoluene, 4-iodotoluene and benzylacetate. The protocol used to prepare the PDB structures of the receptors and the mol2 files of the ligands is described for each ligand in the respective subdirectory under [`MD_on_L99A_complexes`](../MD-simulations/MD_on_L99A_complexes).

In the following subdirectories, we provide the input files as well as the yaml files used to absolute binding free energy calculations on each of our T4 lysozyme complexes.

- [`toluene`](toluene)
- [`iodobenzene`](iodobenzene)
- [`o-xylene`](o-xylene)
- [`p-xylene`](p-xylene)
- [`ethylbenzene`](ethylbenzene)
- [`propylbenzene`](propylbenzene)
- [`butylbenzene`](butylbenzene)
- [`3-iodotoluene`](3-iodotoluene)
- [`4-iodotoluene`](4iodotoluene)
- [`benzylacetate`](benzylacetate)

For iodobenzene, o-xylene, and toluene, we also used the L99A RT co-crystal structures to set up additional binding free energy calculations. The respective input files and yaml files can be found in:

- [`iodobenzene-rt`](iodobenzene-rt)
- [`o-xylene-rt`](o-xylene-rt)
- [`toluene-rt`](toluene-rt)

Also, we added iodobenzene, toluene, and o-xylene to the apo RT structure of L99A to form 3 complexes on which we performed binding free energy calculations. The respective input files and yaml files can befound in:

- [`iodobenzene-apo-rt`](iodobenzene-apo-rt)
- [`o-xylene-apo-rt`](o-xylene-apo-rt)
- [`toluene-apo-rt`](toluene-apo-rt)

PS. We used minimize=yes (yaml files) on the starting structure of each calculation.
