# Convert the assign the numbers as a list to pico 


pico = '''
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10 
'''

# convert the string to a list
pico = [int(i) for i in pico.split()]
print(pico)

for x in pico:
    print(chr(x), end='')