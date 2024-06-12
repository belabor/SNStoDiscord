import json
from urllib.request import Request, urlopen

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)

    webhook_url = 'WEBHOOK_URL_HERE'
    
    snsmsg = { 'content': message }

    req = Request(webhook_url, json.dumps(snsmsg).encode('utf-8'))
        
    # Discord will reject without these..
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    response = urlopen(req)
    response.read()

    return message
