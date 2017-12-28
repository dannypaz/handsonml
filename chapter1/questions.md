* How would you define ML?
  * Programs learning from experiences and data
* Four types of problems where it shines?
  * Classification, predictions, speech recognition, helping humans learn
  * Problems which require a lot of hand tuning or long lists of conditionals, Complex problems with no good solution using traditional approach, Fluctuating environments with the need to adapt to new data, Getting insights with large amounts of data
* What is a labeled Training Set?
  * Already classified data, values and types
* What are two most common supervised tasks?
  * Classification and value predicition (predict a target numeric value)
* Name 4 common unsupervised tasks?
  * clustering, visualization, dimensionality reduction (simplify data without losing too much info), anomaly detection
* What type of algo would you use to allow a robot to walk in various unknown terrains
  * unsupervised, online-based
* what type of algo use to segment customers into multiple groups
  * clustering, unsupervised
* Would you frame the problem of spam detection as supervised or unsupervised?
  * supervised because we are classifying the emails as either Spam or Not Spam (HAM)
* What is an online learning system
  * A system that learns as it is being used. Continually learning, or incrementally learning
* What is out-of-core learning?
  * Loading part of the data and repeating processes until all data has been ran. This is a form of online learning
* What type of learning algo relies on a similarity measure to make predictions?
  * Model-based learning, generalizing a set of examples
* What is the difference between model parameter and hyperparameter
  * model parameter is for data, hyperparameter is for the algo
* What do model-based learn algorithms search for? what is the most common strategy they use, how do they make predictions?
  * making generalizations and finding trends in data. Modeling the data and then making a prediction based off of like models
* Name four main challenges of machine learning
  * Quantity of Data, Quality of Data, Overfitting, Underfitting
* If your model performs great on training data, but generalizes poorly to new instances, what is happening? can you name three possible solutions?
  * Overfitting the training data. Simplify your model, gather more training data, reduce noise in training data (remove outliers, fix data errors)
* What is a test set and why would you want to use it?
  * Test set of data (data taken when splitting into training set and test set). Allows you to figure out the generalization error by evaluating the model
* What is the purpose of a validation set?
  * A final test AFTER the test set.
* What can go wrong if you tune hyperparameters using the test set?
  * Hyperparameters would only produce the best model FOR THE TEST. Meaning that hyperparameters would be bad for any new data
* What is cross-validation and why would you prefer it to a validation set?
  * training multiple models with different chunks of the training set. This is preferred to avoid wasting data in validation sets
