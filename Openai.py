#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai


# In[9]:


import openai

# Set your API key
api_key = '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'
print('1.Hindi')
print('2.Hinglish')

i=int(input("Enter your Choice:-"))
# Prompt for translation

if(i==1):
    input_text = "Translate the following English text to Hindi: "+input("")
else:
    input_text = "Translate the following English text to Hinglish: "+input("")
# Define the API endpoint and parameters

endpoint = "davinci"
engine = "text-davinci-002"  # This engine is optimized for text generation
max_tokens = 100  # Adjust this as needed for your translation

# Make the API call to translate English to Hindi
response = openai.Completion.create(
    engine=engine,
    prompt=input_text,
    max_tokens=max_tokens,
    api_key=api_key
)

# Extract the translated text from the response
translation = response.choices[0].text.strip()

# Print the translation
print("Translated text:")
print(translation)


# In[ ]:





# In[ ]:





# In[ ]:




