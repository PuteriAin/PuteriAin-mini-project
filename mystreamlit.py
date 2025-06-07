#imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns      

#dark background
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    .main, .css-1v0mbdj, .css-1d391kg, .css-1f1j6q6 {
        background-color: black !important;
        color: white !important;
    }
    h1, h2, h3, h4, h5, h6, p, label, div, span {
        color: white !important;
    }
    .stMetric, .stDataFrame {
        background-color: #1e1e1e !important;
        color: white !important;
    }
    .css-1aumxhk, .css-1y4p8pa, .css-1avcm0n {
        background-color: #121212 !important;
        color: white !important;
    }
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#symmetrical dashboard allignment
st.markdown("""
    <hr style='border: 2px solid white; margin-top: 30px; margin-bottom: 30px;'>
""", unsafe_allow_html=True)

#header image
st.image("q.jpg")

#date input
st.date_input("Select a date")

#upload data
upload_file = st.file_uploader("Please upload here:", type = 'csv')
df = pd.read_csv("country_wise_latest.csv")

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#title
st.title("""COVID-19 Analytics Dashboard 🦠 """)
st.markdown("Gain insights into the global COVID-19 pandemic through interactive visualizations and data analysis.")

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#metric cards
col1, col2, col3= st.columns(3)
col1.metric("Total Confirmed Cases🧪 ", "16,480,485", "+228,693")
col2.metric("Total Deaths Cases🕯️", "654,036", "+5,415")
col3.metric("Total Recovered Cases💚 ", "9,468,087", "+174,623")

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#pie chart
st.header("🧩 COVID-19 Cases by WHO Region ")
st.markdown("Distribution of confirmed and new cases by WHO-defined regions.")

col1, col2 = st.columns(2)

with col1:
    colors = ['#B39DDB', '#FFF59D', '#FF8A80', '#81C784', '#FFCC80', '#64B5F6'] 
    fig, ax = plt.subplots()
    df.groupby(['WHO Region'])['Confirmed'].sum().plot(kind='pie', ax=ax,   autopct='%1.1f%%', colors=colors)
    ax.set_ylabel('') 
    ax.set_title('Confirmed COVID-19 Cases by WHO Region', fontsize=18, fontweight='bold', fontname='Arial')
    st.pyplot(fig)
            
with col2:
    colors = ['#B39DDB', '#FFF59D', '#FF8A80', '#81C784', '#FFCC80', '#64B5F6'] 
    fig, ax = plt.subplots()
    df.groupby(['WHO Region'])['New cases'].sum().plot(kind='pie', ax=ax,  autopct='%1.1f%%', colors=colors)
    ax.set_ylabel('') 
    ax.set_title('New COVID-19 Cases by WHO Region', fontsize=18, fontweight='bold', fontname='Arial')
    st.pyplot(fig)

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#mapping
st.header("🗺️ Grouping Countries by COVID-19 Impact Level")
st.markdown("Countries are grouped by total confirmed cases into 3 levels: High, Medium, and Low Impact.")

# Define simple impact categories
    
def impact_level(cases):
    if cases > 1_000_000:
        return 'High Impact'
    elif cases > 100_000:
        return 'Medium Impact'
    else:
        return 'Low Impact'

df['Impact Level'] = df['Confirmed'].apply(impact_level)

    
fig = px.choropleth(df,locations="Country/Region",locationmode="country names",color="Impact Level",title="🌍 Countries Grouped by COVID-19 Impact Level",color_discrete_map={'High Impact': '#FF6F61','Medium Impact':'#FFD700','Low Impact': '#A0D6B4'})

st.plotly_chart(fig)

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#bar graph
st.header("📈 COVID-19 Trends For Top 10 Countries")
st.markdown("Bar charts showing countries with the highest counts in confirmed, death, recovery, and active cases.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Highest Confirmed Cases", "US")
col2.metric("Highest Deaths Cases", "US")
col3.metric("Highest Recovered Cases", "Brazil")
col4.metric("Highest Active Cases", "US")

fig, ax = plt.subplots(figsize=(25, 15), nrows=2, ncols=2)

