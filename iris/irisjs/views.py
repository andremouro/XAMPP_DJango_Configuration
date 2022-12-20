# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, reverse
from irisjs.models import File
from django.views.generic import View
import pandas as pd
from plotly.offline import plot
import plotly.express as px



class HomeView(View):  # definimos a classe HomeView que será chamada dentro do urls.py
    def get(self, request, *args, **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o index.html (que está dentro de irisjs)
        data = File.objects.all()
        bar_chart = [
            {
                'Sp': x.species,
                'sp_length': x.sepal_length,
                'sp_width': x.sepal_width
            }for x in data
        ]
        df = pd.DataFrame(bar_chart)
        fig = px.bar(df.groupby(['Sp']).mean().reset_index(), x='Sp',y='sp_length',color='Sp')
        fig2 = px.scatter(df, x='sp_width',y='sp_length',color='Sp')

        bar_plot = plot(fig, output_type = 'div')
        scat_plot = plot(fig2, output_type='div')
        ctx = {'plot_div':bar_plot, 'plot_div2':scat_plot}

        return render(request, 'irisjs/index2.html', ctx)
