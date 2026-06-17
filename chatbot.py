# =================================================================
# METHOD 1: First Method
# =================================================================
# questions = [
#     "what is your return policy",
#     "how long does shipping take",
#     "how can i contact customer support"
# ]
# answers = [
#     "You can return any product within 30 days.",
#     "Shipping takes 3 to 5 business days.",
#     "You can email us at support@codealpha.tech."
# ]
# print("Chatbot Started! (Type 'exit' to stop)")
# while True:
#     user_input = input("\nYou: ").lower()
#     if user_input == 'exit':
#         print("Goodbye!")
#         break
#     best_match = -1
#     max_matches = 0
#     for i in range(len(questions)):
#         match_count = 0
#         for word in user_input.split():
#             if word in questions[i]:
#                 match_count += 1
#         if match_count > max_matches:
#             max_matches = match_count
#             best_match = i
#     if max_matches > 0:
#         print("Bot:", answers[best_match])
#     else:
#         print("Bot: I didn't understand. Please rephrase.")


# =================================================================
# METHOD 2: This is Cleaning method We can also use this
# =================================================================
questions = [
    "what is your return policy",
    "how long does shipping take",
    "how can i contact customer support"
]

answers = [
    "You can return any product within 30 days.",
    "Shipping takes 3 to 5 business days.",
    "You can email us at support@codealpha.tech."
]

print("Chatbot Started! (Type 'exit' to stop)")

while True:
    user_input = input("\nYou: ").lower()
    
    if user_input == 'exit':
        print("Goodbye!")
        break
        
    # --- CLEANING LOGIC ---
    for char in "?!.,:":
        user_input = user_input.replace(char, "")
        
    best_match = -1
    max_matches = 0
    
    for i in range(len(questions)):
        match_count = 0
        for word in user_input.split():
            if word in questions[i]:
                match_count += 1
                
        if match_count > max_matches:
            max_matches = match_count
            best_match = i
            
    if max_matches > 0:
        print("Bot:", answers[best_match])
    else:
        print("Bot: I didn't understand. Please rephrase.")