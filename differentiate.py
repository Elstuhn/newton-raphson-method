def differentiate(equation : str):
    """
    equation will be a polynomial e.g. 3x^2+4x+2 or 3/4x^3+2x^2+5x+1/2
    equation will have to be simplified e.g. 4x^2+3x+2 instead of 8x^5/2x^3+3x^2/x+2 and 4x^2+3x+2 instead of 6x^2-2x^2+8x-5x+2
    """
    flag = False
    result = ""
    indflag = False
    equation = equation.split("x")

    for i in equation:
        if i=="":
            continue
        if i[1:].isdigit() and flag:
            if i[0] == "^":
                evaluated = str(eval(f"{coeff}*{i[1:ind]}"))+f"x^{int(i[1:ind])-1}" if (int(i[1:ind])-2) else str(eval(f"{coeff}*{i[1:ind]}"))+"x"
                if i != equation[1] and evaluated[0] != "-":
                    evaluated = "+" + evaluated
                result += evaluated
            else:
                result += coeff if coeff[0] == "-" else "+" + coeff
            
        elif not flag:
            coeff = i
            flag = True 
        else:
            try:
                ind = i.index("+")
                indflag = True
            except:
                ind = i.index("-")
            evaluated = str(eval(f"{coeff}*{i[1:ind]}"))+f"x^{int(i[1:ind])-1}" if (int(i[1:ind])-2) else str(eval(f"{coeff}*{i[1:ind]}"))+"x"
            if i != equation[1] and evaluated[0] != "-":
                evaluated = "+" + evaluated
            result+=evaluated
            if not len(i[ind:])-1:
                coeff = eval(f"0+{i[ind:]}1")
            else:
                coeff = i[ind+1:] if indflag else i[ind:]
    
    return result

                
# 8x^5+4x^4+2x^3+8x^2+2x+1
# [8, ^5+4, ^4+2, ^3+8, ^2+2, +1]
# 7x^3 + 8x^2
# [7, ^3+8, ^2]