import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Welcome To Your Daily-Fitness-Track-Report")
file=st.file_uploader("***Upload Your Activity Sheet***",type=['csv','xlsx'])
if file is not None:
    if file.name.endswith('.csv'):
        df=pd.read_csv(file)

    else:
        df=pd.read_excel(file)

    st.header("Your Record")
    st.write(df.head())

    fig,ax=plt.subplots(figsize=(6,3))
    pl=df.groupby('Activity')['Eq_Steps'].sum()
    ax.plot(pl.index,pl,color='white',linestyle='--',marker='*',markersize=5)
    ax.set_title("Activity wise Effort")
    ax.set_facecolor('skyblue')
    ax.set_xlabel("Activity")
    ax.set_ylabel("Eq Steps")
    ax.grid()
    st.pyplot(fig)

    fig,ax=plt.subplots(figsize=(4,6))
    jk=df.groupby('Activity')['Workout_Minutes'].sum()
    st.write(jk)
    ax.pie(jk,labels=jk.index,autopct='%1.2f%%',explode=[0.1,0,0,0,0,0])
    ax.set_facecolor('black')
    ax.legend(
        bbox_to_anchor=(0.5, 1.02, 1., .05),
        loc="right",
        facecolor='pink')

    ax.set_title('Time spent per Activity')
    st.pyplot(fig)


    fig,ax=plt.subplots(1,2,figsize=(12,4))
    ax[0].plot(df['Date'],df['Eq_Steps'],color='blue',label='Eq Steps',marker='o')
    ax[0].set_title('Steps Per Day')
    ax[0].grid()
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Eq Steps')
    ax[0].tick_params(axis='x',rotation=90)
    #ax[0].tick_params(axis='x', rotation=70)
    #st.pyplot(fig)
    ax[1].plot(df['Date'], df['Calories_Burned'], color='green', label='Calories Burned',marker='o')
    ax[1].set_title('Calories burned Per Day')
    ax[1].grid()
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Calories')
    plt.xticks(rotation=90)
    ax[1].set_ylabel('Eq Steps')
    st.pyplot(fig)

    fig,ax=plt.subplots(figsize=(6,3))
    ax.bar(df['Date'],df['Sleep_Hours'],color='red',)
    ax.set_title('Sleep Hours Trends')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sleep Hours')
    ax.grid()
    ax.tick_params(axis='x',rotation=90)
    st.pyplot(fig)

    fig,ax=plt.subplots(figsize=(6,3))
    gp=df.groupby('Activity')['Water_Intake_Liters'].mean()
    ax.barh(gp.index,gp,color='blue',label='Water Intake')
    ax.set_facecolor('black')
    ax.set_title('Average Water Intake per activity')
    ax.set_ylabel('Activity')
    ax.set_xlabel('Water Intake')

    ax.grid()
    st.pyplot(fig)

    fig,ax=plt.subplots(1,2,figsize=(12,4))
    ax[0].bar(df['Date'],df['Average_Heart_Rate'],color='blue')
    ax[0].set_facecolor('pink')
    ax[0].set_title('Daily Average Heart Rate')
    ax[0].set_xlabel('Date')

    ax[0].set_ylabel('Daily Average Heart Rate')
    ax[0].tick_params(axis='x', rotation=90)
    gf=df.groupby('Activity')['Average_Heart_Rate'].mean()
    ax[1].bar(gf.index,gf,color='red')
    ax[1].facecolor='blue'
    ax[1].set_title('Average Heart Rate by Activity')
    ax[1].set_xlabel('Activity')
    ax[1].set_ylabel('Heart Rate')
    ax[1].tick_params(axis='x',rotation=90)
    st.pyplot(fig)



    fig,ax=plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    st.pyplot(fig)