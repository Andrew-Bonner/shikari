import requests
from google import genai

HUNTER_IO_API_KEY = '52f0cae3795354e834485a5ebb67413fb6700407'
VT_API_KEY = 'bdbec77bbec001e0eeaeb085973a930f1cc0a8a2c0c31b9cee094310b196e287'
SHODAN_API_KEY = 'zuskxF9kEtDzDIEQ96OJTRcmHrKyZc48'
SHODAN_URL = 'https://api.shodan.io/dns/domain/'
vt_url = 'https://www.virustotal.com/api/v3/domains/'
hunterio_url='https://api.hunter.io/v2/email-verifier?'

def ask_gemini(message_content):
    client = genai.Client(api_key='AIzaSyBbLTqRnyEH0DKAWok_lVo6iLFu6RW2Yt4')

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
    params = {
        'api_key':HUNTER_IO_API_KEY,
        'email':email
    }
    repsonse = requests.get(hunterio_url,params=params)
    return repsonse.json()

def get_shodan_domain(domain):
    SHODAN_URL = f'https://api.shodan.io/dns/domain/{domain}'
    params = {
        'key': SHODAN_API_KEY,
    }
    response = requests.get(SHODAN_URL,params=params)
    return response.json()
    

domain = input('type your domain: ')
#vt_content = f'summarize the json data returned from this VirusTotal search about the domain in an organized format for a terminal: {get_domain_data(domian,VT_API_KEY)}'
shodan_content = f'summarize the json data returned from this shodan search on a domain and organize it in a format that can be viewed in the terminal: {get_shodan_domain(domain)}'
model_response = ask_gemini(shodan_content)
print(model_response)
#email = input('type in an email: ')
#hunter_content = f'convert the json data into a summary about the email in an organized format for a terminal: {get_email_data(email)}'
#print(ask_gemini(hunter_content))