import pickle as pk

my_data = {
    'name': 'python',
    'type': 'language',
    'version': '3.7'
}

with open('my_pickle.dat','wb') as f:
    pk.dump(my_data,f)

print('输出')
with open('my_pickle.dat','rb') as f:
    out = pk.load(f)

print('输出结果是,', out)