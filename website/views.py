from flask import Blueprint,render_template
import json,os

views = Blueprint('views',__name__)
base_path = os.path.dirname(__file__)

@views.route('/')
def home_site():
    
    return render_template('home.html')
@views.route('/protein')
def protein_site():
    with open(base_path+"/index.json", "r") as f:
        index = json.load(f)
    dates =  index["date"]
    mp = index["protein"]["price"]["mp"]
    mpdes = index["protein"]["description"]["mp"]
    pworks= index["protein"]["price"]["pworks"]
    pworksdes= index["protein"]["description"]["pworks"]
    return render_template('protein.html',dates=dates,mp=mp,mpdes=mpdes,pworks=pworks,pworksdes=pworksdes)
@views.route('/creatine')
def creatine_site():
    with open(base_path+"/index.json", "r") as f:
        index = json.load(f)
    dates =  index["date"]
    mp = index["creatine"]["price"]["mp"]
    mpdes = index["creatine"]["description"]["mp"]
    pworks= index["creatine"]["price"]["pworks"]
    pworksdes= index["creatine"]["description"]["pworks"]
    return render_template('creatine.html',dates=dates,mp=mp,mpdes=mpdes,pworks=pworks,pworksdes=pworksdes)

