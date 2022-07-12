#!/usr/bin/env python
# coding: utf-8

# In[44]:


from flask import Flask, request, render_template


# In[45]:


import joblib


# In[46]:


app = Flask(__name__)


# In[47]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("Regression")
        pred1 = model1.predict([[rates]])
        model2 = joblib.load("DecisionTree")
        pred2 = model2.predict([[rates]])
        return(render_template("index.html", result1=pred1, result2=pred2))
    else:
        return(render_template("index.html", result1="Waiting", result2="Waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




