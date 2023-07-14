# Corn Disease Recognition

This project is able to determine if a corn plant is infected with common rust, blight, or grey leaf spot. Additionally, the project can detect healthy corn plants.

![cr](https://github.com/oanaeser/Corn_Disease_Recognition/assets/139392175/226205cd-9a75-4be9-8d6e-0ea3f93fdca2)
![gls](https://github.com/oanaeser/Corn_Disease_Recognition/assets/139392175/9c445c0d-11f5-4d52-b3e6-e88c6ff9c38a)
![healthy](https://github.com/oanaeser/Corn_Disease_Recognition/assets/139392175/b1ad73c7-d614-46f2-b4cd-3b02095914ac)

## The Algorithm

This project run on a resnet model that has been retrained on four sets of data. The first set contains images of healthy corn plants. The remaining sets contain images with corn plants that have been infected with blight, common rust, and grey leaf spot. After the model was trained, I exported it in ONNX format. The program uses imagenet.py to determine if the corn plant is healthy or infected with one of the diseases.

The datasets I used can be found here: [Corn or Maize Leaf Disease Dataset](https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset) and [Maize_in_Field_Dataset](https://www.kaggle.com/datasets/b7d58bc6d1a9d63d75ee2bfac914658722887c09affeb801063edfcae2426e42)

## Running the project

### Setup

1. Download the [jetson-inference container](https://github.com/dusty-nv/jetson-inference) from github and load it onto a jetson-nano.
2. Navigate to `jetson-inference/python/training/classification/data`
3. Create a new dircetory called "corn_disease_detection"
4. Within the "corn_disease_detection" directory create three more directories called "train", "test", and "val"
5. Create a file called "labels.txt" within the "corn_disease_detection directory" and in the following order write: blight, common_rust, grey_leaf_spot, and healthy (each on its own line)
6. Create four directories called "blight", "common_rust", "grey_leaf_spot", and "healthy" within the "train", "test", and "val" directories
7. Download the [Corn or Maize Leaf Disease Dataset](https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset)
8. Move around 80% of the images in the "Blight" folder in the download to the jetson-nano directory `jetson-inference/python/training/classification/data/corn_disease_detection/train/blight`
9. Move around 10% of the images in the "Blight" folder in the download to the jetson-nano directory `jetson-inference/python/training/classification/data/corn_disease_detection/test/blight`
10. Move around 10% of the images in the "Blight" folder in the download to the jetson-nano directory `jetson-inference/python/training/classification/data/corn_disease_detection/val/blight`
11. Repet steps 8-10 with the "Common_Rust", "Grey_Leaf_Spot", and "Healthy" folders in the download (make sure to change the final jetson directory to "common_rust", "grey_leaf_spot", and "healthy" respectivley)
12. Download the [Maize_in_Field_Dataset](https://www.kaggle.com/datasets/b7d58bc6d1a9d63d75ee2bfac914658722887c09affeb801063edfcae2426e42)
13. Create a new folder on your computer called "sorted"
14. Within "sorted" create more folders called "cr", "gls", "healthy", "nclb", "other", "pls", and "sr"
15. Within the downloaded "Kaggle Dataset" folder create a python file called "csv_sorter.py"
16. Write the following code into the "csv_sorter.py" file:
![csv_code](https://github.com/oanaeser/Corn_Disease_Recognition/assets/139392175/e5e6bff4-8fd9-40fe-992f-a72d46d3e7f0)
(The file paths in workingDirectory and originFolder will change depending on where your folders are located)

17. Run "csv_sorter.py"
18. Once the code has finished running the images should have been sorted in the the "sorted" folder
19. Move files from the "gls" folder to `jetson-inference/python/training/classification/data/corn_disease_detection/train/grey_leaf_spot` until it has around 1,000 images
20. Move files from the "gls" folder to `jetson-inference/python/training/classification/data/corn_disease_detection/test/grey_leaf_spot` until it has around 125 images
21. Move files from the "gls" folder to `jetson-inference/python/training/classification/data/corn_disease_detection/val/grey_leaf_spot` until it has around 125 images

### Training

1. Change directories to `jetson-inference`
2. Run the `./docker/run.sh` command in the terminal
3. In the docker change directories to `jetson-inference/python/training/classification`
4. Run `python3 train.py --model-dir=models/corn_disease_detector data/corn_disease_detector --epochs=150` to start training the model (you can run it for how ever many epochs you'd like)
5. Once the model has finished training run the command `python3 onnx_export.py --model-dir=models/corn_disease_detector` to export the model
6. Exit the docker by pressing  Ctrl + D or by typing `exit`

### Running a Single Image

1. Change directories to `jetson-inference/python/training/classification`
2. Run the command: `NET=models/corn_disease_detector`
3. Run the command: `DATASET=data/corn_disease_detector`
4. Run the command: `imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/common_rust/Corn_Common_Rust_1278.jpg output.jpg`

   (In order to test an image it must have any spaces removed)
6. There should now be a file in the classification directory called output.jpg (or whatever you named the output file)
7. Open the file to see what the computer has identified the image as

View a [video demonstration](https://youtu.be/5fjp-S2D9ck) here

Notes:

In step four "Corn_Common_Rust_1278.jpg" can be replaced with any image name in the currently used directory

In step four "common_rust" can be replaced with "healthy", "grey_leaf_spot", or "blight" to test images in their directories

### Running a Series of Images

1. Change directories to `jetson-inference/python/training/classification`
2. Run the command: `NET=models/corn_disease_detector`
3. Run the command: `DATASET=data/corn_disease_detector`
4. Run the command: `mkdir $DATASET/test_output_blight $DATASET/test_output_common_rust $DATASET/test_output_grey_leaf_spot $DATASET/test_output_healthy`
5. Now run the command: `imagenet --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/./labels.txt $DATASET/test/healthy $DATASET/test_output_healthy`
6. The "test_output_healthy" directory should now be full of images
7. Display the files to find out what the computer thinks they are

View a [video demonstration](https://youtu.be/hCPVmYaP7v0) here

Notes:

In step five "healthy can be replaced with any other directory in "test" to test the images in that directory.

In step five "test_output_healthy" can be replaced with any other directory to place the output images there instead.
