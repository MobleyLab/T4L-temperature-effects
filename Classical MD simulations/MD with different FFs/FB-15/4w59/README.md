The PDB structure of L99A with an open F-helix conformation (PDB code: 4w59) was downloaded from the Protein Data Bank. To obtain an apo structure of L99A with an open F-helix conformation, we passed 4w59 through pdbfixer to remove the ligand and the water molecules, then to add the missing heavy atoms. We used PDB2PQR server to protonate the resulting PDB structure at pH 7 and to rename the residue/atom according to AMBER naming scheme. Then, we converted the resulting pqr file to a PDB file using Parmed. Finally, we parametrized and solvated the system with YANK, where the protein was modeled using AMBER FB-15 and TIP3P water model. The output files used to run MD simulations on this system are:

-[`L99A-o-fb15.prmtop`](L99A-o-fb15.prmtop)
-[`L99A-o-fb15.inpcrd`](L99A-o-fb15.inpcrd)
