class Solution(object):
    def numberOfBoomerangs(self, points):
        boomerangs=0
        for i in points:
            dismap={}
            for j in points:

                xdr=j[0]-i[0]
                ydr=j[1]-i[1]

                dis= xdr*xdr + ydr*ydr

                dismap[dis] = dismap.get(dis,0) + 1

            for m in dismap.values():
                boomerangs += m*(m-1)
        return boomerangs

               
        
