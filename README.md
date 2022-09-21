# Milling-Cutter-Condition-Monitoring-using-Macine-Learning

GUI Application written in Python that allows user to,
1. Visualize Training Dataset
2. Clean Dataset
3. Train the Machine Learning Framework to identify milling cutter faults and display accuracy
4. Extract features from a test signal
5. Classify Test signal into pre trained wear catergories, 
6. Indicate if the test signal is not part of the same distribution from which training data is assumed to be derieved from.

The application files can be found in the directory named 'Source Code', with 'GUI_Backend.py' being the main source file.

For detailed working, the project report has also been uploaded.

Along with this, the dataset used is also provided along with utilities to split the dataset and extract statistical features.
Each file in the primary Dataset consists of an array of tool accelerations corresponding to the particular wear conditions. 

Wear Condition Key: (Guide to Filenames of Dataset)
'111': 'Healthy'
'112': 'Flank Wear'
'113': 'Nose Wear'
'114': 'Notch Wear' 
'115': 'Crater Wear'
'116': 'Edge Fracture'
'117': 'Builtup Edge'
'118': 'All Wear'

How to Run:
1. Run 'GUI_Backend.py' from the directory 'Source Code'
2. Use the precompiled executable 'Milling Cutter Condition Monitor.exe'

Notes:
Clone the repo and open the folder in your prefered editor/IDE for proper functioning of filepaths.
