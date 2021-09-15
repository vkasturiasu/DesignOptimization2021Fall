dim =4
mat_fin = []
for i in range(dim):
    mat = input('enter {}th row'.format(str(i)))
    mat1 = mat.split();
    mat2 = [int(x) for x in mat1]
    mat_fin.append(mat2)

