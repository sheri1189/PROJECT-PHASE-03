import streamlit as st
from utils.toxicity import classify_toxicity, replace_toxic_words
from utils.profile_management import load_profiles, save_profiles, update_user_profile

st.title('Toxicity Detection System')

user_id = st.text_input('Enter your User ID')

text = st.text_area('Enter your comment:')
if st.button('Submit'):
    toxicity_label = classify_toxicity(text)
    processed_text, toxic_word_detected = replace_toxic_words(text)
    
    user_profiles = load_profiles()
    update_user_profile(user_id, toxic_word_detected, toxicity_label, processed_text)
    save_profiles(user_profiles)

    st.write(f'Processed Comment: {processed_text}')
    st.write(f'Toxicity Label: {toxicity_label}')

    comments = user_profiles.get(user_id, {}).get('comments', [])
    st.write('Your Comment History:')
    for comment in comments:
        st.write(comment)
