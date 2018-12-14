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

# Importing libraries
import glob
import re
import os

# set path for sli files
sli_path = "ENNI Dataset/SLI/*.txt"
sli_files = glob.glob(sli_path)

# set path for td files
td_path = "ENNI Dataset/TD/*.txt"
td_files = glob.glob(td_path)


def clean_sli():
    # initializing lists
    myList = []
    Filt_List1 = []
    Filt_List2 = []
    Filt_List3 = []

    # saving required patterns
    pattern1 = r'^\[.*\D?'  # pattern for opening bracket '['
    pattern2 = r'.*?\]'     # pattern for closing bracket ']'
    pattern3 = r'\+.*\D?'   # pattern for words with '+'
    pattern4 = r'\&.*\D?'   # pattern for words with '&'
    pattern5 = r'\[\* m\:\+[a-z]*\]'  # pattern for '[* m:+ed]
    # Filtering the data as required
    flag = False

    for each in file_object.split('\n'):

        if "%mor:" in each:
            flag = False

        if "*CHI:" in each:
            flag = True

        if flag:
            each = re.sub(pattern5, "temp", each)  # replacing [* m:+ed] with temp temporarily
            myList.append(each)

    for item in myList:
        Filtered_Lines = re.sub(r'\*CHI:\t', '', str(item))  # removing the *CHI: from the lines
        # keeping the required symbols in the files
        for word in Filtered_Lines.split():
            if word == "[/]":
                Filt_List1.append(str(word))

            elif word == "[//]":
                Filt_List1.append(str(word))

            elif word == "[*]":
                Filt_List1.append(str(word))

            # removing unnecessary patterns
            elif pattern2 is not None:
                suf = re.sub(pattern2, '', word)
                Filt_List1.append(str(suf))

            elif pattern1 is not None:
                pre = re.sub(pattern1, '', word)
                Filt_List1.append(str(pre))
            elif pattern2 is not None:
                pre = re.sub(pattern2, '', word)
                Filt_List1.append(str(pre))

            else:
                Filt_List1.append(str(word))

    for each in Filt_List1:
        # keeping the required symbols in the files
        for word in each.split():
            if word == "[/]":
                Filt_List2.append(str(word))
            elif word == "[//]":
                Filt_List2.append(str(word))
            elif word == "[*]":
                Filt_List1.append(str(word))

            # removing unnecessary patterns
            elif pattern1 is not None:
                pre = re.sub(pattern1, '', word)
                Filt_List2.append(str(pre))
            else:
                Filt_List2.append(str(word))

    for each in Filt_List2:
        for item in each.split():
            if item == "(.)":
                Filt_List3.append(str(item))
            elif item == "(..)":
                None
            elif pattern4 is not None:
                plus = re.sub(pattern4, '', item)
                Filt_List3.append(str(plus))
            elif pattern3 is not None:
                plus = re.sub(pattern3, '', item)
                Filt_List3.append(str(plus))
            else:
                each = each.replace("(", "")
                each = each.replace(")", "")
                Filt_List3.append(str(each))

    #removing unnecessary characters introduced during the filtering
    FilteredList = str(Filt_List3).replace("', '", " ")
    FilteredList = FilteredList.replace('"', "")
    FilteredList = FilteredList.replace("'", "")
    FilteredList = FilteredList.replace("<", "")
    FilteredList = FilteredList.replace(">", "")
    FilteredList = FilteredList.replace(". ", ".\n")
    FilteredList = FilteredList.replace("! ", "!\n")
    FilteredList = FilteredList.replace("? ", "?\n")
    FilteredList = FilteredList.replace("temp", "[* m:+ed]")  # again replacing temp with [* m:+ed]
    cleaned_sli.write(FilteredList)


