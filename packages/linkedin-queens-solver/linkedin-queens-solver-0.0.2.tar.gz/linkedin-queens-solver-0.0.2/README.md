# Linkedin_Queens_challenge
Solve the Linkedin daily challenge "Queens"

# Usage
Step 1- Take a snapshot of the daily queens problem board, and save this image

Step 2- Run the following code:
```
pip install linkedin-queens-solver

import linkedin_queens_solver
import cv2
image = cv2.imread("<path to the image where the board is saved>")
linkedin_queens_solver.solve_queens(image, visualize=True)
```