import pickle

values = ['camembert', 'coulomnier', 'brie']

file = open('data.pkl', 'wb')
pickle.dump(values, file)
file.close()

file = open('data.pkl', 'rb')
values_to_load = pickle.load(file)
file.close()

print(values_to_load)

values_to_load.append('munster')
values_to_load.append('gruyere')
values_to_load = sorted(values_to_load)

print(values_to_load)

file = open('data.pkl', 'wb')
pickle.dump(values_to_load, file)
file.close()

file = open('data.pkl', 'rb')
values_to_load = pickle.load(file)
file.close()

print(values_to_load)

# l programme stoque la liste values dans un fichier pickels et puis lit ce même fichier et imprime sont contenu