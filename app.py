from flask import Flask ,render_template ,request
import numpy as np
import plotly.express as px
import plotly
import pandas as pd



app = Flask(__name__)



def calc_reynolds(masse_vol , vitesse ,diam,visco):
    return masse_vol * vitesse * diam /visco





@app.route("/",methods = ["GET","POST"])
def home():
    plot_html = None
    if request.method == "POST":
        masse_vol = float(request.form["masse_volumique"])
        vitesse = np.linspace(0.1,10,100)
        diam = float(request.form["diametre"])
        visco = float(request.form["viscosité"])

        reynolds_val = calc_reynolds(masse_vol , vitesse ,diam,visco)

        data = pd.DataFrame({
            "reynolds" : reynolds_val,
            "vitesse"  : vitesse
        })

        fig = px.line(data, x="vitesse", y="reynolds", title='Reynolds plot vs velocity')

        plot_html = plotly.io.to_html(fig, full_html=False) 

    return render_template("index.html",plot_html = plot_html)



if __name__ == "__main__":
    app.run(debug=True)