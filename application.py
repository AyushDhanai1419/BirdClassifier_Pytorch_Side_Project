from flask import Flask, render_template,request
from commons import get_tensor, get_bird_information
from inference import get_bird_name
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    # This if will work when we recieve a get request - loading the home page
    if request.method == 'GET':
        return render_template('index.html',value="Welcome to Bird Classifier")
    
    # This if will work when we recieve a post request - after submiting an image file
    if request.method == 'POST':
        if 'file' not in request.files:
            print("file not uploaded")
            return
        file_read = request.files['file']
        # file.save('uploaded_file.jpeg') to save the file in the disk
        
        image_file = file_read.read()
        bird_name, category = get_bird_name(image_bytes=image_file)

        # getting information about the predicted bird species 
        bird_name.replace('_',' ')
        about_bird_species = get_bird_information(bird_name)
        return render_template('result.html',predicted_bird=bird_name,bird_category=category,about_bird=about_bird_species)


if __name__ == '__main__':
    app.run(debug=True)
