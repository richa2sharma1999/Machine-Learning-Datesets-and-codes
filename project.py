
import json
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets
import sklearn
import numpy as np
import sklearn.linear_model
import sklearn.ensemble

file = open('C:\\Users\\BADMAN\\Desktop\\files_ml\\pizza_act\\train.json')
data = json.loads(file.read())
data = json.dumps(data,indent = 2)
data = pd.read_json(data)


x = data.drop(['giver_username_if_known', 'requester_upvotes_minus_downvotes_at_request','requester_upvotes_plus_downvotes_at_request','requester_user_flair','requester_number_of_posts_at_request','requester_number_of_posts_on_raop_at_request','requester_number_of_comments_at_request','requester_days_since_first_post_on_raop_at_request','requester_received_pizza','requester_subreddits_at_request','requester_user_flair','requester_username','unix_timestamp_of_request','requester_number_of_comments_in_raop_at_request','unix_timestamp_of_request_utc','number_of_downvotes_of_request_at_retrieval','number_of_upvotes_of_request_at_retrieval','post_was_edited','request_id','request_text','request_text_edit_aware','requester_account_age_in_days_at_request','request_title'],axis=1)
y = data['requester_received_pizza']
x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.2)

clf_gini = sklearn.tree.DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=3,min_samples_leaf=5)
clf_gini.fit(x_train,y_train)
print("Using Decision Tree:"+str(clf_gini.score(x_test,y_test)))

clf = sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print('Using Random Forest:'+str(clf.score(x_test,y_test)))

reg = sklearn.linear_model.LogisticRegression()
reg.fit(x_train,y_train)
print("Using Logistic Regression:"+str(reg.score(x_test,y_test)))

model = sklearn.svm.SVC()
model.fit(x_train,y_train)
print("Using Support Vector Machine:"+str(model.score(x_test,y_test)))

reg = sklearn.linear_model.LinearRegression()
reg.fit(x_train,y_train)
print("Using LinearRegression:"+str(reg.score(x_test,y_test)))