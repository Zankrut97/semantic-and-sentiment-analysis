import math
from prettytable import PrettyTable
from decimal import Decimal
import csv

#taking counter for each word that is present in the file
i =1
canada=0
university = 0
dalhousie_university = 0
business =0
halifax=0

#look for university in all the files: https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        if 'university' in f.read():
            university+=1
    i+=1
#look for canada in all the files    
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        if 'canada' in f.read():
            canada+=1
    i+=1
#look for dalhousie university in all the files    
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        if 'dalhousie university' in f.read():
            dalhousie_university+=1
    i+=1
#look for business in all the files    
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        if 'business' in f.read():
            business+=1
    i+=1
#look for halifax in all the files    
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        if 'halifax' in f.read():
            halifax+=1
    i+=1

#calculating log: https://www.tutorialspoint.com/python3/number_log10.htm
#rounding of to two decimal places :https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
canada_log = round(math.log10(140/canada),2)
university_log = round(math.log10(140/university),2)
daluni_log = round(math.log10(140/dalhousie_university),2)
business_log = round(math.log10(140/business),2)
halifax_log = round(math.log10(140/halifax),2)

#adding values to pretty tables: http://zetcode.com/python/prettytable/
tab = PrettyTable()
tab.field_names = ["Search Query","Document containing term(df)","Total Documents(N)/Document containing term(df)","LOG10(N/df)"]
tab.add_row(["canada",canada,round(140/canada,2),canada_log])
tab.add_row(["university",university,round(140/university,2),university_log])
tab.add_row(["dalhousie university",dalhousie_university,round(140/dalhousie_university,2),daluni_log])
tab.add_row(["business",business,round(140/business,2),business_log])
tab.add_row(["halifax",halifax,round(140/halifax,2),halifax_log])

#print(tab)
#Convert Pretty Table to CSV : https://stackoverflow.com/questions/32128226/convert-python-pretty-table-to-csv-using-shell-or-batch-command-line
out_csv_list = []
table=tab.get_string()
for row in table.splitlines():
    rowdata = row.split("|")
    if len(rowdata) == 1:
        continue  
    data_list = []
    for colmn in rowdata:
        colmn = colmn.strip()
        if colmn:
            data_list.append(colmn)
    out_csv_list.append(data_list)
with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\semantic A.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(out_csv_list)

canada_counter={}
file_length={}
for i in range(1,140):
    with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(i)) as f:
        data = f.read().split()
        if(data.count('canada') != 0):
            canada_counter[i]=data.count('canada')
            file_length[i]=len(data)
    i+=1
    
#adding values to pretty tables: http://zetcode.com/python/prettytable/
tab1 = PrettyTable()
tab1.field_names = ["Canada appeared in %d documents"%len(canada_counter),"Total Words(m)","Frequency(f)"]
relative_frequency = {}
for i in canada_counter:
    tab1.add_row(["Article %d"%i,file_length.get(i),canada_counter.get(i)])
    relative_frequency[i]=round(canada_counter.get(i)/file_length.get(i),2)
#print(tab1)

#Convert Pretty Table to CSV : https://stackoverflow.com/questions/32128226/convert-python-pretty-table-to-csv-using-shell-or-batch-command-line
out_csv_list = []
table=tab1.get_string()
for row in table.splitlines():
    rowdata = row.split("|")
    if len(rowdata) == 1:
        continue  
    data_list = []
    for colmn in rowdata:
        colmn = colmn.strip()
        if colmn:
            data_list.append(colmn)
    out_csv_list.append(data_list)
with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\semantic B.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(out_csv_list)


max_rel_freq = max(relative_frequency,key=relative_frequency.get)
#adding values to pretty tables: http://zetcode.com/python/prettytable/
tab2= PrettyTable()
with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(max_rel_freq)) as f:
    art = f.read()
tab2.field_names=["Article File No.","Relative Frequency (f/m)","Article"]
tab2.add_row([max_rel_freq,relative_frequency[max_rel_freq],art])
#print(tab2)

#Convert Pretty Table to CSV : https://stackoverflow.com/questions/32128226/convert-python-pretty-table-to-csv-using-shell-or-batch-command-line
out_csv_list = []
table=tab2.get_string()
for row in table.splitlines():
    rowdata = row.split("|")
    if len(rowdata) == 1:
        continue  
    data_list = []
    for colmn in rowdata:
        colmn = colmn.strip()
        if colmn:
            data_list.append(colmn)
    out_csv_list.append(data_list)

with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\semantic C.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(out_csv_list)



