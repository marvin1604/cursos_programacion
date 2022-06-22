#import function reduce of the module fuctools
from functools import reduce
def run():

    #usign the function filter
    my_list2 = [1,4,5,6,9,13,19,21]

    odd2 = list(filter(lambda x: x%2 != 0, my_list2))
    print("filter:", odd2)


    #using the function map
    my_list= [1,2,3,4,5]
    # odd=[i*i for i in list]
    # print(odd)    
    odd = list(map(lambda i: i**2, my_list))
    print("map: ", odd)
    
    #using the function reduce
    my_list3= [2,2,2,2,2]
    all_multiplied=reduce(lambda a, b: a * b, my_list3)
    print("reduce: ", all_multiplied)



if __name__ == "__main__":
    run()