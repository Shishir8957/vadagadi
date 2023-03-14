import difflib
import pandas as pd
import os


cwd= os.getcwd()


bike_data= pd.read_csv(f"{cwd}\\products\\vehiclesdata.csv")
similarity= pd.read_pickle(f'{cwd}\\products\\similarity.pkl')
list_of_all_name = bike_data['name'].tolist()


def get_recommendation(name):
    find_close_match = difflib.get_close_matches(name,list_of_all_name)

    close_match = find_close_match[0]

    name_of_the_bike = bike_data[bike_data.name == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[name_of_the_bike]))

    sorted_similar_bike = sorted(similarity_score,key = lambda x:x[1],reverse = True)

    print('bike suggested for you: \n')
    i=1
    suggestions=[]
    for bike in sorted_similar_bike:
        index = bike[0]
        name_from_index = bike_data[bike_data.index == index]['name'].values[0]
        index= bike_data[bike_data.index == index]['index'].values[0]
        if(i<11):
            #index_of_the_bike = bike_data[bike_data.name == close_match]['index'].values[0]
            suggestions.append((name_from_index,index))
            i+=1
    return suggestions

