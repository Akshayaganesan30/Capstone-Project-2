#Import required modules
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import Obesity_malnutrition_queries as New_MN2
import Viz_obml

#Set the page layout as wide
st.set_page_config(layout="wide")

#To display the title of the project
st.title(":blue[Obesity and malnutrition]")

#To create a sidebar menu with options Filter Criteria and Queries
with st.sidebar:
    selected = option_menu("Nutrition Paradox: A Global View on Obesity and Malnutrition",
                           ["Home","Queries on Obesity","Queries on Malnutrition","Queries on Obesity and Malnutrition","Data Visualization on Obesity and Malnutrition"],
                           icons=['house'],
                           menu_icon="cast",
                           default_index=0)
if selected == "Home":
    st.header("Introduction",divider="blue")
    st.subheader("Obesity")
    text_obe = """Obesity is classified by the World Health Organization (WHO) as a chronic,relapsing disease arising from complex interactions between
    genetics, neurobiology, eating behaviours, access to healthy diet, market forces, and the broader environment.
            WHO defines overweight and obesity as outlined below.
            
            Adults
                    For adults: Overweight is a BMI greater than or equal to 25
                                Obesity is a BMI greater than or equal to 30.
            Children
                    Children aged between 5–19 years
                            Overweight is BMI-for-age greater than 1 standard deviation above the WHO Growth Reference median
                            Obesity is greater than 2 standard deviations above the WHO Growth Reference median.
                    Children under 5 years of age
                            Overweight is weight-for-height greater than 2 standard deviations above WHO Child Growth Standards median and
                            Obesity is weight-for-height greater than 3 standard deviations above the WHO Child Growth Standards median."""
    st.text(text_obe)
    st.subheader("Malnutrition")
    text_mal = """Malnutrition refers to deficiencies, excesses, or imbalances in a person’s intake of energy and/or nutrients. The term malnutrition addresses 3 broad groups of conditions
    
            Undernutrition, which includes wasting (low weight-for-height), stunting (low height-for-age) and underweight (low weight-for-age)
            Micronutrient-related malnutrition, which includes micronutrient deficiencies (a lack of important vitamins and minerals) or micronutrient excess
            Overweight, obesity and diet-related noncommunicable diseases (such as heart disease, stroke, diabetes and some cancers)."""
    st.text(text_mal)

qry_obe = ["1.Top 5 regions with the highest average obesity levels in the most recent year(2022)",
            "2.Top 5 countries with highest obesity estimates",
            "3.Obesity trend in India over the years(Mean_estimate)",
            "4.Average obesity by gender",
            "5.Country count by obesity level category and age group",
            "6.Top 5 countries least reliable countries(with highest CI_Width) and Top 5 most consistent countries (smallest average CI_Width)",
            "7.Average obesity by age group",
            "8.Top 10 Countries with consistent low obesity (low average + low CI)over the years",
            "9.Countries where female obesity exceeds male by large margin (same year)",
            "10.Global average obesity percentage per year"
          ]

if selected == "Queries on Obesity":
    with st.container(border=True,height = 450):
        option = st.selectbox("Queries on Obesity",
                            (qry_obe
                            ),
                            index=None,
                            placeholder="Select your Query"
                        )   
        if option == qry_obe[0]:
            st.dataframe(New_MN2.qn1(),hide_index=True)
        if option == qry_obe[1]:
            st.dataframe(New_MN2.qn2(),hide_index=True)
        if option == qry_obe[2]:
            st.dataframe(New_MN2.qn3(),hide_index=True,column_order=("Year","Obesity_level"))
        if option == qry_obe[3]:
            st.dataframe(New_MN2.qn4(),hide_index=True)
        if option == qry_obe[4]:
            st.dataframe(New_MN2.qn5(),hide_index=True,column_order=("Age_group","Obesity_Level","No_of_Countries"))
        if option == qry_obe[5]:
            ans,ans1=New_MN2.qn6()
            st.text("Top 5 countries least reliable countries")
            st.dataframe(ans,hide_index=True)
            st.text("Top 5 most consistent countries")
            st.dataframe(ans1,hide_index=True)
        if option == qry_obe[6]:
            st.dataframe(New_MN2.qn7(),hide_index=True)
        if option == qry_obe[7]:
            st.dataframe(New_MN2.qn8(),hide_index=True)
        if option == qry_obe[8]:
            st.dataframe(New_MN2.qn9())
        if option == qry_obe[9]:
            st.dataframe(New_MN2.qn10(),hide_index=True,column_order=("Year","Obesity_Percentage"))
        
qry_mal = ["1.Avg. malnutrition by age group",
            "2.Top 5 countries with highest malnutrition(mean_estimate)",
            "3.Malnutrition trend in African region over the years",
            "4.Gender-based average malnutrition",
            "5.Malnutrition level-wise (average CI_Width by age group)",
            "6.Yearly malnutrition change in specific countries(India, Nigeria, Brazil)",
            "7.Regions with lowest malnutrition averages",
            "8.Countries with increasing malnutrition",
            "9.Min/Max malnutrition levels year-wise comparison",
            "10.High CI_Width flags for monitoring(CI_width > 5)"
          ]

