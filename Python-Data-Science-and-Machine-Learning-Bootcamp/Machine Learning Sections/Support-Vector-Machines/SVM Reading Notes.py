### Support Vector Machines ###
### Chapter 9 - ISLR ###
'''

Approach for classification made in the '90s
	perform well in various settings
	best "out of the box classifiers"

Generalizes #maximal margin classifier#
	
SVM can't be applied to most datasets
	it requires that the classes be separable by a linear boundary

People loosely call the #maximal margin classifier# #support vector classifier# and the #support vector machine# 
as #support vector machines#



'''
### 9.1 - Maximal Margin Classifier ###
'''
# Hyperplane #
	In p-dim space, a hyperplane is a subspace of p-1
	In 2-dim space, a hyperplane is a line
	In 3-dim space, a hyperplane is a plane
# Hyperplane Equation #
	In 2-dim - B0 + B1X1 + B2X2 = 0 (9.1)
		just eq of a line...
	In p-dim - B0 + B1X1 + B2X2 + ... + BpXp = 0 (9.2)
	
	Suppose X does not satisfy  (9.2) such that either:
		 (9.2) > 0 or  (9.2) < 0
		 This implies the point X lies on one side of the hyperplane or the other
	So a hyperplane divides p-dim space into 2 halves

### 9.1.2 - Classification using a Separating Hyperplane ###
Suppose it is possible to construct a hyperplane that perfectly separates the training
observations into their class labels
	If the EQ of the point evaluates to > 0, we assign y_i = 1
	If EQ < 0, we assign y_i = -1
		We are essentially finding a plane that perfectly divides the two classes
		"This ball is either purple, or yellow." - While there may be other colors like red or blue,
		The dividing plane forces these into either purple or yellow
	We let f(x*) be the EQ of the hyperplane
		If f(x*) is > 0 we assign x* to class 1
		If f(x*) is < 0 we assign x* to class -1
			The magnitude of f(x*) is the distance between the x* and the separating hyperplane
			The greater the magnitude the more sure we are of the classification

### 9.1.3 - The Maximal Margin Classifier ###
	If we can perfectly separate our data with a hyperplane, typically there exist
	and infinite number of similar hyperplanes that also separate it perfectly. 
		This is because we can shift the hyperplane by infinitely small decimals in any 
		direction. 
	# Maximal Margin Hyperplane # is the separating hyperplane that is farthest from the training observations
		The smallest distance from the hyperplane to the closest point is called the margin
	# Support Vectors # are the points closest to the Maximal Margin Hyperplane

### 9.1.3 - Construction of the Maximal Margin Classifier ###
	Now we consider constructing the maximal margin hyperplane based on a set of n training observations
	x_1, ...., x_n and class labels y_1, ..., y_n in {-1, 1}

	M denotes the margin of our hyperplane
	Finding the Maximum Margin Hyperplane is simply optimizing B_0, B_1, ..., B_p such that
	M is maximized
	
### 9.1.5 The Non-Separable Case ###
	Many times we cannot define a hyperplane that 100% divides the classes.
	In these cases, we allow for some error using a #soft-margin#
		The generalization of the maximal margin classifier to the non-separable case 
		is known as the #support vector classifier#
	
'''

### 9.2 - Support Vector Classifiers ###

'''
### 9.2.1 - Overview of SVC ###
	Finding a perfect separating hyperplane is a slippery slope to overfitting the training
	data. often we sacrifice preciseness for a larger margin
	
	The #soft margin classifier/support vector classifier# allows for error but maximizes 
	the accuracy of the model
	
	
### 9.2.2 Details of the Support Vector Classiﬁer ###
	


'''
### 9.3 - Support Vector Machines ###
'''
### 9.3.1 Classification with Non-Linear decision boundaries ###
	In the case where a linear hyperplane will do poorly, we can generalize the EQ 
	to quadratic, cubic, etc.
		B_0 + B_1*X_1 + B_1*(X_1)^2 + B_2*(X_2) + B_2*(X_2)^2,...,+ B_p*(X_p) + B_p*(X_p)^2

### 9.3.2 The Support Vector Machine (SVM) ###
	SVM is an extension of the SVC that results from enlarging the feature space in a specific way using #kernels#
	We do so to accommodate a non-linear boundary between classes.
		The kernel approach is simply an efficient computational approach
		A kernel (K) is a function that quantifies the similarity of two observations
		an example could be:
			K(x_i, x_i`) = SUM(j=1, p, x_ij * x_i`j) (9.21)
			this returns the support vector classifier
			(9.21) is called linear kernel bc the support vector classifier is linear
			in the features. The linear kernel essentially quantifies the similarity of a pair of observations
			using Pearson (standard) correlation. 
			
		We could choose another form of kernel such as:
			K(x_i, x_i`)	= (1 + SUM(j=1, p, x_ij * x_i`j)^d where d is a positive int
			This is known as a polynomial kernal of degree d. Using a kernel such that 
			d>1 instead of a linear kernel leads to a flexible decision boundary. When
			the support vector classifier is combined with a non-linear kernel, the 
			resulting classifier is known as a #support vector machine#
	
	Another popular choice is the radial kernel:
		K(x_i, x_i`) = 1^(-g * SUM(j=1,p, (x_ij * x_i`j)^2)
		
'''
### 9.4 - SVMs with More than 2 classes ###
'''
There are no true ways to extend SVMs to more than two classes.
However there are 2 proposed solutions, 1v1 and 1vAll

### 9.4.1 - One Versus One ###
### 9.4.2 - One Versus All ###


'''

### 9.5 - Relationship to Logistic Regression ###
'''
SVMs are very similar to Logistic Regression functions
When classes are well separated, SVMs shine, in other scenarios, Logistic Regression shines

There is an extension for SVMs to allow for quantitative response called #support vector regression#



'''
























