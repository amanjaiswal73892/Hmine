
# Import necessary pyhton modules
import itertools
import math
import csv
import sys
#import os
#import psutil



#This function is used to run the algorithm from interactive python.
# It is also used in our comparison script.
def runApriori(input_file, output_file, min_support):

    if min_support <= 0: #checking for valid value of min_support
        sys.exit("Min_support cannot be less than or equal to 0")

    print("Data Mininging Begins using Apriori algorithm...")

# The input file passed to this algorithm is read under the assumption that every item is separated by " ".
    with open(input_file,'r',encoding='utf-8-sig') as input:
        reader_obj = csv.reader(input, delimiter=" ")
        datalist=[];
        for line in reader_obj:
            datalist.append(line[:-1])

# The minimum support is calculated using the ceil function. 
# min_support which is passed to this algorithm is in precentage(%). This is converted to number of transactions.
    min_sup = math.ceil(min_support * len(datalist))
    out_frequents_items = []                #Frequent Items generated by Apriori are appended one by one to this list

    #This function creates output_file when program is run for first time. 
    #Later this is used to truncate the data so that fresh results can be stored in output file
    def empty_file():   
        with open(output_file, 'w') as f_output:
            f_output.close()
        file = open(output_file,"r+")
        file.truncate(0)
        file.close()

    #This function is used to write the data into output_file
    def write_into_file(string):
        with open(output_file, 'a') as f_output:
            f_output.write(string+"\n")
            f_output.close()

    # This function returns the subsets of a input set
    def findsubsets(s, n): 
        return list(itertools.combinations(s, n))

    # This function returns a join of two input sets a,b if thier first (k-2) elements are matching. If not this returns none
    def new_join(a,b,k):
        if k<3:
            return a.union(b)
        a1=list(a);b1=list(b)
        a1.sort()
        b1.sort()
        if a1[:k-2]==b1[:k-2]:
            return a.union(b)

    # This function is used to generate L1 which is list of 1-frequent itemsets.
    def get_l1(datalist):
        d={};
        for row in datalist:
            for item in row:
                if item not in d.keys() :
                    d[item]=1
                else:
                    d[item]+=1
        # This loop is used to write 1-frequent itemsets into the output list(out_frequents_items)            
        for x in d.keys():
            if d[x] >= min_sup:
                out_frequents_items.append(f'{x} #Supp: {d[x]}') 

        return [set([x]) for x in d.keys() if d[x] >= min_sup] # ouputs a list of 1-sets with the having minimum_supp

    # Apriori_gen function is used to generate candidate itemset C(k) from l(k-1) previous-itemsets.
    def apriori_gen(lk,k): 
        c=[]
        for n1 in range(len(lk)):
                for n2 in range(n1+1,len(lk)):
        # join L(k) with L(k) if their first(k-2) items are in common
                    join=new_join(lk[n1],lk[n2],k)
            # checks if join of two sets is not null
                    if join is not None:
                    # This step checks if subsets of each 'join' is present in l(k-1) set
                        if not has_infrequent_subset(join,lk):
                             c.append(join)
        return c


    # The function will check if any (k-1) subset of a set is not present in l(k-1)
    #pass a set and l(k-1) list , 
    def has_infrequent_subset(c,l):
        subset_len=len(c)-1
        subsets=findsubsets(c,subset_len)
        for s in subsets:
            if set(s) not in l:
                return True
        return False

    def subsets_of_row_present_in_ck (ck,row,k):
        subsets=findsubsets(row,k) #list of tuples of subsets of size k 
        # get the subsets of t that are candidates
        ck_frozen=set(frozenset(x) for x in ck)
        subsets_frozen=set(frozenset(x) for x in subsets)
        return ck_frozen.intersection(subsets_frozen)

    # iterative apriori implementation
    #initialising k=2
    k=2
    #initialising L(k) = L(1)
    lk=get_l1(datalist)
    frequent_itemsets=[]
    frequent_itemsets.append(lk)
    while lk: # while lk is not empty
    # generate C(K) candidates with L(K-1)
        ck=apriori_gen(lk,k)
        # using a another list to store the support count
        ck_count=[[x,0] for x in ck]
        for row in datalist:
            # putting each row in a set
            rowset=set(row)
            # get the subsets of row that are candidates
            ct=subsets_of_row_present_in_ck(ck,rowset,k)
    #         print(ck_count)
            for candidate in ct:
                for count in ck_count:
                    if(candidate in count):
                        count[1]=count[1]+1;

        #filtering C(k) if c in ck_count > min_sup
        lk=[x[0] for x in ck_count if x[1]>=min_sup]

        for x in ck_count:
            if x[1] >= min_sup:
                temp=""
                # This is used append the k-level frequent items into output list (out_frequents_items)
                for item in (x[0]):
                    temp += f'{item},'
                out_frequents_items.append(f'{temp[:-1]} #Supp: {x[1]}')

        # Append to frequent_itenset if lk in not empty
        if lk:
            frequent_itemsets.append(lk)

        #incrementing k 
        k+=1; 

    itemset_count = sum([len(x) for x in frequent_itemsets])  #Total number of frequent_items for given input_file dataset

    
    # Below code is used to truncate the output file and write the Frequent_itemsets generated into the output file
    empty_file()
    write_into_file(f'Input DataSet used is : {input_file}')
    write_into_file(f'output_file is : {output_file}')
    write_into_file(f'min_sup used by algorithm is : {min_sup}\n')
    write_into_file(f'Frequent_Itemsets, Support')
    [write_into_file(out) for out in out_frequents_items]
    write_into_file(f'\nTotal Frequent Itemset Count = {itemset_count}')

    print(f'Data Mining completed using Apriori algorithm for "{input_file}" dataset\nFrequent Itemsets stored in "{output_file}"')
    print("End of Program")

  #Below Code returns the memory usage of this algorithm. This section was used to generate metrics used for experimental analysys.
    # processid = os.getpid()
    # process = psutil.Process(processid)
    # memoryUse = process.memory_info()
    # return memoryUse.rss