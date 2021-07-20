from datetime import datetime

def sample_responses(input_text): 
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"): 
        return "Hey! What's up, homie?"

    if user_message in ("who is this", "who are you?"): 
        return "I am a test bot"

    if user_message in ("what's the time?", "time", "time?"): 
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        return str(date_time)
    
    return "I don't understand you"
        