from re import X
import subprocess
from os.path import exists


class MinTestSuite:

    def __init__(self):
        self.test_case_loc = "large-png-suite/"

        # remove previous coverage data
        if exists("cover.o"):
            subprocess.run("rm cover.o", shell=True)
            subprocess.run("cd libpng-1.6.34; rm *.gcda", shell=True)

        # check if total coverage has been calculated
        for i in range(0, 1639):
            print("RUNNING TEST CASE: ", i)
            cmd = "./libpng-1.6.34/pngtest " + self.test_case_loc + str(i) + ".png > out.o"
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        out = subprocess.run("cd libpng-1.6.34; gcov *.c > /media/sf_481-repos/hw5/part-c/total_cover.o", shell=True, stderr=subprocess.DEVNULL)

        # get full coverage value
        self.goal_cover = self.get_cover("total_cover.o")



    def run_test_cases(self, l1):

        # remove previous coverage data
        if exists("cover.o"):
            subprocess.run("rm cover.o", shell=True)
            subprocess.run("cd libpng-1.6.34; rm *.gcda", shell=True)

        # runs the test case and outputs the coverage for every test case in l1
        for i in l1:
            print("RUNNING TEST CASE: ", i)
            cmd = "./libpng-1.6.34/pngtest " + self.test_case_loc + str(i) + ".png > out.o"
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        out = subprocess.run("cd libpng-1.6.34; gcov *.c > /media/sf_481-repos/hw5/part-c/cover.o", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    def get_cover(self, file):
        # open coverage folder
        last_line = ""
        with open(file) as f:
            for line in f:
                pass
            last_line = line        

        # parse the coverage output
        x = last_line.split(":")[1].split("%")
        return float(x[0])      

    def is_interesting(self, l1):
        self.run_test_cases(l1)
        return self.get_cover("cover.o") == self.goal_cover

