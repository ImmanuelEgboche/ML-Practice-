# Understand Linear Regression

Linear regression is a statiscal method used to model relationships between a dependeatn variable and a independent variable (or more than one). The aim is to find a relationship that best fits the data

### Simple Linear Regression 

In simple linear regression, models the relationship between two variables. The equation is:

$$y = mx + b$$

- Dependent Variable (y): The variable we are trying to predict. In simple linear regression, y is modeled as a function of a single independent variable.

- Independent Variable (x): The predictor variable used to predict y. It is assumed to be related to the dependent variable linearly.

- Slope (m): Represents the rate of change of the dependent variable (y) with respect to the independent variable (x). It tells us how much y will change for each unit increase in x.

- Y-Intercept (b): This is the value of y when x is zero. It represents the point where the line crosses the y-axis in a graph of the relationship.


### Multiple Linear Regression

In multiple linear regression this is extended to multiple independent variables:

$$
y = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n
$$

- Dependent Variable (y): This is the variable that we are trying to predict or explain. It depends on the independent variables.

- Independent Variables (x₁, x₂, ..., xₙ): These are the variables that provide the input or the factors that is used to predict the dependent variable. Each x represents a different independent variable.

- Coefficients (b₀, b₁, b₂, ..., bₙ): b₀ is the y-intercept, which is the predicted value of y when all the independent variables are equal to zero. The other coefficients (b₁, b₂, ..., bₙ) represent the effect of each independent variable on the dependent variable. They say yu how much y changes for a unit change in each x.

## Mean Squared error 

Mean Squared error (MSE) is used to measyre the average squared difference between estimated values(in this case predictions) and the actual value. In the context of regression analysis, its a way to measure the error of a model in predicting quantitative data 

### Formula 

The MSE is calculated as the average of the squares of the errors, the average squared difference between the estimated values and the actual value. Represented as: 

MSE = $\frac{1}{n}$ $\sum_{i=1}^{n}$ ($y_i$ - $\hat{y}_i$)$^2$

- `n` is the number of observations.
- `Y_i` is the actual value of an observation.
- `Ŷ_i` (or `Y_hat_i`) is the predicted value for that observation.

### Importance of MSE 

- MSE shows error magnitude which helps to quantify the magnitude of the error in predicition models. it squares the errors, which has the effect of heavily penalizing larger errors. This can be particually usefulw hen large errors are more undesirable than smaller ones.

- The squaring of errors makes MSE continously differentiable, which is benficial for optimization algorithms that rely on derivatives, such as gradient descent

- By squaring the errors, MSE puts the errors in the same units as the square of the output variable. This is usefulf for comparison across datasets or models

- MSE also provides a way to measure the performance of difference predictive models on the same dataset

### Limitations 

- Due to the squaring of each term, MSE can be sensitivte to outliers. Large deviations are given disproportinately large weights, which can skew the results if data containers outliers

- The value of MSE is scale-dependent, whihc means it can vary significantly across datasets with different scales. Which can make it challenging to compare across datasets 

### 

- You would want the MSE to be as small as possible compared to the variance. A standard measure for this is the coefficient of determination, also known as "R squared":
    𝑅2=1−𝑀𝑆𝐸𝑣𝑎𝑟(𝑌).



## Practice 

We have a dataset of house prices where we want to predict the price of a house based on its size (in square feet).

| Size (sq ft) | Price ($) |
|--------------|-----------|
| 600          | 300,000   |  
| 800          | 350,000   |
| 1000         | 400,000   |
| 1200         | 450,000   |
| 1400         | 500,000   |


Find a linear relationship between the Size and the Price. Then use it to predict the price of a house with a size of 1100 sq ft and 1500 sq ft


