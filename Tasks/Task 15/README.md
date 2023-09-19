# Session 15 : 10/9/2023

## What is the difference between covarience and correlation?

| Basis for Comparison | Covariance                                                                                                                                   | Correlation                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Definition           | Covariance is an indicator of the extent to which 2 random variables are dependent on each other. A higher number denotes higher dependency. | Correlation is a statistical measure that indicates how strongly two variables are related. |
| Values               | The value of covariance lies in the range of -∞ and +∞.                                                                                      | Correlation is limited to values between the range -1 and +1.                               |
| Change in scale      | Affects covariance                                                                                                                           | Does not affect the correlation                                                             |
| Unit-free measure    | No                                                                                                                                           | Yes                                                                                         |

## Examples on statistical test types

1. **T-Test**:
   - *Description*: The t-test is used to determine if there is a significant difference between the means of two groups. It is commonly employed when you have two sets of data and want to compare their means statistically.
   - *Scenario*: You want to know if there's a significant difference in the average commute times between two routes to work (Route A and Route B).

2. **Chi-Square Test**:
   - *Description*: The chi-square test is used to test the independence or association between two categorical variables. It is often used to analyze contingency tables and determine if there is a relationship between the variables.
   - *Scenario*: You're analyzing whether there's an association between gender (Male/Female) and job satisfaction (Satisfied/Dissatisfied) in a company.

3. **Analysis of Variance (ANOVA)**:
   - *Description*: ANOVA is used to compare the means of three or more groups to determine if there are statistically significant differences among them. It's an extension of the t-test for more than two groups.
   - *Scenario*: You're comparing the average test scores of students from three different schools (School A, School B, School C).

4. **Regression Analysis**:
   - *Description*: Regression analysis is used to model the relationship between a dependent variable and one or more independent variables. It helps predict outcomes based on input variables.
   - *Scenario*: You want to predict a person's monthly utility bill based on the number of household members and the average monthly temperature.

5. **Wilcoxon Rank-Sum Test**:
   - *Description*: The Wilcoxon rank-sum test, also known as the Mann-Whitney U test, is a non-parametric test used to compare two independent groups when the assumptions of the t-test are not met.
   - *Scenario*: You're comparing the exam scores of two groups of students, one who attended a prep course and another who didn't.

6. **Kruskal-Wallis Test**:
   - *Description*: The Kruskal-Wallis test is a non-parametric alternative to one-way ANOVA. It's used when you have three or more independent groups and want to compare their distributions.
   - *Scenario*: You're comparing the test scores of three different teaching methods (Method A, Method B, Method C) to see if they have different effects.

7. **Fisher's Exact Test**:
   - *Description*: Fisher's exact test is used to determine if there are nonrandom associations between two categorical variables in a 2x2 contingency table, especially when sample sizes are small.
   - *Scenario*: You're analyzing the effectiveness of a new drug treatment in a small clinical trial with only 10 patients.

8. **Pearson Correlation**:
   - *Description*: Pearson correlation measures the strength and direction of a linear relationship between two continuous variables. It provides a value between -1 and 1, indicating the degree of correlation.
   - *Scenario*: You want to understand if there's a linear relationship between the number of hours spent studying and the final exam scores of a group of students.

9. **Spearman Rank Correlation**:
   - *Description*: Spearman rank correlation is a non-parametric measure of the strength and direction of the monotonic relationship between two variables. It's used when data is ordinal or not normally distributed.
   - *Scenario*: You're exploring whether there's a monotonic relationship between the age of employees and their job performance ratings.

10. **Chi-Square Test for Homogeneity**:
    - *Description*: This test is used to determine whether different populations or groups have the same or different distributions of categorical variables. It assesses if the proportions are consistent across groups.
    - *Scenario*: You're comparing the distributions of political party preferences (Republican, Democrat, Independent) among three different cities.

## Types of data distributions with its track

- Normal Distribution : `natural and social sciences, finance, engineering, and quality control`
- Uniform Distribution : `probability theory and simulations`
- Exponential Distribution : `reliability engineering and queuing theory`
- Log-Normal Distribution : `finance for modeling asset prices and returns`
- Poisson Distribution : `epidemiology to model disease counts, in telecommunications for modeling call arrivals, and in quality control for modeling defect counts`
- Binomial Distribution : `hypothesis testing, quality control, and situations involving a fixed number of trials with binary outcomes`
- Skewed Distributions : `Left-skewed distributions are sometimes seen in financial data (e.g., stock returns) or income distributions.`
  `Right-skewed distributions are often found in income data, where a few individuals earn significantly more than the majority`
- Chi-Square Distribution : `statistical hypothesis testing, particularly for testing relationships and associations between categorical variables`
- F-Distribution : `statistical hypothesis testing for comparing variances or testing the equality of means between two or more groups`

## What is the difference between Naive bayes and conditional probability?

- Conditional probability P(A∣B) = P(A∩B) / P(B)
- Naive Bayes P(C∣X) = P(X∣C)∗P(C) / P(X)
  ​

​
