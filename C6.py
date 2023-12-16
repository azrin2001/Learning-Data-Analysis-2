x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com', 'Fahima Azrin': 'f.a.h.i.m.a.z.r.i.n5060@gmail.com'}
print(x['Fahima Azrin'])
x['Kevyn Collins-Thompson'] = None
print(x['Kevyn Collins-Thompson'])
for name in x:
    print(x[name])
for email in x.values():
    print(email)
for name, email in x.items():
    print(name)
    print(email)
