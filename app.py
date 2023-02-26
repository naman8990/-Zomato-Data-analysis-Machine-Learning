import pandas as pd
import streamlit as st
df=pd.read_csv(r"C:\Users\naman\OneDrive - sonyacd\zomato anmol\final_zomato.csv")

def recommend_restaurant(cuisine,location):
    filtered_df =df[(df['Restaurant_address'] == location)]
    # Popular Cuisine in the area
    popular_cuisine = filtered_df['C'].mode()[0]
    
    # Average price for 1 person
    average_price = filtered_df['Price for one'].mean()
    
    # Most Popular Restaurant and Cuisine they are serving
    most_popular_restaurant = filtered_df.loc[filtered_df['Ratings'].idxmax(), 'Name']
    most_popular_cuisine = filtered_df.loc[filtered_df['Ratings'].idxmax(), 'C']
    
    # Most Popular restaurant serving the same cuisine
    similar_cuisine_df = df[(df['C'] == cuisine)& (df['Restaurant_address'] == location)]
    most_popular_similar_cuisine_restaurant = similar_cuisine_df.loc[similar_cuisine_df['Ratings'].idxmax(), 'Name']
    
    output = {
        "Popular cuisine in this area": popular_cuisine,
        "Average price for one in this area": average_price,
        "Most popular restaurant in this area": most_popular_restaurant,
        "Cuisine served by the most popular restaurant in this area": most_popular_cuisine,
        "Most popular restaurant serving the same cuisine as user provided": most_popular_similar_cuisine_restaurant
    }
    
    return output

def app():
    st.title("Restaurant Recommender")

    # Add user input fields
    cuisine = st.text_input("Enter cuisine type:")
    location = st.text_input("Enter location:")

    # Add a button to call the function
    if st.button("Recommend"):
        # Call the function and display the results
        results = recommend_restaurant(cuisine, location)
        for key, value in results.items():
            st.write(f"{key}: {value}")

# Run the app
if __name__ == '__main__':
    app()