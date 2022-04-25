from celery import current_task, Celery
from config import app
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os


#celery task created 
def make_celery(app):
    celery = Celery(
        app.name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
   

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

@celery.task(name="tasks.Create_Chart")
def Create_Chart(rdata,charttitle,xtitile):
    df = pd.DataFrame(rdata)
    layout = go.Layout(title = charttitle,xaxis = dict(title = xtitile,tickangle= 40))
    fig = go.Figure(layout=layout)

    for i in range(1,len(df.columns)):
        fig.add_trace(go.Bar(x=df[df.columns[0]],y=df[df.columns[i]],name=df.columns[i]))
        
    fig.update_layout(barmode='group')
    fig.write_image(os.path.join(app.config['IMAGES_FOLDER'],current_task.request.id + ".png"))   
    return current_task.request.id + ".png"


@celery.task(name="tasks.Create_School_Chart")
def Create_School_Chart(rdata,charttitle):
    df = pd.DataFrame(rdata)
    fig = px.pie(df, values=df.columns[1], names=df.columns[0],title=charttitle)
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.write_image(os.path.join(app.config['IMAGES_FOLDER'],current_task.request.id + ".png"))   
    return current_task.request.id + ".png"