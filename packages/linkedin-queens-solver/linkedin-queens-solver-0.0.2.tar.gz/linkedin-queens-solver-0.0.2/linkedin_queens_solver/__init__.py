"""Module to solve the Linkedin Queens daily challenge"""

import cv2
import numpy
import numpy as np
from typing import Any, Dict, List, Tuple

colors_covered: Dict[str, Any] = {}

class Utils():
	"""Class for handling utility functions"""
	def display_board(self, board: List[List[int]]) -> None:
		"""Display the board on console.

		Args:
			board (List[List[int]]): board to be displayed
		"""
		rows = len(board)
		for i in range(rows):
			print(board[i])

	def show_image(self, image: numpy.ndarray) -> None:
		"""Display the image.

		Args:
			image (numpy.ndarray): input image
		"""
		cv2.imshow("abc", image)
		cv2.waitKey(0)

	def detect_color_board(self, image: numpy.ndarray) -> Tuple[List[List[int]], List[List[int]]]:
		"""Detect the color board from the image and convert to a matrix.

		Args:
			image (numpy.ndarray): input image.

		Raises:
			AssertionError: Raise an error if grid not found

		Returns:
			Tuple[List[List[int]], List[List[int]]]: board as a simplex matrix and tile centers.
		"""
		gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		# threshold the image
		_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
		
		# find contours and compute the area of contours
		contours, _ = cv2.findContours(thresh_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
		contour_areas = [cv2.contourArea(cnt) for cnt in contours]
		
		# remove spurious contours
		med = np.median(contour_areas)
		
		retries = [5, 4, 3, 2]
		grid_found = False
		for attempt in retries:
			lower_contour_thresh, higher_contour_thresh = med - (med//attempt), med + (med // attempt)

			filtered_contours = [contours[i] for i, area in enumerate(contour_areas) if area > lower_contour_thresh and \
							area < higher_contour_thresh]
			grid_size = np.sqrt(len(filtered_contours))
			if grid_size == np.floor(grid_size):
				grid_found = True
				break
		if not grid_found:
			raise AssertionError("Could not find grid")
		
		grid_size = int(grid_size)

		contour_moments = [cv2.moments(cnt) for cnt in filtered_contours]
		contours_centers = [(int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) for M in contour_moments]
		
		xmin = min([elem[0] for elem in contours_centers])
		xmax = max([elem[0] for elem in contours_centers])
		ymin = min([elem[1] for elem in contours_centers])
		ymax = max([elem[1] for elem in contours_centers])

		board = [[0 for i in range(grid_size)] for j in range(grid_size)]
		
		color_idx = 1
		color_map = {}
		# arrange the contour centers so that we index the contours correctly
		rearranged_tile_centers = [[None for i in range(grid_size)] for j in range(grid_size)]
		ii, jj = 0, 0
		for i in np.linspace(xmin, xmax, int(grid_size)):
			for j in np.linspace(ymin, ymax, int(grid_size)):
				rearranged_tile_centers[ii][jj] = (i, j)
				color = image[int(i)][int(j)]
				color_hash = str(color)
				if color_hash not in color_map:
					color_map[color_hash] = color_idx
					color_idx += 1

				board[ii][jj] = color_map[color_hash]
				jj += 1
			jj = 0
			ii += 1
		return board, rearranged_tile_centers

class Solver():
	"""Solver class to solve the challenge."""

	def __init__(self, visualize = True):
		"""default constructor

		Args:
			visualize (bool, optional): flag to control wheter to visualize the result or not. Defaults to True.
		"""
		self.visualize = visualize

	@staticmethod
	def diag_dist(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> int:
		"""Compute the diagonal distance between 2 points.

		Args:
			point_1 (_type_): coordinates of point 1
			point_2 (_type_): coordinates of point 2
		"""
		return(max(abs(point_2[0] - point_1[0]), abs(point_2[1] - point_1[1])))

	def can_place_queen(self, color_board:List[List[int]],
					 		  board:List[List[int]], row: int, col: int) -> bool:
		"""Check if we can place the queen at the current position.

		Args:
			color_board (List[List[int]]): color board matrix
			board (List[List[int]]): output board matrix
			row (int): current row
			col (int): current col

		Returns:
			bool: return true if we can place the queen at the current position.
		"""
		# check if current color is already covered
		if color_board[row][col] in colors_covered:
			return False
		# check all columns in current row --> Left wards
		for j in range(col-1, -1, -1):
			if board[row][j] == 1:
				return False
		# check all rows in current column --> Up wards
		for i in range(row-1, -1, -1):
			if board[i][col] == 1:
				return False
		
		# check all diagonal elements --> NorthWest wards
		for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
			if self.diag_dist((row, col), (i, j)) > 1:
				continue
			if board[i][j] == 1:
				return False
		# check all diagonal elements --> NorthWest wards
		for i, j in zip(range(row+1, len(board)), range(col-1, -1, -1)):
			if self.diag_dist((row, col), (i, j)) > 1:
				continue
			if board[i][j] == 1:
				return False
		return True

	def backtrack(self, color_board: List[List[int]], board: List[List[int]], col: int) -> bool:
		"""Run backtracking.

		Args:
			color_board (List[List[int]]): color board matrix
			board (List[List[int]]): output board matrix
			col (int): column idx

		Returns:
			bool: return True if a valid position is found for current column
		"""
		rows, cols = len(board), len(board[0])
		if col == cols:
			return True

		for i in range(rows):
			if self.can_place_queen(color_board, board, i, col):
				board[i][col] = 1
				colors_covered[color_board[i][col]] = True
				if self.backtrack(color_board, board, col+1):
					return True
				board[i][col] = 0
				del colors_covered[color_board[i][col]]
		return False

	def solve(self, image: numpy.ndarray) -> None:
		"""solver wrapper function

		Args:
			color_board (List[List[int]]): color board matrix
			board (List[List[int]]): output board matrix
		"""
		utils_obj = Utils()
		color_board, tile_centers = utils_obj.detect_color_board(image)
		N = len(color_board)
		board = [[0 for i in range(N)] for j in range(N)]
		
		self.backtrack(color_board, board, 0)
		print("********** Result *********")
		utils_obj.display_board(board)
		print("***************************")
		
		if self.visualize:
			output_image = image.copy()
			idx_1d = 0
			for i in range(N):
				for j in range(N):
					if board[i][j] == 1:
						cv2.circle(output_image, (int(tile_centers[i][j][1]), int(tile_centers[i][j][0])), 5, (0, 0, 0), -1)
					idx_1d += 1
			utils_obj.show_image(output_image)

def solve_queens(image: numpy.ndarray, visualize=True):
	solver_obj = Solver(visualize=visualize)
	solver_obj.solve(image)
