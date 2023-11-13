import itertools
import time
import tqdm

def generate_all_possible_4_digit_numeric_passwords():
  """Generates all possible 4 digit numeric passwords.

  Returns:
    A list of all possible 4 digit numeric passwords, as strings.
  """

  # Create a list of all possible characters in the password.
  digits = [str(i) for i in range(10)]

  # Start a timer.
  start_time = time.time()

  # Create a progress bar.
  progress = tqdm.tqdm(total=len(digits)**10)

  # Use the itertools.product() function to generate all possible combinations
  # of 4 characters from the list of digits.
  passwords = itertools.product(digits, repeat=8)

  # Convert the combinations to strings and return them.
  for password in passwords:
    progress.update(1)
    yield "".join(password)

  # Stop the timer and print the elapsed time.
  end_time = time.time()
  elapsed_time = end_time - start_time
  print("Elapsed time: {} seconds".format(elapsed_time))

  # Close the progress bar.
  progress.close()

def save_to_txt(passwords, filename):
  """Saves the list of passwords to a text file.

  Args:
    passwords: A list of passwords, as strings.
    filename: The name of the text file to save the passwords to.
  """

  with open(filename, "w") as f:
    for password in passwords:
      f.write(password + "\n")

if __name__ == "__main__":
  # Generate all possible 4 digit numeric passwords.
  passwords = generate_all_possible_4_digit_numeric_passwords()

  # Save the passwords to a text file.
  save_to_txt(passwords, "8_digit_numeric_passwords.txt")
