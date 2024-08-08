# Video Frame Extraction and Feature Analysis

This project provides tools to extract frames from a video file and perform feature extraction using a pre-trained VGG16 model. The project is divided into two main scripts:

1. `extract_frames.py`: Extracts frames from a specified interval of a video file with detailed progress tracking.
2. `feature_extraction.py`: Loads images and extracts features in batches using a pre-trained VGG16 model.

## Requirements

To run these scripts, you need the following packages installed:

- `opencv-python`
- `numpy`
- `ipython`
- `tqdm`
- `tensorflow`
- `scikit-learn`

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

Setting Up Environment Variables
Make sure to set the VIDEO_PATH environment variable to the path of your video file.


## Project Structure

```
├── .env                    # Environment variable file (optional)
├── README.md               # Project documentation
├── requirements.txt        # Required packages
├── extract_frames.py       # Script for extracting frames from video
├── feature_extraction.py   # Script for extracting features from images
└── extracted_data          # Folder where extracted frames will be ```