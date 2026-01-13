from django.shortcuts import render

def calculator(request):
    result = ""

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operator = request.POST.get("operator")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

    return render(request, "calculator.html", {"result": result})

