from matplotlib import pyplot as plt
import random
import math



class Person():
    def __init__(self,startpos,step_value=1,maxdist=100):
        self.x=[startpos[0]]
        self.y=[startpos[1]]
        self.step_value=step_value
        self.maxdist=maxdist
        self.current_maxdist=0
        self.steps_taken=0
        self.init_values()

    def init_values(self):
        while self.current_maxdist<self.maxdist:
            r=random.choice([1,2,3,4])
            if r==1:
                self.x.append(self.x[-1]+self.step_value)
                self.y.append(self.y[-1])
            elif r==2:
                self.x.append(self.x[-1]-self.step_value)
                self.y.append(self.y[-1])
            elif r==3:
                self.y.append(self.y[-1]+self.step_value)
                self.x.append(self.x[-1])
            elif r==4:
                self.y.append(self.y[-1]-self.step_value)
                self.x.append(self.x[-1])

            current_dist=pow(pow(self.x[-1],2)+pow(self.y[-1],2),0.5)
            if current_dist>self.current_maxdist:
                self.current_maxdist=current_dist

            self.steps_taken+=1



p=Person((0,0))
# plt.plot(p.x,p.y)
plt.grid(True)
# plt.axis([0,100,0,100])
plt.plot(p.x,p.y)
print(p.steps_taken)
plt.show()
