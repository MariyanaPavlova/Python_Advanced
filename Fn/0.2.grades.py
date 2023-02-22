def output_grade(gr):
    if 2.00 <= gr <= 2.99:
        return "Fail"
    elif 3.00 <= gr <= 3.49:
        return "Poor"
    elif 3.50 <= gr <= 4.49:
        return "Good"
    elif 4.50 <= gr <= 5.49:
        return "Very Good"
    elif 5.50 <= gr <= 6.00:
        return "Excellent"


grade = float(input())
print(output_grade(grade))