def clean_td():
    # initializing lists
    myList = []
    Filt_List1 = []
    Filt_List2 = []
    Filt_List3 = []

    # saving required patterns
    pattern1 = r'^\[.*\D?'
    pattern2 = r'.*?\]'
    pattern3 = r'\+.*\D?'
    pattern4 = r'\&.*\D?'
    pattern5 = r'\[\* m\:\+[a-z]*\]'

    # setting flag as false
    flag = False
    # Filtering the data as required
    for each in file_object.split('\n'):

        if "%mor:" in each:
            flag = False

        if "*CHI:" in each:
            flag = True

        if flag:
            each = re.sub(pattern5, "temp", each)  # replacing [* m:+ed] with temp temporarily
            myList.append(each)

    for item in myList:
        Filtered_Lines = re.sub(r'\*CHI:\t', '', str(item))  # removing the *CHI: from the lines
        # keeping the required symbols in the files
        for word in Filtered_Lines.split():
            if word == "[/]":
                Filt_List1.append(str(word))

            elif word == "[//]":
                Filt_List1.append(str(word))

            elif word == "[*]":
                Filt_List1.append(str(word))
            # removing unnecessary patterns
            elif pattern2 is not None:
                suf = re.sub(pattern2, '', word)
                Filt_List1.append(str(suf))

            elif pattern1 is not None:
                pre = re.sub(pattern1, '', word)
                Filt_List1.append(str(pre))
            elif pattern2 is not None:
                pre = re.sub(pattern2, '', word)
                Filt_List1.append(str(pre))

            else:
                Filt_List1.append(str(word))

    for each in Filt_List1:
        # keeping the required symbols in the files
        for word in each.split():
            if word == "[/]":
                Filt_List2.append(str(word))
            elif word == "[//]":
                Filt_List2.append(str(word))
            elif word == "[*]":
                Filt_List2.append(str(word))
            # removing unnecessary patterns
            elif pattern1 is not None:
                pre = re.sub(pattern1, '', word)
                Filt_List2.append(str(pre))
            else:
                Filt_List2.append(str(word))

    for each in Filt_List2:
        for item in each.split():
            if item == "(.)":
                Filt_List3.append(str(item))
            elif item == "(..)":
                None
            elif pattern4 is not None:
                plus = re.sub(pattern4, '', item)
                Filt_List3.append(str(plus))
            elif pattern3 is not None:
                plus = re.sub(pattern3, '', item)
                Filt_List3.append(str(plus))
            else:
                each = each.replace("(", "")
                each = each.replace(")", "")
                Filt_List3.append(str(each))

    # removing unnecessary characters introduced during the filtering
    FilteredList = str(Filt_List3).replace("', '", " ")
    FilteredList = FilteredList.replace('"', "")
    FilteredList = FilteredList.replace("'", "")
    FilteredList = FilteredList.replace("<", "")
    FilteredList = FilteredList.replace(">", "")
    FilteredList = FilteredList.replace(". ", ".\n")
    FilteredList = FilteredList.replace("! ", "!\n")
    FilteredList = FilteredList.replace("? ", "?\n")
    FilteredList = FilteredList.replace("temp", "[* m:+ed]")  # again replacing temp with [* m:+ed]
    cleaned_td.write(FilteredList)  # writing the filtered list to the file


os.mkdir("sli_clean")
file_number_sli = 1
for names in sli_files:
    with open(names) as f:
        file_object = f.read()
        cleaned_sli = open("sli_clean/cleaned_sli"+str(file_number_sli)+".txt", "w+")
        clean_sli()
        cleaned_sli.close()
        file_number_sli = file_number_sli + 1
print("SLI files cleaned successfully and stored in 'sli_clean' directory\n")

os.mkdir("td_clean")
file_number_td = 1
for names in td_files:
    with open(names) as f:
        file_object = f.read()
        cleaned_td = open("td_clean/cleaned_td" + str(file_number_td) + ".txt", "w+")
        clean_td()
        cleaned_td.close()
        file_number_td = file_number_td + 1
print("TD files cleaned successfully and stored in 'td_clean' directory\n")


