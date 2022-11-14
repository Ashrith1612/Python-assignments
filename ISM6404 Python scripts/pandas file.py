def average_all_elements(some_list):
    the_sum = 0
    num_of_elements = 0
    for i in some list:
        the_sum +=1
        num_of_elements +=1
   averege = the_sum/num_of_elements
        return average
    
    mport pandas

    myCsvFile = pandas.read_csv("WeightHeightAgeDataWithFieldNamesInFirstRow.csv")

    print (myCsvFile)

    lst_weights = []

    for i in myCsvFile["Weight"]:
        lst_weights.append(i)
        
    print(lst_weights)

    lst_heights = ["]

    for i in myCsvFile["Height"]:
        lst_heights.append(i)
    print(lst_heights)
        
        lst_age = ["]

        for i in myCsvFile["Age"]:
            lst_age.append(i)

    print(lst_age)
    
    print ("The average height =", avg_of_all_elements(lst_heights))
    print ("The average weight =", avg_of_all_elements(lst_weights))
    print ("The average age =", avg_of_all_elements(lst_age) )