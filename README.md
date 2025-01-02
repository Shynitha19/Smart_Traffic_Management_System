# 🚦ANPR and ATCC for Smart Traffic Management

## Project Overview

This project aims to develop an intelligent traffic management system using Automatic Number Plate Recognition (ANPR) and Automatic Traffic Classification and Control (ATCC). By leveraging Deep Learning and Object Detection techniques, the system will automate traffic monitoring and control in smart city environments. ANPR will detect and recognize vehicle license plates, while ATCC will classify different types of traffic. The system will improve traffic flow, reduce congestion, and enhance road safety.

## Key features

- Automatic Number Plate Recognition (ANPR)
- Traffic classification and control (ATCC)
- Data interpolation for accurate detection and visualization
- Video output with annotated traffic information

## Project structure of github repo:

```
├── CV_Basics/                # Computer vision and OCR learning materials
├── model/                    # Tracking code
├── object_tracker/           # Main detection and vehicle tracking code
├── output/                   # Interpolated CSV files for visualization
├── result/                   # Generated output videos
├── testing/                  # Project testing files
├── utils/                    # Video processing
├── .gitignore                # Git ignore rules
├── add_missing_data.py       # Data interpolation script
├── main.py                   # Main execution file
├── requirements.txt          # Project dependencies
└── visualize.py              # Video visualization script
```

## Workflow

- Execute main.py to perform initial vehicle detection and generate CSV file in results/ directory
- Run add_missing_data.py to perform data interpolation and generate enhanced CSV file in Interpolated_results/ directory
- Run visualize.py to create visualization video using interpolated data, saved in output_videos/ directory

## Setup and Installation

1.Clone the repository:
  ```bash
  git clone https://github.com/Shynitha19/Smart_Traffic_Management_System
  cd ANPR-and-ATCC-for-Smart-Traffic-Management
  ```

2.Create and activate virtual environment (recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3.Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Running the Project

1.Replace the path to your input video and your desired output directory.

2.Run the main detection:
  ```bash
  python main.py
  ```

3.Perform data interpolation:
  ```bash
  python add_missing_data.py
  ```

4.Generate visualization:
  ```bash
  python visualize.py
  ```

## 📄License

ANPR and ATCC for Smart Traffic Management is released under the [MIT License](License), allowing you to freely use, modify, and distribute the project.