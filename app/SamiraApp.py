from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="fa">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>صفحه دانشجو</title>
  <style>
    html,body{
      height:100%;
      margin:0;
      padding:0;
      font-family: "Tahoma", Arial, Helvetica, sans-serif;
      direction: rtl;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }
    body{
      background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 50%, #ff9fbf 100%);
      display:flex;
      align-items:center;
      justify-content:center;
    }
    .card{
      background: rgba(255,255,255,0.12);
      border-radius: 14px;
      padding: 22px 42px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      backdrop-filter: blur(6px) saturate(120%);
      -webkit-backdrop-filter: blur(6px) saturate(120%);
      border: 1px solid rgba(255,255,255,0.08);
      display:inline-block;
      text-align:center;
      min-width:320px;
    }
    .name{
      color: #ffffff;
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
      letter-spacing: 0.4px;
    }
    .id{
      color: #f7f7f7;
      font-size: 18px;
      font-weight: 600;
      opacity:0.95;
    }
    .note{
      margin-top: 12px;
      font-size: 14px;
      color: #fff;
      opacity: 0.9;
    }
  </style>
</head>
<body>
  <div class="card" role="main" aria-label="کارت دانشجویی">
    <div class="name">سمیرا ارواحی</div>
    <div class="id">40113011003</div>

    <!--  این خط جدید اضافه شد -->
    <div class="note">این یک تغییر تستی است </div>

  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
