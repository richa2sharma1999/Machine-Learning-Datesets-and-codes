#d assuming d has one to many relationship for key and values

final = {}
for i in d.keys():
	if(d[i] in final.keys()):
		final[d[i]].push(i)]
	else:
		final[d[i]] = []
		final[d[i]].push(i)

print(final)