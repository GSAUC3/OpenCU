import numpy as np 

class Ftransforms:

    def __init__(self,mat):
        self.m = mat
        self.N=len(mat)
    
    def twiddle(self): 
    # twiddle factor
        twiddleFactor=np.full((self.N,self.N),complex(0,0))
        for i in range(self.N):
            for j in range(self.N):
                x=np.exp((complex(0,-1)*2*np.pi*i*j)/self.N)
                twiddleFactor[i][j]=np.around(x,decimals=4,out =None)
        return twiddleFactor
    

    def dft(self):
    # discrete fourier transform of a given sequence
        ans=[]
        t=self.twiddle()    
        for i in t:
            ans.append(sum(i*self.m))
        return ans

    


        