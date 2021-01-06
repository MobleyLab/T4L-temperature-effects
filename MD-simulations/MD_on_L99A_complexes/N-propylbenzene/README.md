Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:propylbenzene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to propylbenzene (PDB code:4w55) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of propylbenzene (first conformer of propylbenzene listed in 4w55) were extracted from the original PDB structure (4w55). Propylbenzene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of propylbenzene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and propylbenzene are:

- [`L99A_4w55.pdb`](L99A_4w55.pdb)

- [`propylbenzene_1_oe.mol2`](propylbenzene_1_oe.mol2)

Using the PDB file of the receptor and the mol2 file of propylbenzene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

- [`complex.prmtop`](complex.prmtop)

- [`complex.inpcrd`](complex.inpcrd)
