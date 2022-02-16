labels = {1:'A', 2:'B', 3:'C'}
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk A from peg",source,"to peg",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",labels[n],"from peg",source,"to peg",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 3
TowerOfHanoi(n,1,3,2)
