def divide_scores(total_score, number_of_tests):
    try:
        average = total_score / number_of_tests
        return f"Average score is: {average}"
    except ZeroDivisionError:
        return "Error: cannot divide by zero tests"
    except TypeError:
        return "Error: invalid input type"

print(divide_scores(90, 3))
print(divide_scores(90, 0))
print(divide_scores(90, "three"))