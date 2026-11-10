# Define a function to save regression results to a text file
def save_results(filename, lines):
    # Write the slope, intercept, and predictions to the file, each on a separate line.
    with open(filename, "w") as file:
        file.writelines(lines)
    print(f"Data is saved in {filename}")


# Define a function to read the saved regression results from a text file
def read_results(filename):
    # Read the file and return all of its contents.
    with open(filename, "r") as file:
        content = file.read()

    return content


# OPTIONAL CHALLENGE: summarize a list of numeric values
def data_summary(values):
    # Do the computations with simple native Python computations

    # Return all summary results in a dictionary
    pass
