from flask import Flask, request, render_template
import cv2
import your_model_module  # Import your model module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Save the uploaded image to a temporary file
    file.save('uploaded_image.jpg')

    # Process the image using your models
    image = cv2.imread('uploaded_image.jpg')
    result = your_model_module.process_image(image)

    # Display the result on the webpage
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)