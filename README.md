# dabp_final_proj
## Distance finder python (distance_finder.py)
We first have to create use the distance finder file. The breakdown of the code is as follows:
1. We are trying to find distance between all possible school and hospital combinations, by scraping it from mapquest. We do this by first getting all the addresses for schools and hospitals and putting together all the combinations. The start for each address is a school and end point is a hospital. The outcome is a matrix of size 32 X 47. 
## Program Code (dabp_final_code.py)
1. We first import all the data set, (schools,school population, hospitals, distances), create a list for the number of hospital beds. School populations are five different csv's having the number of infected students for each scenario and for each school.The name of the files are in this format(school_population_infectionrate). 
2. We then add all our constraints, create our two objective functions and then run it for each infection rate.
3. After running the objective function, we then extract the total miles travelled by each student for each models.The output is a csv. We then used this csv to create graphs in excel.
