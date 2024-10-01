import random
from IPython.display import display, HTML
import ipywidgets as widgets

exercises = [
	{
		"exercise": "Exercise 1: Implement a function to reverse a string.",
		"solution": "Solution: def reverse_string(s): return s[::-1]"
	},
	{
		"exercise": "Exercise 2: Write a function to check if a number is prime.",
		"solution": "Solution: def is_prime(n): return all(n % i != 0 for i in range(2, int(n**0.5) + 1))"
	},
	{
		"exercise": "Exercise 3: Create a function to sort a list of numbers.",
		"solution": "Solution: def sort_numbers(lst): return sorted(lst)"
	},
	# Add more exercises and solutions here
]

def display_random_exercise():
	exercise = random.choice(exercises)
	exercise_text = exercise["exercise"]
	solution_text = exercise["solution"]

	solution_button = widgets.Button(description="Show Solution")
	solution_output = widgets.Output()

	def on_button_click(b):
		with solution_output:
			solution_output.clear_output()
			display(HTML(f"<pre>{solution_text}</pre>"))

	solution_button.on_click(on_button_click)

	display(HTML(f"<p>{exercise_text}</p>"))
	display(solution_button)
	display(solution_output)