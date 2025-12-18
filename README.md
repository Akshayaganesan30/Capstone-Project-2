# Capstone-Project-2
Nutrition Paradox: A Global View on Obesity and Malnutrition

To investigate the complex challenge of undernutrition and overnutrition across different countries, age groups, and genders : publicly available WHO data is used to uncover trends, patterns, and disparities in obesity and malnutrition rates around the world.

Data set is collected from below URLS:
    For Obesity:
      https://ghoapi.azureedge.net/api/NCD_BMI_30C – Obesity among adults (BMI ≥ 30)
      https://ghoapi.azureedge.net/api/NCD_BMI_PLUS2C – Obesity/Overweight among children 
    For Malnutrition:
      https://ghoapi.azureedge.net/api/NCD_BMI_18C – Underweight in adults (BMI < 18.5)
      https://ghoapi.azureedge.net/api/NCD_BMI_MINUS2C – Thinness in children


The data is collected from the above URLS and it is then preprocessed. The data type conversion,data cleaning and feature engineering is done so that the final data has no type mismatch and missing values. The selected data is then written to SQL table. The queries are written accordingly to brign the output. The output is given in the Streamlit UI.Data visualization is also done for a clearer insight in the same Streamlit UI
