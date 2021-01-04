Here you can find the files used to initialize the receptor for docking in the equilibrated cryo structure of T4-L99A with a closed loop conformation after 50 ns of MD simulations:

-[`cryo-equilibrated.pdb`](cryo-equilibrated.pdb): file used to define the receptor for docking with OEdock. This file was extracted from the MD trajectory corresponding to the MD simulations performed on the cryo apo structure of T4-L99A (PDB code: 4W51) in complex with toluene, after 50 ns of MD. The details of the MD simulations are reported in ../../../../../Classical MD simulations/MD with 3 loop conformation and in the Methods section of the paper.

 
-[`toluene_oe.mol2`](toluene_oe.mol2): file used to define the reference ligand (Toluene) in order to specify the binding site for docking with OEdock. The coordinates of toluene were extracted from the original PDB structure (4w53) after aligning 4w53 to the receptor structure: cryo-equilibrated.pdb. Toluene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of toluene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

