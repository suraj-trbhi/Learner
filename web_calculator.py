from flask import Flask, render_template, request, jsonify
import math
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def index():
    """Serve the calculator web interface"""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API endpoint for calculator operations"""
    try:
        data = request.get_json()
        operation = data.get('operation')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0)) if data.get('b') is not None else None
        
        result = None
        
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        elif operation == 'power':
            result = calc.power(a, b)
        elif operation == 'square_root':
            result = calc.square_root(a)
        elif operation == 'percentage':
            result = calc.percentage(a, b)
        elif operation == 'factorial':
            result = calc.factorial(int(a))
        elif operation == 'sin':
            result = calc.sin(a)
        elif operation == 'cos':
            result = calc.cos(a)
        elif operation == 'tan':
            result = calc.tan(a)
        elif operation == 'log':
            if b is not None:
                result = calc.log(a, b)
            else:
                result = calc.log(a)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Calculation error: {str(e)}'}), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'calculator'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
