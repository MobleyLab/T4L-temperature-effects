# Docking of T4 compounds

Here you will find the files of the compounds we docked within the different structures of the T4 lysozyme and other docking information.

## Manifest

- [`decoys.smi`](decoys.smi): file containing the SMILES strings of the 3152 property-matched DUD-E decoys
- [`zinc.smi`](zinc.smi): file containing 35 ZINC compounds (described as binders)
- [`mobley-minh-actives.smi`](mobley-minh-actives.smi): file containing experimentally confirmed T4-L99A binders obtained from https://github.com/MobleyLab/lysozyme_binding, which contains compounds from the following study: B. Xie, T. H. Nguyen, D. D. L. Minh, Absolute Binding Free Energies between T4 Lysozyme and 141 Small Molecules: Calculations Based on Multiple Rigid Receptor Configurations. J Chem Theory Comput 13, 2930-2944 (2017)
- [`OEdock.ipynb`](OEdock.ipynb): Jupyter notebook used for docking all the T4 compounds within the T4 lysozyme structures using OEdock (OpenEye Scientific Software). This notebook was written based on teaching material prepared by David Mobley.
- [`files-to-prepare-receptors`](files-to-prepare-receptors): files used to initialize the docking (using OEdocking) of T4 compounds into the different apo structures of T4-L99A
