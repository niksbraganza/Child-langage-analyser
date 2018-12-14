# Name:Nikhil Braganza
# Student_ID:29977770
# Start_Date: 28_Oct_2018
# Last_Modified:28_Oct_2018
#               31_Oct_2018
#               2_Oct_2018
#               6_Oct_2018
#               8_Oct_2018
#               9_Oct_2018
#               11_Oct_2018


import glob
import re


class Analyser:
    # initializing and defining variables ith default value '0'
    def __init__(self, transcript_length=0, vocab_size=0, no_of_repetition=0, no_of_retracing=0, no_of_errors=0, no_of_pauses=0):
        self.len = transcript_length
        self.siz = vocab_size
        self.rep = no_of_repetition
        self.ret = no_of_retracing
        self.err = no_of_errors
        self.poz = no_of_pauses

    def __str__(self):
        print("\n\n")
        print("Length of the transcript: " + str(self.len))
        print("Size of the vocabulary: " + str(self.siz))
        print("Number of repetition for certain words or phrases: " + str(self.rep))
        print("Number of retracing for certain words or phrases: " + str(self.ret))
        print("Number of grammatical errors detected: " + str(self.err))
        print("Number of pauses made: " + str(self.poz))

    def analyse_script(self, cleaned_file):
        complete_sli_list = []
        complete_td_list = []
        self.cleaned_file = cleaned_file
        files = glob.glob(cleaned_file)
        for name in files:
            with open(name) as f:
                file_obj = f.read()
                retracing_statements = re.findall(r'(\[//])', file_obj)
                for each in retracing_statements:
                    self.ret = self.ret + 1
                repeating_statements = re.findall(r'(\[/])', file_obj)
                for each in repeating_statements:
                    self.rep = self.rep + 1
                grammatical_errors = re.findall(r'(\[\* m:\+ed*\])', file_obj)
                for each in grammatical_errors:
                    self.err = self.err + 1
                number_of_pauses = re.findall(r'(\(.\))', file_obj)
                for each in number_of_pauses:
                    self.poz = self.poz + 1
                for each in file_obj.split("\n"):
                    self.len = self.len + 1

                new_list = file_obj.split()

                new_set = set(new_list)
                self.siz = self.siz + len(new_set)
                # print(self.size)
                if cleaned_file == "sli_clean/*.txt":
                    total_statistics = [0, self.len, self.siz, self.rep, self.ret, self.err, self.poz]
                else:
                    total_statistics = [1, self.len, self.siz, self.rep, self.ret, self.err, self.poz]

        return total_statistics


my_data = Analyser()
sli_path = "sli_clean/*.txt"
sli_files_cleaned = glob.glob(sli_path)
file_number = 1
for all in sli_files_cleaned:
    with open(all) as f:

        file_object = f.read()
        my_data.analyse_script("sli_clean/cleaned_sli"+str(file_number)+".txt")
        my_data.__str__()
        file_number = file_number + 1


my_data = Analyser()
td_path = "td_clean/*.txt"
td_files_cleaned = glob.glob(td_path)
file_number = 1

for all in td_files_cleaned:
    with open(all) as f:
        file_object = f.read()
        my_data.analyse_script("td_clean/cleaned_td"+str(file_number)+".txt")
        my_data.__str__()
        file_number = file_number + 1


