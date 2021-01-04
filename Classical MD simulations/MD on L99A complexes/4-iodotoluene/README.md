Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:4-iodotoluene complex as well as the input files.

**System setup**

There are no co-crystal structures available in the Protein Data Bank for T4 lysozyme:4-iodotoluene. Based on the concept that similar molecules bind to a protein in a similar trend, we used a PDB file of the L99A:3-iodotoluene complex from a previous study (Gill et al., 2018; doi.org/10.1021/acs.jpcb.7b11820), where BLUES technique was used to sample and identify the binding mode of 3-iodotoluene; the resulting dominant binding mode of 3-iodotoluene was used here to generate the 3D structure of 4-iodotoluene using Chimera. The generated structure of 4-iodotoluene and the coordinates of the receptor extracted from the BLUES simulations performed by Gill et al were used to prepare the following structures of the receptor and the ligand:

-[`L99A.pdb`](L99A.pdb)

-[`4-iodotoluene_oe.mol2`](4-iodotoluene_oe.mol2)

Using the PDB file of the receptor and the mol2 file of 4-iodotoluene, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

-[`complex.prmtop`](complex.prmtop)

-[`complex.inpcrd`](complex.inpcrd)
