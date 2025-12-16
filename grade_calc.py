def get_grade(marks):
    """
    Function to determine grade and encouraging message based on marks.
    """
    if marks >= 90:
        return "A", "Excellent work! Keep it up! "
    elif marks >= 80:
        return "B", "Great job! You're doing really well! "
    elif marks >= 70:
        return "C", "Good effort! Keep pushing forward! "
    elif marks >= 60:
        return "D", "You're getting there! Stay focused! "
    else:
        return "F", "Don't give up! Learn from mistakes and try again! "


# Main program
while True:
    try:
        marks_input = input("Enter student marks (0–100): ")
        marks = int(marks_input)

        # Check valid range
        if marks < 0 or marks > 100:
            print(" Invalid input. Marks must be between 0 and 100. Try again.")
            continue

        # Get grade and message
        grade, message = get_grade(marks)

        # Show result
        print(f"\n Marks: {marks}")
        print(f" Grade: {grade}")
        print(f" Encouragement: {message}\n")
        break

    except ValueError:
        print(" Please enter a valid number (0–100). Try again.")
