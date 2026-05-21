import requests
from google import genai

HUNTER_IO_API_KEY = '52f0cae3795354e834485a5ebb67413fb6700407'
VT_API_KEY = 'bdbec77bbec001e0eeaeb085973a930f1cc0a8a2c0c31b9cee094310b196e287'
vt_url = 'https://www.virustotal.com/api/v3/domains/'
hunterio_url='https://api.hunter.io/v2/email-verifier?email='

def ask_gemini(message_content):
    client = genai.Client(api_key='AIzaSyCsXDV5xSXISLczruH4os3h00_vBILY3Aw')

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=message_content
    )
    return response.text


def get_domain_data(domain,api_key):
    headers = {
        'x-apikey': api_key 
        }
    repsonse = requests.get(vt_url + domain,headers=headers)
    return repsonse.text

def get_email_data(email):
    params={
        'email': email,
        'api_key': HUNTER_IO_API_KEY
    }
    
    repsonse = requests.get(hunterio_url,params=params)
    return repsonse.json


domian = input('type your domain: ')
vt_content = f'summarize the json data returned from this VirusTotal search about the domain in an organized format for a terminal: {get_domain_data(domian,VT_API_KEY)}'
model_response = ask_gemini(vt_content)
print(model_response)
email = input('type in an email: ')
hunter_content = f'summarize the json data returned from this Hunter.io search about the email in an organized format for a terminal: {get_email_data(email)}'
print(ask_gemini(hunter_content))