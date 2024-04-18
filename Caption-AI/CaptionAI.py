"""
At the command line, only need to run once to install the package via pip:

$ `pip install google-generativeai`
"""
import google.generativeai as genai

genai.configure(api_key="AIzaSyBQZiYBsCR0aLm7EW_OZBp0aOrlehD2dMI")
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hey, help me write a funny caption for my friends 20th birthday. hes sitting at a pizza place having macrons and cupcakes and pizza"]
  },
  {
    "role": "model",
    "parts": ["Haha, that sounds like quite the birthday feast! Here are a few funny caption options for your friend's 20th birthday photo:\n\nCaption 1: \"20 years old and still can't decide between pizza and dessert. Happy birthday, [friend's name]!\" #GrowingUpIsHard  \nCaption 2: \"[Friend's name] is proof that you can have your cake and eat pizza too. Happy 20th!\"  #BirthdayGoals \nCaption 3: \"This is what happens when you let a 20-year-old plan their own birthday dinner. Happy birthday, [friend's name]!\" #PizzaAndMacarons \nCaption 4: \"Not sure what's more impressive, the food spread or the fact that he's 20. Happy birthday, [friend's name]!\"  #TwentyAndThriving \nCaption 5: \"Forget the candles, [friend's name] is celebrating with carbs. Happy 20th!\"  #CarbLoading"]
  },
  {
    "role": "user",
    "parts": ["i want more captions"]
  },
  {
    "role": "model",
    "parts": ["Alright, here are a few more funny captions to choose from:\n\nCaption 1:\"Living his best life at 20... one bite at a time. Happy birthday, [friend's name]!\" #FoodieFriend \nCaption 2: \"This is 20: fueled by pizza, macarons, and good times. Happy birthday, [friend's name]!\" #FueledByFood \nCaption 3: \"[Friend's name] is 20 today, but his taste buds are still 5. Happy birthday!\" #KidAtHeart \nCaption 4: \"Happy birthday to the friend who can eat anything and still look fabulous. Cheers to 20, [friend's name]!\" #BirthdayBoy \nCaption 5:\"Turns out you can have it all at 20. Pizza, macarons, cupcakes... and a birthday celebration! Happy birthday, [friend's name]!\" #Spoiled"]
  },
  {
    "role": "user",
    "parts": ["hey"]
  },
  {
    "role": "model",
    "parts": ["Hey there! What can I do for you today?  😊"]
  },
  {
    "role": "user",
    "parts": ["generate captions"]
  },
  {
    "role": "model",
    "parts": ["Caption 1:\"[Friend's name] turned 20 and decided to celebrate with the most epic food coma ever. Happy birthday!\" #FoodComaGoals \nCaption 2: \"20 years old and already a master of the balanced diet: pizza, macarons, and cupcakes. Happy birthday, [friend's name]!\" #BalancedDiet \nCaption 3: \"This is how [friend's name] rolls on his 20th birthday. Happy birthday, you pizza-loving, macaron-munching legend!\" #Legend \nCaption 4: \"Happy 20th birthday to the friend who knows the way to our hearts is through our stomachs. Cheers, [friend's name]!\" #FriendGoals \nCaption 5: \"Proof that age is just a number when you have pizza, macarons, and cupcakes. Happy 20th birthday, [friend's name]!\" #ForeverYoung"]
  },
  {
    "role": "user",
    "parts": ["give me more caprions"]
  },
  {
    "role": "model",
    "parts": ["No problem, here are a few more options: \n\nCaption 1: \"20 never looked so delicious. Happy birthday, [friend's name]!\" #BirthdayFeast \nCaption 2: \"[Friend's name] is 20 today, but his birthday spread is ageless. Happy birthday!\" #TimelessTreats \nCaption 3: \"Forget the birthday cake, [friend's name] is celebrating with pizza and macarons. Happy 20th!\" #Upgrade \nCaption 4: \"This is what happens when you combine a 20th birthday with a cheat day. Happy birthday, [friend's name]!\" #CheatDayChamp \nCaption 5: \"Happy 20th birthday to the friend who knows how to party... with his taste buds. Cheers, [friend's name]!\" #TasteBudParty"]
  },
  {
    "role": "user",
    "parts": ["hey"]
  },
  {
    "role": "model",
    "parts": ["Hey there! What kind of captions would you like me to help you with today? 😊"]
  },
  {
    "role": "user",
    "parts": ["its me going to a listening party for taylor's new album The tortured poets department release"]
  },
  {
    "role": "model",
    "parts": ["Caption 1: \"Heading to the listening party for Taylor's new album, The Tortured Poets Department Release, ready to have my heart broken and put back together again. #TorturedPoetVibes\" \nCaption 2: \"Swifties unite! I'm on my way to the listening party for The Tortured Poets Department Release. Can't wait to hear what Taylor has in store for us. #SwiftTok\" \nCaption 3: \"POV: Me listening to Taylor's new album for the first time at the listening party. Tissues at the ready. #TaylorSwiftIsMyTherapist\" \nCaption 4: \"I'm so excited to be at the listening party for Taylor's new album. I can already feel the emotions coming. #AllTheFeels\" \nCaption 5: \"Can't believe I'm here at the listening party for Taylor's new album. I'm ready to be transported to another world. #MusicMagic\""]
  },
])

while True:
  print("Hey there! What can I do for you today?  ")
  user_input = input("Tell me about your photo (or 'quit' to exit): ")

  if user_input.lower() == "quit":
    break

  convo.send_message(user_input)  # Send user input to the conversation

  print(convo.last.text)  # Print the model's response (captions)

  # No need to ask for further input here, the loop continues automatically

print("Thanks for using the Caption AI - Developed by @purohitamann Have a great day. ")
