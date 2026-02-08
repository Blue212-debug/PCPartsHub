from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>My Website</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
      background: #f4f4f4;
      text-align: center;
    }
    header {
      background: #007bff;
      color: white;
      padding: 20px;
      border-radius: 5px;
    }
    main {
      margin-top: 30px;
    }
    a.button {
      display: inline-block;
      padding: 10px 20px;
      background: #007bff;
      color: white;
      text-decoration: none;
      border-radius: 3px;
      margin-top: 20px;
    }
    a.button:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to My Website</h1>
  </header>
  <main>
    <p>This is a simple homepage created for your project.</p>
    <a href="#" class="button">Get Started</a>
  </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
