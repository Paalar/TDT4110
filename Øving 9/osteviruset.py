cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A234-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

print("Hylleplassene til Port Salut er:", ", ".join(cheeses["port salut"]))

infected_cheeses = []
clean_cheeses = {}
hyller = ["B13-1","B13-2", "B13-3", "B13-4", "B14-1", "B14-2", "B14-3", "B14-4", "B15-1", "B15-2", "B15-3", "B15-4",
"A234-1", "A234-2", "A234-3", "A234-4", "A234-5", "A235-1", "A235-2", "A235-3", "A235-4", "C31-1", "C31-2" ]

for i in cheeses:
    clean_cheeses[i] = []
    for h in cheeses[i]:
        clean_cheeses[i].append(h)
        if h in hyller:
            infected_cheeses.append(i)
            clean_cheeses[i].remove(h)



print("\nThe potentially infected cheeses:", ", ".join(list(set(infected_cheeses))))
print("\nThe clean cheeses are:")

for i in clean_cheeses:
    for h in clean_cheeses[i]:
        print(h, i)
