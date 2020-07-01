d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4 = {}
for d in d1:
	d4[d]=d1[d]	
for d in d2:
	d4[d]=d2[d]
for d in d3:
	d4[d]=d3[d]
print("sample dictonaries\nd1={1:10, 2:20}\nd2={3:30, 4:40}\nd3={5:50,6:60} ")	
print("concatenated dictornay:",d4)