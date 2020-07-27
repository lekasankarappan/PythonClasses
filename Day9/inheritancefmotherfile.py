from DAY8.Baseclass import Base

class Testcase01(Base):

    def Tc01(self):
        print("Tc01")

        self.click(self,"search")
        self.scroll(self,"End")


t=Testcase01()
t.Tc01()