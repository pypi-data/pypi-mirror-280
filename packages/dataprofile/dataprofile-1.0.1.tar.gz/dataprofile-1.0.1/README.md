DataProfile Library
 
Description: the principal fuction of this library is create a data base profile fast view. For this recorre a dataframe in order to analyze diferentes relevants features for each column. 

The princial features are:
                           Count: count the number of records. Return a numeric

                           Count distinct: count the number of distincs recors. Return a numeric.

                           Unique: count the unique records. Return a numeric.

                           Id probability: calculate a probability that the column be a id. For that evaluate the data type, the name of the column, the number of unique ids, the amoun of empty and null records. And with all this information estimate a probability. Return a percent.

                           Email probability: Find the probability that the column contains emails. To do this, count the number of @ and valid domains, then estimate a probbility. Return a percent.

                           Duplicate: Count the duplicate recors per column. Return a numeric. Return a numeric.

                           Numeric: Define whether the data type is numeric. Returns a "True" only if all records in the column are numeric.

                           Letter: Define whether the data type is string. Returns a "True" only if all records in the column are string.

                           Bool: Define whether the data type is bool. Returns a "True" only if all records in the column are bool.

                           Empty: Count the number of empty records per column. Return a numeric.

                           Cero: Count the number of ceros per column. Return a numeric.

                           Null: Count the number of null records per column. Return a numeric.

Install Requires:
               Pandas
               Numpy
               Prettytable
        
Fuctions:
         dataprofile(DF): this is the main function. takes as input a DataFrame and returns another one with all the features described above.


Example:

1) The first step is install the library using pip instal dataprofile:
![alt text](image-2.png)

2) The second step is import the dataprofile librari: import dataprofile as dp.
![alt text](image-3.png)

3) The therd step is creat or importa a Dataframe. In this case use read_csv from Pandas for import a csv and creat a DataFrame.
![alt text](image-1.png)

4) The fored step is use the fuction dataprofile on a Dataframe on this way dp.dataprofile(DataFrame)
![alt text](image.png)
