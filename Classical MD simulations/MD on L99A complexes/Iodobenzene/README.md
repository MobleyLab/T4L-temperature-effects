Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:iodobenzene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to iodobenzene (PDB code:3dn4) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of conformer A of iodobenzene were extracted from the original PDB structure (3dn4). Iodobenzene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of iodobenzene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and the conformers A of iodobenzene are:

-[`L99A-3dn4.pdb`](L99A-4w53.pdb)

-[`iodobenzene-A_oe.mol2`](iodobenzene-A_oe.mol2)

Using the PDB file of the receptor and the mol2 file of iodobenzene, the protein-ligand complex (L99A:iodobenzene-A was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

-[`complex-A.prmtop`](complex-A.prmtop)

-[`complex-A.inpcrd`](complex-A.inpcrd)