# Confirmed
top10 = df.sort_values(by='Confirmed', ascending=False).head(10)
top10.plot(kind='barh', x='Country/Region', y='Confirmed', color='#FFF59D', edgecolor='#FBC02D', ax=ax[0, 0])
ax[0, 0].set_title("Top 10 Countries by Confirmed Cases", fontsize=16, fontweight='bold')
ax[0, 0].set_xlabel("Number of Cases")
ax[0, 0].set_ylabel("Country")
ax[0, 0].grid(True, linestyle='--', alpha=0.6)

# Deaths
top10 = df.sort_values(by='Deaths', ascending=False).head(10)
top10.plot(kind='barh', x='Country/Region', y='Deaths', color='#FF8A80', edgecolor='#C62828', ax=ax[0, 1])
ax[0, 1].set_title("Top 10 Countries by Deaths", fontsize=16, fontweight='bold')
ax[0, 1].set_xlabel("Number of Deaths")
ax[0, 1].set_ylabel("Country")
ax[0, 1].grid(True, linestyle='--', alpha=0.6)

# Recovered
top10 = df.sort_values(by='Recovered', ascending=False).head(10)
top10.plot(kind='barh', x='Country/Region', y='Recovered', color='#81C784', edgecolor='#388E3C', ax=ax[1, 0])
ax[1, 0].set_title("Top 10 Countries by Recoveries", fontsize=16, fontweight='bold')
ax[1, 0].set_xlabel("Number of Recoveries")
ax[1, 0].set_ylabel("Country")
ax[1, 0].grid(True, linestyle='--', alpha=0.6)

# Active
top10 = df.sort_values(by='Active', ascending=False).head(10)
top10.plot(kind='barh', x='Country/Region', y='Active', color='#64B5F6', edgecolor='#1565C0', ax=ax[1, 1])
ax[1, 1].set_title("Top 10 Countries by Active Cases", fontsize=16, fontweight='bold')
ax[1, 1].set_xlabel("Number of Active Cases")
ax[1, 1].set_ylabel("Country")
ax[1, 1].grid(True, linestyle='--', alpha=0.6)

st.pyplot(fig)

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#country selector
st.header("📌 Check Specific Country Details")
st.markdown("Use this dropdown to view key stats for a specific country.")

country_list = df['Country/Region'].unique()
selected_country = st.selectbox("Select a country:", country_list)

country_data = df[df['Country/Region'] == selected_country]
st.write(country_data[['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', '1 week change']])

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#data table
st.subheader("📄 Data of COVID-19 Cases per Country")
st.write(df)

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#correlation heatmap

st.header("🔍 Correlation Between COVID-19 Metrics")
st.markdown("This heatmap shows how different variables are correlated with each other.")

corr_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', '1 week change']
corr = df[corr_cols].corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='gray', ax=ax)
ax.set_title("Correlation Heatmap of COVID-19 Metrics", fontsize=16, fontweight='bold')

st.pyplot(fig)

st.markdown("<hr style='border: 2px solid white;'>", unsafe_allow_html=True)

#scatter graph
st.header("📉 Scatter Plots: Recovered Vs Deaths per 100 Cases")
st.markdown("These scatter plots help visualize how the number of confirmed and new cases relate to weekly trends.")

df['Recovered / 100 Cases'] = (df['Recovered'] / df['Confirmed']) * 100
df['Deaths / 100 Cases'] = (df['Deaths'] / df['Confirmed']) * 100

pastel_colors = ['orange']

fig, ax = plt.subplots(figsize=(15, 10))
df.plot(kind='scatter', x='Recovered / 100 Cases', y='Deaths / 100 Cases',color=pastel_colors[0], ax=ax, label='Recovered / 100 Cases')

ax.set_title('Recovered vs Deaths per 100 Cases', fontsize=16, fontweight='bold')
ax.set_xlabel('Recovered / 100 Cases')
ax.set_ylabel('Deaths / 100 Cases')
ax.grid(True)
ax.legend()

st.pyplot(fig)

