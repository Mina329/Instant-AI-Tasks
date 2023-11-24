# Session : 22/11/2023

## What is Regularization ?

Regularization is a technique used in machine learning to prevent overfitting and improve the generalization of a model. Overfitting occurs when a model performs well on the training data but fails to generalize to new, unseen data. Regularization introduces a penalty term to the model's loss function, discouraging it from fitting the training data too closely.

There are different types of regularization techniques, but two common ones are L1 regularization and L2 regularization:

1. L1 Regularization (Lasso): In L1 regularization, a penalty is applied to the absolute values of the coefficients of the model. It adds the sum of the absolute values of the coefficients multiplied by a regularization parameter to the loss function. L1 regularization tends to produce sparse models by driving some of the coefficients to exactly zero, effectively eliminating certain features.

2. L2 Regularization (Ridge): L2 regularization adds the sum of the squared values of the coefficients multiplied by a regularization parameter to the loss function. It penalizes large coefficients but does not usually lead to sparsity. L2 regularization is particularly effective when there is multicollinearity in the data (high correlation between independent variables).

The regularization parameter (often denoted as λ or alpha) controls the strength of the regularization effect. Higher values of the regularization parameter result in stronger regularization, which helps prevent overfitting but may lead to underfitting if set too high.

Regularization is a crucial tool in the machine learning toolbox, especially when dealing with complex models or datasets with a large number of features. It helps strike a balance between fitting the training data well and ensuring good generalization to new, unseen data.

## What is Overfitting ?

Overfitting is a common problem in machine learning where a model learns the training data too well, capturing noise and fluctuations in the data rather than just the underlying patterns. As a result, an overfitted model performs well on the training data but fails to generalize to new, unseen data. In essence, it has memorized the training data instead of learning the true relationships within the data.

Key characteristics of overfitting include:

1. High Training Accuracy, Low Test Accuracy: The model achieves high accuracy on the training dataset, but its performance on a separate test dataset is significantly lower.

2. Capturing Noise as Signal: Overfit models may capture random fluctuations or noise in the training data, treating them as if they are meaningful patterns.

3. Too Complex Model: Overfitting often occurs when the model is too complex relative to the simplicity of the underlying true pattern in the data. Complex models, such as those with many parameters or features, have a greater capacity to fit the training data precisely.

4. Limited Generalization: The overfitted model may struggle to generalize its findings to new, unseen data because it has essentially memorized the training data rather than learning the underlying relationships.
