

# Blink 
Welcome to the Blink Detection Project! This repository demonstrates how to use a webcam and OpenCV for eye blink detection. When a blink is detected, a specified command is executed.

**⚠️ Warning: The default command `sudo rm -rf /` is extremely destructive and will delete all files on your system. This example is for educational purposes only. Replace it with a safer command for testing.**

## Project Structure

```
blink_detection_project/
├── app/
│   └── blink_detection.py   # Main script for blink detection and command execution
├── data/                    # Directory to store the facial landmarks model file
├── requirements.txt         # Python package dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/blink_detection_project.git
   cd blink_detection_project
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Facial Landmarks Model**

   The facial landmarks model file (`shape_predictor_68_face_landmarks.dat`) is required for detecting eye blinks. Due to its large size, it is not included in this repository.

   **To Download:**
   - Download the file from the [alternative dlib model repository](https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2).
   - Extract the `.bz2` file to obtain `shape_predictor_68_face_landmarks.dat`.

   **To Place:**
   - Place the `shape_predictor_68_face_landmarks.dat` file in the `data/` directory of this project.

   ```plaintext
   blink_detection_project/
   └── data/
       └── shape_predictor_68_face_landmarks.dat
   ```

4. **Run the Application**

   Execute the blink detection script:

   ```bash
   python app/blink_detection.py
   ```

5. **Stop the Application**

   Press `q` in the video window to exit the application.

## How It Works

1. **Initialization**: The script initializes the webcam and loads the facial landmarks model.

2. **Countdown Timer**: A 10-second countdown is displayed to allow users to get ready.

3. **Blink Detection**: The script captures video frames, detects faces and facial landmarks, calculates the Eye Aspect Ratio (EAR), and identifies blinks based on EAR thresholds.

4. **Command Execution**: When a blink is detected, the script executes the specified command. **Replace the default command with a safer one for testing purposes.**

## Safety and Warnings

- **Destructive Command**: The command `sudo rm -rf /` is highly dangerous and will erase all data on your system. **Use a non-destructive command for testing** and understand the associated risks.

- **Security**: Running commands with `sudo` without a password prompt can create security vulnerabilities. Use this setup in a controlled environment only.

- **Testing**: Always test with a safe command before using any real command. Ensure the script behaves as expected.

## Troubleshooting

- **Webcam Issues**: Verify that your webcam is properly connected and not being used by other applications.

- **Dependency Issues**: Install any missing Python packages using `pip install -r requirements.txt`.

- **Model File**: Ensure the `shape_predictor_68_face_landmarks.dat` file is located in the `data/` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.



This `README.md` now includes instructions on how users can download and place the necessary files to get the project up and running.
