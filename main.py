from flask import Flask, render_template
import datetime

app = Flask(__name__)

email = 'info@mixity.ru'.upper()
current_year = datetime.datetime.now().year


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', email=email, current_year=current_year)


@app.route('/glue/glue')
def glue():
    return render_template('/glue/glue.html', email=email, current_year=current_year, title='МИКСИТИ - клеи для плитки.')


@app.route('/grout/grout')
def grout():
    return render_template('/grout/grout.html', email=email, current_year=current_year, title='МИКСИТИ - затирки.')


@app.route('/plaster/plaster')
def plaster():
    return render_template('/plaster/plaster.html', email=email, current_year=current_year, title='МИКСИТИ - штукатурки.')


@app.route('/putty/putty')
def putty():
    return render_template('/putty/putty.html', email=email, current_year=current_year, title='МИКСИТИ - шпаклевки.')


@app.route('/block/block')
def block():
    return render_template('/block/block.html', email=email, current_year=current_year, title='МИКСИТИ - кладочные и монтажные.')


@app.route('/leveler/leveler')
def leveler():
    return render_template('/leveler/leveler.html', email=email, current_year=current_year, title='МИКСИТИ - ровнители для пола.')


@app.route('/ricks/ricks')
def ricks():
    return render_template('/ricks/ricks.html', email=email, current_year=current_year, title='RICKS - сухие строительные смеси.')


@app.route('/hydro/hydro')
def hydro():
    return render_template('/hydro/hydro.html', email=email, current_year=current_year, title='МИКСИТИ - гидроизоляция.')


@app.route('/general/products')
def products():
    return render_template('/general/products.html', email=email, current_year=current_year, title='МИКСИТИ - продукция.')


@app.route('/general/buy')
def buy():
    return render_template('/general/buy.html', email=email, current_year=current_year, title='МИКСИТИ - где купить.')


@app.route('/general/contacts')
def contacts():
    return render_template('/general/contacts.html', email=email, current_year=current_year, title='МИКСИТИ - контакты.')


@app.route('/general/trademark')
def trademark():
    return render_template('/general/trademark.html', email=email, current_year=current_year, title='МИКСИТИ - торговая марка.')


@app.route('/general/certificates')
def certificates():
    return render_template('/general/certificates.html', email=email, current_year=current_year, title='МИКСИТИ - сертификаты.')

@app.route('/glue/base_glue')
def base_glue():
    return render_template('/glue/base_glue.html', email=email, current_year=current_year, title='МИКСИТИ - БАЗОВЫЙ клей для плитки.')

if __name__ == '__main__':
    app.run(debug=True)
