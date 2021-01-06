Here, you can find the protocol used to prepare the input files used to run MD simulations on L99A:benzylacetate complex as well as the input files.

**System setup**

There are no co-crystal structures available in the Protein Data Bank for L99A:benzylacetate. Based on the concept that similar molecules bind to a protein in a similar trend, we chose the co-crystal structure of the closest congeneric ligand (butylbenzene; PDB code: 4w57) that we modified using Chimera to generate the 3D structure of benzylacetate (mol2 format). The receptor structure prepared from the L99A:butylbenzene complex [`L99A-4w57.pdb`](../N-butylbenzene/L99A-4w57.pdb) was used to form the L99A:benzylacetate complex. The generated structures of benzylacetate (considered neutral) and the receptor are:

- [`L99A-4w57.pdb`](L99A-4w57.pdb)

- [`benzylacetate-from-butyl_oe.mol2`](benzylacetate-from-butyl_oe.mol2)

Using the above structures, the protein-ligand complex was generated, parametrized, and solvated with YANK 0.17.0, which led to the following AMBER files that we used to run MD simulations:

- [`complex.prmtop`](complex.prmtop)

- [`complex.inpcrd`](complex.inpcrd)
