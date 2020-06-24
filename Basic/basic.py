

######################
# beautiful code for making key, value 
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
# {5: 35044.51299744237, 25: 29016.41319191076, 50: 27405.930473214907, 100: 27282.50803885739, 250: 27893.822225701646, 500: 29454.18598068598}
best_tree_size = min(scores, key=scores.get)

# one line if
value = 10 if x > 0 else 20

# Array Copy
train_X_plus = train_X.copy()

# for loop with step
def srange(start, stop, step):
    numelements = int((stop-start-1)/float(step))
    print(numelements)
    for i in range(numelements + 1):
        yield start + i * step