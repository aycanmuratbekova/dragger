x = {'tasks': ['Something', 'Do something else'], 'in progress': [], 'testing': [], 'done': []}
print(x['tasks'])
for key, value in x.items():
    print(
        key,
        value
    )
