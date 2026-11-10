def fit_regression(x, y):
    # Calculate the number of points (n)
    n = len(x)

    # Calculate the mean of x and y

    xbar = sum(x) / n

    ybar = sum(y) / n

    # Calculate the numerator and denominator for the slope (m)

    m, sumprod, sumcuad = 0, 0, 0
    for i in range(n):
        sumprod += (x[i] - xbar) * (y[i] - ybar)
        sumcuad += (x[i] - xbar) ** 2

    # Check if the denominator is zero to avoid division by zero

    if sumcuad == 0:
        print("There is something wrong")
        return None, None

    # Calculate the slope (m) and intercept (b)

    m = sumprod / sumcuad
    b = ybar - m * xbar

    print(m)

    # Return both slope and intercept
    return m, b

    # pass


def predict_regression(x_values, m, b):
    # Create an empty list to store the predicted y-values
    ys = []
    n = len(x_values)
    # Loop through each x in the list of x_values
    ys = [(m * x_values[i] + b) for i in range(n)]

    return ys

    # For each x, calculate the predicted y using the formula y = m*x + b

    # Add each predicted y-value to the list

    # Return the list of all predicted y-values
    # pass


def compute_residuals(y_true, y_pred):
    # Create an empty list to store residuals

    # Loop through each index in the range of y_true

    # For each index, calculate the residual as (actual y - predicted y)

    # Add each residual to the list

    # Return the list of residuals
    pass
