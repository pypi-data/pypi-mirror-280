# gradescalculator/main.py

import argparse

def calculate_grades(grades):
    # Calculate the total weighted sum of the grades
    total_weighted_sum = sum(item["weight"] * item["grade"] for item in grades.values())

    # Calculate the total weight
    total_weight = sum(item["weight"] for item in grades.values())

    # Calculate the overall grade
    overall_grade = total_weighted_sum / total_weight

    # Round the overall grade to the nearest 0.01 and the nearest 0.5
    precise_overall_grade = round(overall_grade * 100) / 100
    rounded_overall_grade = round(overall_grade * 2) / 2

    return precise_overall_grade, rounded_overall_grade

def main():
    parser = argparse.ArgumentParser(description="Calcule la note globale à partir des notes.")
    parser.add_argument('grades', metavar='N', type=float, nargs='+', help='Liste des notes et de leurs poids sous la forme: note1 poids1 note2 poids2 ...')
    args = parser.parse_args()

    # Convert the grades to a dictionary
    grades = {}
    for i in range(0, len(args.grades), 2):
        grades[f'grade {i//2 + 1}'] = {"weight": args.grades[i+1], "grade": args.grades[i]}

    precise_grade, rounded_grade = calculate_grades(grades)
    
    print(f"Precise Overall Grade (rounded to the nearest 0.01): {precise_grade}")
    print(f"Rounded Overall Grade (rounded to the nearest 0.5): {rounded_grade}")

if __name__ == '__main__':
    main()
