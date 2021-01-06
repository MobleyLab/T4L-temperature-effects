Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:o-xylene complex as well as the input files.

**System setup**

The crystallographic structure of T4 lysozyme (L99A) bound to o-xylene (PDB code:188L) was downloaded from the RCSB Protein Data Bank. We used pdbfixer 1.4 to remove the ligand and the water molecules from the original PDB structure and to add the missing heavy atoms to the receptor. Then, PDB2PQR server was used to protonate the receptor's residues at pH 7 and to rename the residue/atom according to the AMBER naming scheme.
The coordinates of o-xylene were extracted from the original PDB structure (188L). O-xylene was considered neutral and was protonated using Chimera 1.12. Then, the PDB file of o-xylene was converted to a mol2 file using OpenEye toolkits (OpenEye Scientific Software).

The prepared structures of the receptor and o-xylene are:

- [`L99A-188l.pdb`](L99A-188l.pdb)

- [`o-xylene_oe.mol2`](o-xylene_oe.mol2)

Using the PDB file of the receptor and the mol2 file of o-xylene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

- [`complex.prmtop`](complex-A.prmtop)

- [`complex.inpcrd`](complex-A.inpcrd)
