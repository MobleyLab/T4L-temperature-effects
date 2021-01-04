Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:hexylbenzene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to hexylbenzene (PDB code:4w59) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of hexylbenzene (first conformer of hexylbenzene listed in 4w59) were extracted from the original PDB structure (4w59). Hexylbenzene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of hexylbenzene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and hexylbenzene are:

-[`L99A-4w59.pdb`](L99A-4w59.pdb)

-[`hexylbenzene_1_oe.mol2`](hexylbenzene_oe.mol2)

Using the PDB file of the receptor and the mol2 file of hexylbenzene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

-[`complex.prmtop`](complex.prmtop)

-[`complex.inpcrd`](complex.inpcrd)
