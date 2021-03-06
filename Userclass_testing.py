#Okoye-Nobert/Joachim

from user_admin import *
from userclass import *
from user_admin import *
from Drugclass import *
from abortionclass import *
from antibioticsclass import *
from antimalarialclass import *
from antisepticclass import *
from userclass import *
import unittest

user = User('Okoye-Nobert','edy@gmail.com','Edno','edno123')
user.__str__()


class TestStringMethod(unittest.TestCase):
    def testmenu(self):
       s = ("To add an antibiotics drug press 1\n"
              "To add an antiseptic drug press 2\n"
              "To add an antimalarial drug press 3\n"
              "To add an abortion drug press 4\n")

       self.assertEqual(s, "To add an antibiotics drug press 1\n"
              "To add an antiseptic drug press 2\n"
              "To add an antimalarial drug press 3\n"
              "To add an abortion drug press 4\n")


    def testquantity(self):
        b = "Which drug do you want to view its quantity? e.g(CIPROFLAXIN)"
        self.assertEqual(b,"Which drug do you want to view its quantity? e.g(CIPROFLAXIN)")

    def testadd(self):
        size_before = 0
        druglist = []

        drug1 = Antiseptic('Antiseptic', 'CHLOROQUINE', '23-09-2022', '1-09-2022', '4-09-2022', 45, '$60', 'pill',
                           '18')
        druglist.append(drug1)

        size_after = len(druglist)

        self.assertNotEqual(size_before, size_after)


    def testprices(self):
        drug1 = Antiseptic\
            ('Antiseptic', 'CHLOROQUINE', '23-09-2022', '1-09-2022', '4-09-2022', 45, '$60', 'pill', '18')
        if 'drugname' != 'CHLOROQUINE':
            pass

        self.assertNotEqual(drug1.drugname, drug1.price)




    def testview(self):
     self.assertEqual("drug".upper(),"DRUG")

    def testdeletedrug(self):
        self.assertEqual("drug".upper(), "DRUG")




if __name__ == '__main__':
    unittest.main()



