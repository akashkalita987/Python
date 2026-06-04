#easy reverse
subs = ["OS","Python","AWP","DBMS"]
print(subs[::-1])

#using loop
reve = []

for subjects in subs:
    reve.insert(0,subjects)
print(reve)

#using another method
reversed_list = []

for i in range(len(subs) -1, -1, -1):
    reversed_list.append(subs[i])
print(reversed_list)