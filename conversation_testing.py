import streamlit as st
from openai import OpenAI
import pandas as pd
import json

st.title("Bot conversation testing")
st.write("upload the conversation in csv")

## Limits

## number of chats to test 10
## number of agent tool to test 100


# define the openai key


openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    client  = OpenAI(api_key="")

    # Read the csv file
    uploaded_file = st.file_uploader("Upload the CSV file", type="csv")

    if uploaded_file is not None :
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write(df.describe())

        ## convert to json
        # Convert the DataFrame to a list of JSON objects
        json_data = df.to_dict(orient='records')

        # Convert list of dictionaries to JSON string
        json_string = json.dumps(json_data, indent=2)

        # Display the JSON data
        st.write("JSON data:")
        st.write(json_data)

        messages = [
            {
                "role": "user",
                "content": f"conversation of the user and bot: {json_string} \n\n---\n\n Analyse the conversation",
            }
        ]

        # Generate an answer using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )

        # Stream the response to the app using `st.write_stream`.
        st.write_stream(stream)



## Make the api call to generate the user responses for the bot

## run the gpt prompt and validate the score.

## send an response



