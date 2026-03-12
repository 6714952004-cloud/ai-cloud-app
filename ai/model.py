def ai_response(text):

    text = text.lower()

    if "hello" in text:
        return "Hello!"

    if "สวัสดี" in text:
        return "สวัสดีครับ"

    if "hi" in text:
        return "Hi!"

    return "I don't understand"