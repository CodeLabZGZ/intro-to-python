"""View Instagram user follower count from Instagram public api"""
import requests

from flask import Flask, request, render_template
app = Flask(__name__)

def getfollowedby(url):
 """View Instagram user follower count"""
 link = 'https://www.instagram.com/%s/?__a=1'
 tag = link % (url)
 user = requests.get(tag)
 return (user.json()['user']['followed_by']['count'])

def getname(url):
 """Split the URL from the username"""
 return url.replace("https://", "").replace("www.", "").replace("instagram.com/", "").replace("/", "")


@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    
    return getfollowedby(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)