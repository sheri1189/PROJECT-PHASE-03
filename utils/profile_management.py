import json
import os

def load_profiles():
    if not os.path.exists('data/user_profiles.json'):
        return {}
    try:
        with open('data/user_profiles.json', 'r') as f:
            # Try to load the file content
            data = json.load(f)
            if not isinstance(data, dict):
                # If the data is not a dictionary, consider it invalid
                return {}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty dictionary if file not found or JSON is invalid
        return {}

def save_profiles(profiles):
    # Make sure profiles is a dictionary before saving
    if not isinstance(profiles, dict):
        profiles = {}
    with open('data/user_profiles.json', 'w') as f:
        json.dump(profiles, f, indent=4)

def update_user_profile(user_id, toxic_word, toxicity_label, comment):
    user_profiles = load_profiles()
    if user_id not in user_profiles:
        user_profiles[user_id] = {'toxic_word_usage': {}, 'comments': [], 'toxicity_labels': []}
    if toxic_word:
        if toxic_word not in user_profiles[user_id]['toxic_word_usage']:
            user_profiles[user_id]['toxic_word_usage'][toxic_word] = 0
        user_profiles[user_id]['toxic_word_usage'][toxic_word] += 1
    user_profiles[user_id]['comments'].append(comment)
    user_profiles[user_id]['toxicity_labels'].append(toxicity_label)
    save_profiles(user_profiles)
