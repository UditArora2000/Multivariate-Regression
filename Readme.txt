REPORT
Description of the Problem
The question I have attempted is Q2. Unlike the problem in the previous assignment where we were asked to find the error in the impact factor calculated for testing data using the regression line having only one variable (HI index), this time we need to include other variables which affect impact factor. Apparently we have to take all possible combinations of the variables in order to determine the case for which the regression line is most accurate that is the error in impact factor calculated for the testing data is minimum. Since now we have 9 possible inputs on which the impact factor can depend on we need to consider (2^9 - 1 = 511) cases (-1 because we need to remove the case where impact factor depends on none of the inputs). Now we also need to select the training data from which the multi variable regression line will be predicted. Since we have 600 data and we need to select 80% that is 480 data for training we have 600C480 possible ways to select the training data. But that number is very large and calculating error for all possibilities would take 600C480 x 511 order of computations which could take years to find. So we have to limit the number of possibilities. I have taken only 10 cases (I tried 400 cases and it took more than 1 hour to find the minimum error). 

Scripts Submitted:
1. ‘creating found from journals.py’ – This is for the purpose of accumulating all the 9 inputs from the ‘journals.csv’ file and the expected impact factors from the ‘journals.txt’ file into a single file by the name of ‘found.txt’.
2. ‘Maths.py’ – This is for the purpose of calculating the minimum error for the data in ‘found.txt’ and finding the regression line for which the error is minimum. 

Output:
Minimum Mean square error: 0.622439386345022 
Corresponding Mean absolute error: 0.0037017629150346994

The inputs that lead to minimum error would be:
1. SJR
2. Total Docs. (3 years)
3. Total Cities (3 years)
4. Citable Docs. (3 years)
For regression line and list of index of data such that first 480 are used to train and the remaining 120 are used to test see the ‘output.py’ file.


