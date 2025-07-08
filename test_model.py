import torch
import subprocess
import os

# Test with default model
def test_model():
    cmd = [
        'python', 'detect.py',
        '--weights', 'yolov5s.pt',  # or your model path
        '--source', 'data/images/bus.jpg',
        '--save-txt',  # saves detection results as text
        '--save-conf'  # saves confidence scores
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", result.returncode)
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    
    # Show where results are saved
    print("\nResults saved to: runs/detect/exp/")

if __name__ == "__main__":
    test_model()