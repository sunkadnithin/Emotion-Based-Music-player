# Emotion-Based-Music-player
This model can predict live emotion from a video and play songs according to the last emotion captured.

**The Emotion Based Music Player** project is a system that uses image processing and machine learning to play music based on the user's current emotion. The system consists of four main components: Image Acquisition, Feature Extraction, Model Creation and User Interface.

_Image Acquisition:_ The system uses OpenCV to capture video from the user's camera and extract 300 frames for each emotion to create a dataset. The user has to give 300 frames for each emotion for creating the dataset.

_Feature Extraction:_ The system uses Mediapipe to identify the facial landmarks on the captured frames. Holistic Solutions are applied to gather all the landmarks position and convert them into holistic values. This process is applied to every 300 frames and the results are stored in an npy file for each emotion.

_Model Creation:_ The npy files containing the facial feature values are used by a dense layer in Keras to classify the input image into different classes. The neural network is created with Keras and TensorFlow as the backend. The network is trained for 50 epochs to improve accuracy. The trained model is stored in a model.h5 file for faster access.

_User Interface_: The system uses Tkinter for the user interface. There are four buttons: Data collection, Train, Run and Close. Data Collection allows the user to input an emotion name and capture frames, Train trains the model with all the emotional data files in the folder, Run captures the user's image and analyzes it to predict the emotion and plays music accordingly, Close terminates all the project windows.





***Required Libraries:***
+mediapipe
+Numpy
+Pandas
+OpenCV (CV2)
+Tkinter
+Tensorflow
+Keras
+pygame

***Just run the UI.****

