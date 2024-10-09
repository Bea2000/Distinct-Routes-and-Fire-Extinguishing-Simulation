# Obtiene N y M desde standard input
N, M = map(int, input().strip().split())

class FiremansTree:
    def __init__(self, value, origin, time=0):
        self.fireman = origin
        self.position = value
        self.time_spent = time
        self.left = None
        self.right = None
        self.current_distance = 0
        
    ''' Add value to tree '''
    def add(self, value, origin, time=0):
        if self.position > value:
            if self.left == None:
                self.left = FiremansTree(value, origin, time)
            else:
                self.left.add(value, origin, time)
        else:
            if self.right == None:
                self.right = FiremansTree(value, origin, time)
            else:
                self.right.add(value, origin, time)

    ''' remove value from tree '''
    def remove(self, value):
        if value < self.position:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.position:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            min_val = self.right.find_min()
            self.fireman = min_val.fireman
            self.position = min_val.position
            self.time_spent = min_val.time_spent
            self.current_distance = 0
            self.right = self.right.remove(min_val.position)
        return self
    
    ''' find min value in tree '''
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self
    
    ''' print tree '''
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.fireman, self.position, self.time_spent)
        if self.right:
            self.right.print_tree()
        
def getFiremansAndFires():
    ''' get firemans and fires from standard input '''
    # get fireman's position
    firemans = list(map(int, input().strip().split()))
    firemans.sort()
    # get fires position
    fires = list(map(int, input().strip().split()))
    fires.sort()
    return firemans, fires

def addFiremansToTree(firemans, firemans_tree):
    ''' add firemans to tree '''
    mid = len(firemans)//2
    for i in range(len(firemans)):
        if i != mid:
            firemans_tree.add(firemans[i], firemans[i])
    return firemans_tree

def getFiremanInBetween(fireman, fire):
    ''' return distance between fireman and fire '''
    if fire > fireman.fireman and fire < fireman.position:
        return "True"
    elif fire < fireman.fireman and fire > fireman.position: 
        return "True"
    else: 
        return abs(fireman.position - fire) + fireman.time_spent

def getNearestFiremanToFire(firemans_tree, fire, best):
    ''' return nearest fireman to fire '''
    # get distance to fire of actual fireman
    in_between = getFiremanInBetween(firemans_tree, fire)
    if in_between == "True":
        firemans_tree.current_distance = firemans_tree.time_spent
        firemans_tree.position = fire
        return firemans_tree
    else: 
        firemans_tree.current_distance = in_between
    # get fireman that is closer to fire
    # closer to the left
    if firemans_tree.position >= fire:
        if firemans_tree.left == None:
            best.position = fire
            return best
        else:
            temp_fireman_distance = abs(firemans_tree.left.position - fire) + firemans_tree.left.time_spent
            if temp_fireman_distance <= best.current_distance:
                best = firemans_tree.left
            return getNearestFiremanToFire(firemans_tree.left, fire, best)
    # closer to the right
    else:
        if firemans_tree.right == None:
            best.position = fire
            return best
        else:
            temp_fireman_distance = abs(firemans_tree.right.position - fire) + firemans_tree.right.time_spent
            if temp_fireman_distance < best.current_distance:
                best = firemans_tree.right
            return getNearestFiremanToFire(firemans_tree.right, fire, best)

def saveMax(a, b):
    ''' return max between a and b '''
    if a > b:
        return a
    return b
    
# get firemans and fires
firemans, fires = getFiremansAndFires()

# initialize tree with fireman in the middle
mid = N//2
tree = FiremansTree(firemans[mid], firemans[mid])

# add firemans to tree

addFiremansToTree(firemans, tree)

ans = -1
for i in range(M):

    # search in tree the nearest fireman to fire
    fireman = getNearestFiremanToFire(tree, fires[i], tree)

    # save max time spent
    ans = saveMax(ans, fireman.current_distance)

    # save fireman values
    temp_fireman_value = fireman.position
    temp_fireman_distance = fireman.current_distance
    temp_fireman_origin = fireman.fireman

    # update fireman actual position
    tree = tree.remove(fireman.position)
    # update fireman time spent
    tree.add(temp_fireman_value, time = temp_fireman_distance, origin = temp_fireman_origin)

# Entrega ans a standard output
print(ans)