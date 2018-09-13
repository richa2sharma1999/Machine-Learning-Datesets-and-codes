



my_feature_columns=[]
for Key in train_x.keys():
	my_feature_columns.append(tf.feature_columns.numeric_column(Key=Keys))
classifier=tf.estimator.DNNClassifier(feature_columns)