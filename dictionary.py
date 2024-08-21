# TODO new_dict = {new_key:new_value for (key, value) in dict.items() if test}
from pandas.io.sas.sas_constants import column_format_text_subheader_index_length

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence = sentence.replace("?", "")
# each_word = list(sentence.split(" "))
#
# result ={value: len(value) for value in each_word}

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {key:round((value * (9/5) + 32),1 ) for (key,value) in weather_c.items()}
#
# print(weather_f)



student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# # TODO Looping through dict
#
# for (key, value) in student_dict.items():
    # print(value)
    # print(key)

# TODO Iterare over Pandas DF

import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)

#Loop through rows of a df
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)