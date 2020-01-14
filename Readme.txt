REPORT
Description of the Problem
We will take all possible combinations of the variables in order to determine the case for which the regression line is most accurate that is the error in impact factor calculated for the testing data is minimum. Since now we have 9 possible inputs on which the impact factor can depend on we need to consider (2^9 - 1 = 511) cases (-1 because we need to remove the case where impact factor depends on none of the inputs). Now we also need to select the training data from which the multi variable regression line will be predicted. Since we have 600 data rows and we need to select 80% that is 480 data rows for training.

Scripts:
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



