#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_csv('eda.csv')


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


data_model=data[['Job Title', 'Salary Estimate', 'Job Description', 'Rating',
       'Company Name', 'Location', 'Headquarters', 'Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'Competitors',
       'hourly', 'employer_provided', 'min_salary', 'max_salary', 'avg_salary',
       'job_state', 'company_txt', 'same_state', 'age', 'python_yn', 'R_yn',
       'spark', 'aws', 'excel', 'job_simp', 'seniority', 'desc_len',
       'num_comp']]


# In[6]:


data_dum=pd.get_dummies(data_model)


# In[7]:


data_dum


# In[8]:


from sklearn.model_selection import train_test_split


# In[9]:


X=data_dum.drop('avg_salary',axis=1)


# In[10]:


Y=data_dum['avg_salary'].values


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


# In[12]:


import statsmodels.api as sm


# In[13]:


X_sm=sm.add_constant(X)


# In[14]:


model=sm.OLS(Y,X_sm)


# In[15]:


model.fit().summary()


# In[16]:


from sklearn.linear_model import LinearRegression,Lasso


# In[17]:


from sklearn.model_selection import cross_val_score


# In[18]:


lm = LinearRegression()
lm.fit(X_train, y_train)


# In[19]:


import numpy as np
np.mean(cross_val_score(lm,X_train,y_train,scoring='neg_mean_absolute_error',cv=3))


# In[20]:


lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))


# In[21]:


alpha=[]
error=[]


# In[22]:


for i in range(1,100):
    alpha.append(i/100)
    lml=Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))


# In[23]:


import matplotlib.pyplot as plt
plt.plot(alpha,error)


# In[24]:


err=tuple(zip(alpha,error))


# In[25]:


data_err=pd.DataFrame(err,columns=['alpha','error'])


# In[26]:


data_err[data_err.error == max(data_err.error)]


# In[27]:


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()


# In[28]:


np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))


# In[ ]:





# In[29]:


from sklearn.model_selection import GridSearchCV
# parameters = {'n_estimators':range(10,300,10)}
parameters = {'n_estimators':range(10,300,10)}


# In[30]:


gs = GridSearchCV(rf,parameters)


# In[31]:


gs.fit(X_train,y_train)


# In[32]:


gs.best_score_



# In[33]:


gs.best_estimator_


# In[34]:


tpred_lm = lm.predict(X_test)


# In[ ]:


tpred_lml = lm_l.predict(X_test)


# In[ ]:


tpred_rf = gs.best_estimator_.predict(X_test)


# In[ ]:


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)


# In[ ]:


mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)


# In[ ]:


import pickle


# In[ ]:


pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(np.array(list(X_test.iloc[1,:])).reshape(1,-1))[0]

list(X_test.iloc[1,:])


# In[ ]:




