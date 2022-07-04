
from csv import DictWriter
import os
import pandas as pd

def result_dataframe(epochs,precision,recall,map_5,map_95,weights,time_taken,batch_size, gpu_memory):
    # list of column names
    
    data_path = os.getcwd()
    print(data_path)
    if os.path.exists(data_path+'/benchmark_result.csv'):

        field_names = ['batch_size','epochs','GPU Memory','precision','recall',
                    'map_5','map_95','weights', 'Time taken']

        new_row={'batch_size':batch_size,'epochs':epochs, 'GPU Memory': gpu_memory,'precision':precision,'recall':recall,
                    'map_5':map_5,'map_95':map_95,'weights':weights, 'Time taken': time_taken}

        # Open your CSV file in append mode
        # Create a file object for this file
        with open(data_path+'/benchmark_result.csv', 'a') as f_object:
            
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)

            #Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(new_row)

            #Close the file object
            f_object.close()
    
    else:
        result_dataframe = pd.DataFrame({"batch_size":batch_size,"epochs": [epochs],"GPU Memory":[gpu_memory],"precision":[precision], "recall": [recall] ,"map_5": [map_5], "map_95": [map_95],
                                     "weights":[weights], "Time taken":time_taken })
        result_dataframe.to_csv(data_path+'/benchmark_result.csv', index=False)




def time_taken(total_time,batch_size=None,epochs=None,precision=None,recall=None,map_5=None,map_95=None,weights=None):
    data_path = os.getcwd()
    if os.path.exists(data_path+'/benchmark_result.csv'):

        field_names = ['batch_size','epochs','precision','recall',
                    'map_5','map_95','weights', 'Time taken']

        new_row={'batch_size':batch_size,'epochs':epochs,'precision':precision,'recall':recall,
                    'map_5':map_5,'map_95':map_95,'weights':weights, 'Time taken': total_time}


        # Open your CSV file in append mode
        # Create a file object for this file
        with open(data_path+'/benchmark_result.csv', 'a') as f_object:
            
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)

            #Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(new_row)

            #Close the file object
            f_object.close()







