from flask import Flask, render_template, abort

app = Flask(__name__)

PRODUCTS = {
    'iphone': {
        'name': 'Iphone 5S',
        'category': 'Phones',
        'price': 699
    },
    'galaxy': {
        'name': 'Samsung',
        'category': 'Phones',
        'price': 599
    },
    'LG': {
        'name': 'LG',
        'category': 'Phones',
        'price': 499
    }
}


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/products/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run()
