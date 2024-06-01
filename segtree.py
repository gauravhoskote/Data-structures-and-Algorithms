class segment_tree:

    def __init__(self, a, func):
        self.a = a
        self.t = [0]*(4*len(a))
        self.func = func
        self.build(1, 0, len(self.a)-1)

    def getrange(self, v, tl, tr, l, r):
        if l > r:
            return 0
        elif tl == l and tr == r:
            return self.t[v]
        else:
            tm = tl + ((tr - tl) // 2)
            return self.func(self.getrange(v*2, tl, tm, l, min(r,tm)) , self.getrange(v*2 + 1, tm+1, tr, max(tm+1, l), r))

    def build(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.a[tl]
        else:
            tm = tl + ((tr - tl) // 2)
            self.build(v*2, tl, tm)
            self.build(v*2+1, tm+1, tr)
            self.t[v] = self.func(arg1 = self.t[v*2] , arg2 = self.t[v*2+1])

    def update_element(self, v, newval, pos, tl, tr):
        if tl == tr:
            self.t[v] = newval
        else:
            tm = tl + (tr - tl)//2
            if tm > pos:
                self.update_element(2*v, newval, pos, tl, tm)
            else:
                self.update_element(2*v+1, newval, pos, tm+1, tr)
            self.t[v] = self.func(arg1 = self.t[v*2] , arg2 = self.t[v*2+1])
    
    def get_range(self, l,r):
        return self.getrange(1, 0, len(self.a)-1, l, r)

    def update(self, index, newval):
        self.a[index] = newval
        self.update_element(1, newval, index, 0, len(self.a)-1)


def func(arg1, arg2):
    return arg1+arg2


a = [1,2,3,4,5]

stree = segment_tree(a, func)

print(stree.get_range(1,4))
print(stree.get_range(1,2))
print(stree.get_range(1,3))
print(stree.get_range(3,4))


stree.update(0,10)
print(stree.get_range(0,2))

print(stree.a)
print(stree.t)

