mylist = ["cho", "meo", 'lon', 'ga']
hello = str(input())
print(mylist.index(hello))

































'''
class phan_so:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
    
    def __str__(self):
        return f"Tu so moi: {self.tu_so}\nMau so moi: {self.mau_so}"

    def add(self, other):
        tu_so_moi = (self.tu_so * other.mau_so) + (self.mau_so * other.tu_so)
        mau_so_moi = self.mau_so * other.mau_so
        return phan_so(tu_so_moi, mau_so_moi)
    
    def mini(self):
        u_tu_so = []
        u_mau_so = []
        uc = []
        for i in range(1, self.tu_so):
            if self.tu_so % i == 0:
                u_tu_so.append(i)
        for j in range(1, self.mau_so):
            if self.mau_so % j == 0:
                u_mau_so.append(j)
        uc.append(list(set(u_tu_so) & set(u_mau_so)))
        uc.sort()
        ucln = (uc[-1])[-1]
        min_tu_so = self.tu_so // ucln
        min_mau_so = self.mau_so // ucln
        return phan_so(min_tu_so, min_mau_so)

a = phan_so(1990, 66)
#b = phan_so(300, 20)

#result = a.add(b)
#mini_result = result.mini()
mini_result = a.mini()
#print(result)
print(mini_result)
'''