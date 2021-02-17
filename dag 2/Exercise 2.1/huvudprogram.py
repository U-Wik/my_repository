import animals

m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()

f = animals.Fish()
f.printMembers()

d_f = animals.harmless.Birds()
d_f.printMembers()

d_f = animals.dangerous.Fish()
d_f.printMembers()


