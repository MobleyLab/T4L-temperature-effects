filelist = []

# get the active score file paths
act = open("actfiles.txt", "r")
alines = act.readlines()
for l in alines:
	filelist.append("active-corrected/" + l.strip())
act.close()

# get the decoy score file paths
dec = open("decfiles.txt", "r")
dlines = dec.readlines()
for l in dlines:
	filelist.append("decoys/" + l.strip())
dec.close()

# get the mobley-active score file paths
mobact = open("mafiles.txt", "r")
mlines = mobact.readlines()
for l in mlines:
	filelist.append("mobley-active/" + l.strip())
mobact.close()


namefile = open("lignames.txt", "w")
scorefile = open("scores.txt", "w")

# get the names and the score
for fname in filelist:
	# write the name to lignames.txt file
	name = fname.split("-OEChem-")[0].split("/")[1]
	namefile.write("{}\n".format(name))

	f = open(fname, "r")
	lines = f.readlines()
	foundaffinity = False
	for l in lines:
		if l[0:9] == "Affinity:":
			score = l.split()[1]
			scorefile.write("{}\n".format(score))
			foundaffinity = True
	if foundaffinity == False:
		print(fname)
