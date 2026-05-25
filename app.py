from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Cloud Native App</title>
        <style>
            body{
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color:white;
                font-family: Arial;
                text-align:center;
                padding-top:100px;
            }

            .card{
                background: rgba(255,255,255,0.1);
                width:60%;
                margin:auto;
                padding:40px;
                border-radius:20px;
                box-shadow:0px 0px 20px rgba(0,0,0,0.5);
            }

            h1{
                font-size:50px;
                color:#00d4ff;
            }

            h2{
                color:#ffffff;
            }

            p{
                font-size:20px;
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>☁ Cloud Native Application</h1>

            <h2>Aplicația funcționează cu succes!</h2>

            <p>Python Flask + Docker + Kubernetes + CI/CD</p>

            <p>Universitatea Tehnică a Moldovei</p>

            <p>Laborator Aplicații Cloud</p>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)