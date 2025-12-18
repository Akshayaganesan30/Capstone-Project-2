#!/usr/bin/env python
# coding: utf-8

# In[301]:


import pandas as pd
from sqlalchemy import *
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[8]:


username = "root"
password = "Pgnkka#"
host = "localhost"
port = 3306
database = "obesity_malnutrition"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

plt.style.use('dark_background')


sel_qry = "SELECT * FROM obesity"
df_obe = pd.read_sql(sql=sel_qry,con=engine)


sel_qry1 = "SELECT * FROM malnutrition"
df_mal = pd.read_sql(sel_qry1,con=engine)


# ### Line chart: Global obesity & malnutrition trends

def chrt1():
    fig,ax = plt.subplots()
    ax.plot(df_obe.groupby("Year")['Mean_Estimate'].mean(),label="Obesity Trend",marker="o")
    ax.plot(df_mal.groupby("Year")['Mean_Estimate'].mean(),label="Malnutrition Trend",marker="o")
    ax.set_xlabel("Year")
    ax.set_xticks(df_obe['Year'].value_counts().sort_index().index)
    ax.tick_params("x", rotation=45)
    ax.set_ylabel("Average Level")
    ax.set_title("Global Obesity and Malnutrition Trend")
    ax.legend()
    return fig

def chrt2():
    df_bar_ob = pd.DataFrame(df_obe.groupby(['Country'])['Mean_Estimate'].mean().sort_values(ascending=False)[0:9])
    df_bar_ml = pd.DataFrame(df_mal.groupby(['Country'])['Mean_Estimate'].mean().sort_values(ascending=False)[0:9])
    fig,ax = plt.subplots()
    ax.bar(df_bar_ob.index,df_bar_ob['Mean_Estimate'],label='Obesity')
    ax.set_xlabel("Country")
    ax.tick_params("x", rotation=90)
    ax.set_ylabel("Avergae Obesity Level")
    ax.bar(df_bar_ml.index,df_bar_ml['Mean_Estimate'],label='Malnutrition')
    ax.set_xlabel("Country")
    ax.tick_params("x", rotation=90)
    ax.set_ylabel("Avergae Malnutrition Level")
    ax.legend()
    return fig

def chrt3():
    fig,ax = plt.subplots()
    #df_obe.boxplot("Mean_Estimate",by="Region",rot=45,figsize=(10,8))
    sns.boxplot(x="Region", y="Mean_Estimate", data=df_obe, ax=ax)
    ax.tick_params("x", rotation=90)
    ax.set_title("Box plot for Obesity")
    return fig

def chrt4():
    fig,ax = plt.subplots()
    #df_obe.boxplot("Mean_Estimate",by="Region",rot=45,figsize=(10,8))
    sns.boxplot(x="Region", y="Mean_Estimate", data=df_mal, ax=ax)
    ax.tick_params("x", rotation=90)
    ax.set_title("Box plot for Malnutrition")
    return fig

def chrt5():
    fig,ax = plt.subplots()
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='CI_width', y='Mean_Estimate', data=df_obe,
               hue='Obesity_Level', style='Obesity_Level', palette='Set1', edgecolor='black',ax=ax)
    ax.set_title("Patterns in Obesity Data")
    return fig

def chrt6():
    fig,ax = plt.subplots()
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='CI_width', y='Mean_Estimate', data=df_mal,
               hue='Malnutrition_Level', style='Malnutrition_Level', palette='Set1', edgecolor='black',ax=ax)
    ax.set_title("Patterns in Malnutrition Data")
    return fig

def chrt7():
    fig,ax = plt.subplots()
    plt.figure(figsize=(12, 4))  # length breadth
    sns.histplot(data=df_obe, x='Mean_Estimate',
                 bins=20, 
                 color='b', 
                 edgecolor='black', 
                 label='Obesity',ax=ax)
    sns.histplot(data=df_mal, x='Mean_Estimate',
                 bins=20, 
                 color='g', 
                 edgecolor='black', 
                 label='Malnutrition',ax=ax)
    ax.legend()
    ax.set_title('Distribution of obesity and Malnutrition')
    return fig

def chrt8():
    df_bars_ob = pd.DataFrame(df_obe.groupby(['Gender'])['Mean_Estimate'].mean())
    df_bars_ml = pd.DataFrame(df_mal.groupby(['Gender'])['Mean_Estimate'].mean())
    df_stacked_bar = pd.DataFrame({'Gender':df_bars_ob.index,'Obesity':df_bars_ob['Mean_Estimate'],'Malnutrition':df_bars_ml['Mean_Estimate']})
    fig,ax = plt.subplots()
    df_stacked_bar.plot(kind='bar', 
                                 stacked=True,
                                figsize=(12, 5),
                                colormap='tab20',
                                edgecolor='black',ax=ax)
    return fig

def chrt9():
    df_gpbar_gender_ob = df_obe.groupby('Age_group')['Obesity_Level'].value_counts().reset_index()
    fig = px.bar(df_gpbar_gender_ob, x='Obesity_Level',y='count',color='Age_group', barmode='group',)
    fig.update_layout(title='Obesity Level', template='plotly_dark')
    return fig

def chrt10():
    df_gpbar_gender_mal = df_mal.groupby('Age_group')['Malnutrition_Level'].value_counts().reset_index()
    fig = px.bar(df_gpbar_gender_mal, x='Malnutrition_Level',y='count',color='Age_group', barmode='group',)
    fig.update_layout(title='Malnutrition Level', template='plotly_dark')
    return fig

def chrt11():
    fig,ax = plt.subplots()
    ax.plot(df_obe[df_obe['Country']=="India"].groupby("Year")['Mean_Estimate'].mean(),label="Obesity Trend in India",marker="o")
    ax.plot(df_obe[df_obe['Country']=="China"].groupby("Year")['Mean_Estimate'].mean(),label="Obesity Trend in China",marker="o")
    ax.set_xlabel("Year")
    ax.set_xticks(df_obe['Year'].value_counts().sort_index().index)
    ax.tick_params("x", rotation=45)
    ax.set_ylabel("Average Level")
    ax.set_title("Obesity Trend Comparision between India and China")
    ax.legend()
    return fig

def chrt12():
    fig,ax = plt.subplots()
    ax.plot(df_mal[df_mal['Country']=="India"].groupby("Year")['Mean_Estimate'].mean(),label="Malnutrition Trend in India",marker="o")
    ax.plot(df_mal[df_mal['Country']=="China"].groupby("Year")['Mean_Estimate'].mean(),label="Malnutrition Trend in China",marker="o")
    ax.set_xlabel("Year")
    ax.set_xticks(df_obe['Year'].value_counts().sort_index().index)
    ax.tick_params("x", rotation=45)
    ax.set_ylabel("Average Level")
    ax.set_title("Malnutrition Trend Comparision between India and China")
    ax.legend()
    return fig