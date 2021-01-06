Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:toluene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to toluene (PDB code:4w53) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of toluene were extracted from the original PDB structure (4w53). Toluene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of toluene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and toluene are:

- [`L99A-4w53.pdb`](L99A-4w53.pdb)

- [`toluene_oe.mol2`](toluene_oe.mol2)

Using the PDB file of the receptor and the mol2 file of toluene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

- [`complex.prmtop`](complex.prmtop)

- [`complex.inpcrd`](complex.inpcrd)
