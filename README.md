# ship-route-optimization
Ship route optimization using two kinds of data to integrate and provide better results.
Work folw for this project is attached to this for better understanding the flow

![image](https://github.com/user-attachments/assets/0ad96eee-4a54-4406-b688-a150c5f5c330)

Person detection along with Gender Classification (Protecting Women from safety threats) 

Why gender classification for women safety?
Detecting the person on the images with features of facial, body characteristics and their gender.
This technology is essential while enhancing surveillance systems, especially in environments prone to safety risks.

Why crowd or not is matter more?
If the place is crowded then it is not quite safer for women to say longer.
By recognizing individuals and identifying possible threats, the system can serve as an early-warning mechanism to ensure prompt action is taken in potentially dangerous scenarios.

Traditional person detection methods relied on handcrafted features such as Histograms of Oriented Gradients (HOG) or Support Vector Machines (SVM), which lacked scalability and robustness for real-world applications. 
Recent advancements in deep learning have paved the way for Convolutional Neural Networks (CNNs) like ResNet and EfficientNet, which have significantly improved accuracy in detecting people. 
These models use multiple layers of learned features, allowing them to generalize well to a variety of environments and settings.

Literature Survey:
Person Detection: The use of object detection models such as YOLO (You Only Look Once), Faster R-CNN, and SSD (Single Shot Multibox Detector) has improved the accuracy and speed of person detection. These models can identify and localize people in crowded or complex environments.
Gender Classification: Gender classification techniques often rely on facial recognition systems. Convolutional Neural Networks (CNNs) have been widely used for this purpose. VGG-16, ResNet, and MobileNet architectures are commonly employed in gender classification models.
Applications in Women’s Safety: Prior studies have explored the use of surveillance systems in improving women’s safety. Some systems include panic buttons and location-based tracking devices. However, a more proactive solution integrating gender identification could be key to preventing incidents before they escalate.

Methodology:
Data Collection: 
A dataset of images containing individuals of different genders will be collected. 
Data source: Gender Classification dataset, COCO dataset, CrowdHuman dataset
Preprocessing: 
Normalizing pixel values
Performing data augmentation
Facial features extracted to improve the accuracy of gender classification.
Model Selection:
Person Detection: OpenCV's Haar Cascade Classifier used to detect and annotate the person with faces.
Gender Classification: Using CNN, OpenCV’s DNN(Pretrained),EfficientNet

Integration: The person detection and gender classification modules will be integrated to identify the person and gender at the same time.
Safety Alert System: Based on input images it detecting a crowd or not and make sure it is safe or not safe to be there.
Evaluation:
          Mean Average Precision (mAP) for object detection tasks.
          Mean Squared Error(mse) for gender detection 
EfficientNetB Architecture:
![image](https://github.com/user-attachments/assets/02ac0621-e51f-434f-8d78-5f5e93449028)


Conclusion:
EfficientNet: The model to perform well used early stopping and regularization and bring the accuracy for the test dataset 94%.
