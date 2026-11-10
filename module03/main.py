from mini_regression.model import fit_regression, predict_regression
from mini_regression.utils import save_results, read_results


def main():
    # Initialize data
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 55]

    # Print X and Y to check the data

    print("X=", X)
    print("Y=", Y)

    m, b = fit_regression(X, Y)

    print(f"the function is {m}X + {b}")

    # Call the fit_regression function
    # and store the returned slope (m) and intercept (b)

    # Call the predict_regression function
    # and store the returned list of predicted y-values

    regre = predict_regression(X, m, b)

    print(regre)

    # Save the regression results to a text file using save_results
    # Pass the filename, slope, intercept, and predicted y-values
    lines = [
        f"Slope={m}\n",
        f"Intercept={b}\n",
        f"Y predicted values={regre}\n",
    ]
    filename = "module03.txt"
    save_results(filename, lines)

    # Read the saved results from the text file using read_results
    # Store the returned file contents and print them
    linesread = read_results(filename)

    print(f"lines from {filename}")
    print(linesread)


# OPTIONAL CHALLENGE: Call the compute_residuals function
# and store the returned list of residuals


# OPTIONAL CHALLENGE: Call data_summary to summarize the numeric data


if __name__ == "__main__":
    main()
