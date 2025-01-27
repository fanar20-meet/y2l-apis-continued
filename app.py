from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])



def study_image():
        image_url = request.form['url-input']  
        headers = {'Authorixation' : 'key < 3ec5e4ff7f814f37a5351e44c4c38685>'}
        api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
        data ={"inputs": [
              {
                "data": {
                 "image": {
                  "url": 'image_url'
                  }
                }
            }
        ]}

        response = request.post(api_url,headers=headers,data=jason.dumps(data))

    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    
        return render_template('home.html', results=response)

# response = request.post(api_url,headers=headers,data=jason.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)



    