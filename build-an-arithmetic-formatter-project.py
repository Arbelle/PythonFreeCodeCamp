def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem should have two numbers and one operator."
        
        num1, op, num2 = parts
        
        
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        
        if show_answers:
            if op == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
        
        
        width = max(len(num1), len(num2)) + 2
        
        
        top_lines.append(num1.rjust(width))
        bottom_lines.append(op + ' ' + num2.rjust(width - 2))
        dash_lines.append('-' * width)
        
        if show_answers:
            answer_lines.append(answer.rjust(width))
    
    
    arranged_problems = "    ".join(top_lines) + "\n"
    arranged_problems += "    ".join(bottom_lines) + "\n"
    arranged_problems += "    ".join(dash_lines)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_lines)
    
    return arranged_problems


