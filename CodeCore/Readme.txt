This python script is used to identify the aromatic residues facing the internal cavity formed by the TM1 to TM4 helixes in a set of ion channel structures extracted from PDB files, returning a list for each PDB file of pairs and clusters of aromatic residues with lower distances, compared with a given threshold.

For this, the distances between all alpha carbons in opposing helixes (TM1-TM3 and TM2-TM4) are calculated, choosing the nearest residue pairs. The same procedure is followed for gamma/alpha pairs. Those residues with (Cα-Cα)distance > (Cα-CƳ)distance is recorded in a list. After, it calculates distances between all atoms in pairs of aromatic residues in this list and keeps the minimal distances between pairs. Then, the third code groups in clusters all the pairs with a distance below a defined threshold.

Procedure:
The codes need the set of PDB files in a subfolder (in the included example C:\CodeCore\PDBs\ ). They also need a file with the information of the PDB ID and the limits of each transmembrane helix. In the included example, (C:\CodeCore\Aromatics\PDBfiles.txt), there is an extra column with the protein sequence ID used in the alignment used to determine the same segment of different channels. Other two empty folders are needed for the code to run: 
C:\CodeCore\Aromatics\1AromaticPositions
C:\CodeCore\Aromatics\2AromaticDistancesPares

After having all the needed files and subfolders set, the codes have to be executed sequentially in the order: ExtractAromaticOnCore.py -> ExtractDistancesAromaticPairsOnCore.py -> GroupingClusters.py

The last code will give a list of PDB IDs with the corresponding pairs and clusters of aromatic residues with lower distances, compared with the threshold. 