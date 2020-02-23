
import os.path as P
import os
import yaml

project_dir = '/Users/doayakut/Desktop/third'
immutable_dir = P.join(project_dir, 'data', 'immutable')

def print_csv_details(fname):
    print('-' * 80 + '\n\n' + fname)
    
    
    with open(P.join(immutable_dir,fname), 'r') as fp:
        print("\nFields:")
        
        for field in fp.readline().split(','):
            print(' -', field)

def print_json_details(fname):
    print('-' * 80 + '\n\n' + fname)
    
    c = 0
    field_sets = set()
    with open(P.join(immutable_dir,fname), 'r') as fp:
        for line in fp:
            if c == 10000:
                break
            try:
                c += 1
                data = yaml.load(line)
                field_sets.add(",".join(list(data.keys())))
            except:
                print(line)

    print(field_sets)



print('\n\nImmutable datasets:')
for fname in os.listdir(immutable_dir):
    print(' -', fname)

for fname in os.listdir(immutable_dir):

    if fname[-4:] == ".csv":
        print_csv_details(fname)
    
    # if fname[-4:] == "json":
    #     print_json_details(fname)
