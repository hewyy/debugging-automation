import sys
import math

class Ochiai:
    def get_cla(self):
        self.failed_file = []
        self.passed_file = []

        for i in sys.argv:
            if "fail" in i:
                self.failed_file.append(i)
            else:
                self.passed_file.append(i)

    def __init__(self):
        self.get_cla()
        self.total_failed = len(self.failed_file)
        print(self.total_failed)
        
        self.passed_statement_info = {}
        self.failed_statement_info = {}
        self.max_line_number = 0

    def run(self):

        # callect all the failed statement information
        for file in self.failed_file:
            with open(file) as f:
                for line in f:
                    x = line.split(":")
                    print(x[0].strip())
                    if x[0].strip().isnumeric():
                        if not x[1].strip().isnumeric(): 
                            continue
                        line_num = int(x[1])
                        if line_num not in self.failed_statement_info:
                            self.failed_statement_info[line_num] = 0.0
                        self.failed_statement_info[line_num] += 1.0
                        if line_num > self.max_line_number:
                            self.max_line_number = line_num
                    

        # collect all the passed statement information
        for file in self.passed_file:
            with open(file) as f:
                for line in f:
                    x = line.split(":")
                    if x[0].strip().isnumeric():
                        if not x[1].strip().isnumeric(): 
                            continue
                        line_num = int(x[1])
                        if line_num not in self.passed_statement_info:
                            self.passed_statement_info[line_num] = 0.0
                        self.passed_statement_info[line_num] += 1.0
                        if line_num > self.max_line_number:
                            self.max_line_number = line_num


    def calculate_sus(self, line_number):
        failed = 0.0
        passed = 0.0

        if line_number in self.failed_statement_info:
            failed = self.failed_statement_info[line_number]

        if line_number in self.passed_statement_info:
            passed = self.passed_statement_info[line_number]

        dem = math.sqrt(self.total_failed*(failed + passed))
        if dem == 0:
            return -1
        
        return failed / dem

    def full_calc(self):

        line_num = 0
        self.final_numbers = []
        for line_num in range(self.max_line_number + 1): # this is assuming that every line is in every file
            sus_rating = self.calculate_sus(line_num)
            if sus_rating == -1:
                continue
            tup = (line_num, sus_rating)
            self.final_numbers.append(tup)
            print("here")

        # sort
        self.final_numbers.sort(key=lambda x: x[1], reverse=True)



    def get_final(self):
        if len(self.final_numbers) > 100:
            return self.final_numbers[:100]
        else:
            return self.final_numbers


a = Ochiai()
a.run()
a.full_calc()
print(a.get_final())

