from sklearn import tree #decision tree flow point
#[height, weight, shoe size]
x = [[5.6,120,5],[5.9,160,7],[6.9,190,12],[5.3,132,8],[5.9,123,9],[5.6,120,5],[5.9,160,7],[6.9,190,12],[5.3,132,8],[5.9,123,9]]

y = ['male','female', 'male','female','male','female','male','female','male','female',]

classifier= tree.DecisionTreeClassifier()

clf=classifier.fit(x,y)

prediction = clf.predict([5.6,120,5])
