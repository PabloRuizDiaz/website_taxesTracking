from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from taxes.models import *
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
import os


@csrf_exempt
@require_http_methods(["GET", "POST"])
def form(request):
    if request.method == 'POST':
        data = taxesModel(
            tax=taxNameModel(int(request.POST.get('tax'))),
            money=request.POST.get('money'),
            pay_day=datetime.strptime(request.POST.get('pay_day'), '%Y-%m-%d'))

        data.save()

        return redirect(form)

    if request.method == 'GET':
        list_all_taxes = taxNameModel.objects.all()
        
        graph1()
        graph2()
        
        return render(request, 'main.html', {'list_all_taxes': list_all_taxes})



def graph1():
    list_all_taxes = taxNameModel.objects.all().values('category')
    df = pd.DataFrame(list_all_taxes)
    
    sns.histplot(x=df.iloc[:, 0], data=df,
                 discrete=True, shrink=.8, color='#2a9d8f')
    plt.title("Amount of taxes per category")

    BASE_DIR = Path(__file__).resolve().parent.parent
    pathfile = '{0}/static/img/graph1.png' .format(BASE_DIR)


    try:
        os.remove(pathfile)
    except:
        pass

    plt.savefig(pathfile)

    return


def graph2():
    list_all_taxes = taxesModel.objects.values_list('tax', 'money', 'pay_day')
    df = pd.DataFrame(list(list_all_taxes), columns=['tax', 'money', 'pay_day'])
    
    df['pay_day'] = pd.to_datetime(df['pay_day'], format='%Y-%m-%d')
    df['pay_month'] = pd.DatetimeIndex(df['pay_day']).month
    
    fig, ax = plt.subplots(figsize=(12, 10))
    fig = sns.barplot(x="pay_month", y="money", data=df,
                      estimator=sum, ci=None, ax=ax, color='#dda15e')
    plt.title('Acumulative payment of taxes per month')
    # x_dates = df['pay_month'].dt.strftime('%m').sort_values().unique()
    # ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')

    BASE_DIR = Path(__file__).resolve().parent.parent
    pathfile = '{0}/static/img/graph2.png' .format(BASE_DIR)

    try:
        os.remove(pathfile)
    except:
        pass
    
    plt.savefig(pathfile)

    return
