from django.shortcuts import render, redirect
from google import genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from google.genai import types
import base64


def generate(user_input):
  client = genai.Client(
      api_key=("YOUR_API_KEY")
  )

  model = "gemini-2.0-flash"
  contents = [
      types.Content(
          role="user",
          parts=[
              types.Part.from_text(
                  text=user_input
              ),
          ],
      ),
  ]
  generate_content_config = types.GenerateContentConfig(
      temperature=1,
      top_p=0.95,
      top_k=40,
      max_output_tokens=8192,
      response_mime_type="text/plain",
  )
  res=""
  for chunk in client.models.generate_content_stream(
      model=model,
      contents=contents,
      config=generate_content_config,
  ):
    # print(chunk.text, end="")
    res+=chunk.text
  return res

def index(request):
    return render(request, 'index.html')

def myfiles(request):
    return render(request, 'myfiles.html')

def mylearning(request):
    
    # client = genai.Client(api_key="AIzaSyDborNKyQdkM4546d3KbBkUl26Tjo1hHKM")
    # response = client.models.generate_content(model="gemini-2.0-flash", contents="Hi")
    # print(response.text)
    return render(request, 'mylearning.html')

def search(request):
    return render(request, 'search.html')

def nirnayai(request):
    try:
        if request.method=="POST":
            user_input=request.POST.get('user-input')
            response=generate(user_input)
            print(response)
            param={'response':response}
            return render(request, 'nirnayai.html', param)
        return render(request, 'nirnayai.html')
    except:
        pass

def formfilling(request):
    return render(request, 'formfilling.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
