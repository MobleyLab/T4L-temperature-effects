Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:ethylbenzene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to ethylbenzene (PDB code:4w54) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of ethylbenzene (the first conformer listed in the PDB 4w54) were extracted from the original PDB structure. Ethylbenzene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of ethylbenzene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and ethylbenzene are:

-[`L99A-4w54.pdb`](L99A-4w54.pdb)

-[`ethylbenzene_1_oe.mol2`](ethylbenzene_1_oe.mol2)

Using the PDB file of the receptor and the mol2 file of ethylbenzene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

-[`complex.prmtop`](complex.prmtop)

-[`complex.inpcrd`](complex.inpcrd)
