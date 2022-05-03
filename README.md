# CZ4171-IoT: Communications and Networking Project 
![photo_2022-04-17_21-52-39](https://user-images.githubusercontent.com/62253459/163717676-d9dc3682-d1c7-4b9e-a2bb-dc2323f9beb6.jpg)
For this project, Singapore Dollars Image Classification Application have been developed. This application allows users to select images from his or her Android Device or to use the camera to take a picture of the note. The image will be uploaded to Flask Server which will perform a prediction based on the image sent. The prediction result will then be sent from the server to the Android Application for it to be displayed.
Therefore, for this project to be done, there are three parts that is required to be done: 
1. Image Classification Model 
2. Flask Server Development 
3. Android Application Development 

## 1. Image Classification Model 
Google Teachable Machine has been used to train the model for the Note Classification. To train the mode, around 600 images of each dollar note class has been taken. The note class are namely - Fifty, Ten, Five and Two. 
The parameters used for training are as follows: 
1. Epochs: 50 (The number of times the algorithm will go through for the entire training dataset)
2. Batch Size: 16 (The number of samples to go through before updating the internal model paramaters
3. Learning Rate: 0.001 (A tuning parameter that determines the step size at each iteration) 

The trained model have the following diagrams to determine its accuracy: 
### 1. Accuracy Per Class
![apc](https://user-images.githubusercontent.com/62253459/163720406-b9db77d6-be22-4e28-a98b-52ef02641978.jpg)

### 2. Confusion Matrix
![cm](https://user-images.githubusercontent.com/62253459/163720415-aad7d99d-36a8-47e9-ba77-92861eeee3cd.jpg)

### 3. Accuracy per Epoch 
![ape](https://user-images.githubusercontent.com/62253459/163720416-6f29262c-4484-4bda-a702-4a6bb1e4e816.jpg)

### 4. Loss per Epoch 
![lpe](https://user-images.githubusercontent.com/62253459/163720418-a42bb696-1644-4ca0-9ff9-ef6e48850e57.jpg)

Based on the diagrams and numbers, the numbers have shown to be reasonable enough for the Money Classification Application. Therefore, the model have been exported to Tensorflow in Keras Format, named sgdMoney.h5.

The Teachable Machine file is named as sgdDollars.tm which can be opened in the Google Teachable Machine website to adjust the necessary parameters for future use. 

## 2. Python-Flask Server Development 
The codes for the Python Flask Server can be found in the iotServer folder. 
The Keras Model as obtained from the training should be stored in the same file directory as the Flask Server and be declared in the Python Server code. 
There exists a Predict Function in the code that is used to deploy the model. This function allows us to run the prediction on images of the money, which returns the predicted note class. 
In the server, all that is required to do is to use a POST request to receive the image file uploaded from the IoT Device. Then it uses the file directory of the uploaded image to run the Predict Function. 
This prediction will be returned as a response, which will be sent to the apllication. 

## 3. Android Application Development 
The codes for the Android Application can be found in the IOTProject folder. 
The UI of the Android Application is shown below: 

![photo_2022-04-30_13-41-53](https://user-images.githubusercontent.com/62253459/166093123-f9445837-c913-4d41-bc63-029910498fe2.jpg)


There are 2 buttons that allows users to either select the image from the gallery or to use the camera function to take the photo.
Once the image is selected or taken from the camera, it will be shown on the placeholder. By clicking on the Predict Button, it sends the image to the server that has the Keras Machine Learning Model. The prediction process will then be processed in the server and the result will be sent back to the Android Application, which will be displayed in the textview. The application with the predicted result is shown below: 

![example](https://user-images.githubusercontent.com/62253459/163723145-f993bee6-1e25-4a46-8a84-18eb0739fec1.jpg)

## Video Demo 
https://youtu.be/_MiuO6lj_y8

