The PDB structure of apo L99A with a closed F-helix conformation (PDB code: 4w51) was downloaded from the Protein Data Bank. Then, we used pdbfixer to remove the water molecules and to add the missing heavy atoms. We used PDB2PQR server to protonate the resulting PDB structure at pH 7 and to rename the residue/atom according to AMBER naming scheme. Then, we converted the resulting pqr file to a PDB file using Parmed. Finally, we parametrized and solvated the system with YANK, where the protein was modeled using AMBER ff14SB and TIP3P water model. The output files used to run MD simulations on this system are:

- [`L99A-c-ff14sb.prmtop`](L99A-c-ff14sb.prmtop)
- [`L99A-c-ff14sb.inpcrd`](L99A-c-ff14sb.inpcrd)