if selected == "Queries on Malnutrition":
    with st.container(border=True,height = 450):
        option = st.selectbox("Queries on Malnutrition",
                            (qry_mal
                            ),
                            index=None,
                            placeholder="Select your Query"
                        )
        if option == qry_mal[0]:
            st.dataframe(New_MN2.qn11(),hide_index=True)
        if option == qry_mal[1]:
            st.dataframe(New_MN2.qn12(),hide_index=True)
        if option == qry_mal[2]:
            st.dataframe(New_MN2.qn13(),hide_index=True,column_order=("Year","Malnutrition_Level"))
        if option == qry_mal[3]:
            st.dataframe(New_MN2.qn14(),hide_index=True)
        if option == qry_mal[4]:
            st.dataframe(New_MN2.qn15(),hide_index=True)
        if option == qry_mal[5]:
            st.dataframe(New_MN2.qn16(),hide_index=True,column_order=("Year","Country","Malnutrition_Level"))
        if option == qry_mal[6]:
            st.dataframe(New_MN2.qn17(),hide_index=True)
        if option == qry_mal[7]:
            st.dataframe(New_MN2.qn18(),hide_index=True)
        if option == qry_mal[8]:
            st.dataframe(New_MN2.qn19(),hide_index= True,column_order=("Year","Malnutrition_Level_Max","Malnutrition_Level_Min"))
        if option == qry_mal[9]:
            st.dataframe(New_MN2.qn20(),hide_index=True)

qry_ob_mal = ["1.Obesity vs malnutrition comparison by country(any 5 countries)",
            "2.Gender-based disparity in both obesity and malnutrition",
            "3.Region-wise avg estimates side-by-side(Africa and America)",
            "4.Countries with obesity up & malnutrition down",
            "5.Age-wise trend analysis"
           ]

if selected == "Queries on Obesity and Malnutrition":
    with st.container(border=True,height = 450):
        option = st.selectbox("Queries Obesity and Malnutrition",
                            (qry_ob_mal
                            ),
                            index=None,
                            placeholder="Select your Query"
                        )
        if option == qry_ob_mal[0]:
            st.dataframe(New_MN2.qn21(),hide_index=True)
        if option == qry_ob_mal[1]:
            st.dataframe(New_MN2.qn22(),hide_index=True)
        if option == qry_ob_mal[2]:
            st.dataframe(New_MN2.qn23(),hide_index=True)
        if option == qry_ob_mal[3]:
            st.dataframe(New_MN2.qn24(),width=200,hide_index=True)
        if option == qry_ob_mal[4]:
            yr,ob_chd,ob_adt,ml_chd,ml_adt = New_MN2.qn25()
            df = pd.DataFrame(
                {
                    "Year":yr,
                    "Obesity-Children": ob_chd,
                    "Obesity-Adult": ob_adt,
                    "Malnutrition-Children": ml_chd,
                    "Malnutrition-Adult": ml_adt,
                }
            )
            st.dataframe(df,hide_index=True)

opt = ["Obesity and Malnutrition trend",
       "TOP 10 Countries by Obesity and Malnutrition",
       "Variability of Obesity on different Regions",
       "Variability of Malnutrition on different Regions",
       "To identiy patterns in Obesity data",
       "To identify patterns in Malnutrition data",
       "Distribution of Obesity and Malnutrition",
       "Obesity and malnutriiton by gender",
       "Obesity Level based on Age group",
       "Malnutrition Level based on Age group",
       "Obesity Trend in India and China",
       "Malnutrition Trend in India and China"]

if selected == "Data Visualization on Obesity and Malnutrition":
    with st.container(border=True):
        option = st.selectbox("Select one for data visualization",
                            (opt
                            ),
                            index=None,
                            placeholder="Select one Data"
                        )
        if option == opt[0]:
            st.pyplot(Viz_obml.chrt1())
        if option == opt[1]:
            st.pyplot(Viz_obml.chrt2())
        if option == opt[2]:
            st.pyplot(Viz_obml.chrt3())
        if option == opt[3]:
            st.pyplot(Viz_obml.chrt4())
        if option == opt[4]:
            st.pyplot(Viz_obml.chrt5())
        if option == opt[5]:
            st.pyplot(Viz_obml.chrt6())
        if option == opt[6]:
            st.pyplot(Viz_obml.chrt7())
        if option == opt[7]:
            st.pyplot(Viz_obml.chrt8())
        if option == opt[8]:
            st.plotly_chart(Viz_obml.chrt9())
        if option == opt[9]:
            st.plotly_chart(Viz_obml.chrt10())
        if option == opt[10]:
            st.pyplot(Viz_obml.chrt11())
        if option == opt[11]:
            st.pyplot(Viz_obml.chrt12())


