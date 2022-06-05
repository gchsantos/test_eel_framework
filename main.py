import eel

eel.init('app')

@eel.expose
def calculate(operation: str, n1: float, n2: float) -> float:
    n1 = float(n1)
    n2 = float(n2)
    try:
        if operation == 'sum':
            return n1+n2
        elif operation == 'sub':
            return n1-n2
        elif operation == 'mult':
            return n1*n2
        elif operation == 'div':
            return n1/n2
        return 0
    except:
        return 0

eel.js_test_func()
eel.start('index.html', size=(800, 600))
