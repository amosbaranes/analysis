from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings


def index(request):
    title = 'Finance App'
    s_file_name = settings.EXCEL_DIR + 'all_securities.xlsx'
    df = pd.read_excel(s_file_name, sheet_name="data", header=0)  # , index_col=
    print(df.head())
    print(df.columns)
    return render(request, 'finance/index.html', {'title': title})
