from flask import Flask, render_template
import names

app = Flask(__name__)

#Generate random names
def generate_names(numberofnames):
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())
        print(i)
    return nlist
namelist = generate_names(50)

#Homepage
@app.route('/')
def home():
    return render_template('home.html', namelist=namelist)

def test_generate_names():
    namelist1 = generate_names(101)
    assert len(namelist1) == 101