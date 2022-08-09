## Sales Prediction with Multiple Linear Regression

The [dataset](https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv) given here contains the data about the sales of the product. The dataset is about the advertising cost incurred by the business on various advertising platforms.

    1. TV: Advertising cost spent in dollars for advertising on TV;
    2. Radio: Advertising cost spent in dollars for advertising on Radio;
    3. Newspaper: Advertising cost spent in dollars for advertising on Newspaper;
    4. Sales: Number of units sold;

So, the objective is to predict the sales of product and find the most impact features.


### [Multiple Linear Regression equation.](https://en.wikipedia.org/wiki/Linear_regression)

$$
y = \alpha + \beta_{0} x_{0} + \beta_{1} x_{1} + ... + \beta_{n} x_{n}
$$


### Evaluate the regression model with [R-Squared](https://en.wikipedia.org/wiki/Coefficient_of_determination)

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}\ \\
$$
with,
$$
\\ SS_{res} = \sum \limits _{i=1} ^{n} (y_{i} - f(x_{i}))^2
\\ SS_{tot} = \sum \limits _{i=1} ^{n} (y_{i} - \bar{y})^2
$$