from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import pickle


def home(request):
    return render(request,"home.html")

def result(request):
    
    cls = pickle.load(open('randomforest.pkl','rb'))
    
    lis = []
    txt=request.GET['text']
    txt=pd.Series(txt)
    ans=cls.predict(txt)
    
    print(ans)
    
    if ans == 1:
        ans="SQl Injection Attack"
    else:
        ans="Not SQL Injection Attack"
    return render(request,"result.html",{'ans':ans})