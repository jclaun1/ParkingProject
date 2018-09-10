import subprocess
import requests
import json

ngrok = subprocess.Popen(['ngrok', 'tcp', '22'], stdout = subprocess.PIPE)

localhost_url = "http://localhost:4040/api/tunnels"
tunnel_url = requests.get(loicalhost_url).text
j = json.loads(tunnel_url)

tunnel_url = j['Tunnels'][0]['PublicUrl']
