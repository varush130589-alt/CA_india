from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AKHAND PRATAP MAURYA | Chartered Accountant</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,Helvetica,sans-serif;
}

body{
background:linear-gradient(135deg,#003366,#0059b3,#3399ff);
color:white;
}

header{
padding:30px;
text-align:center;
background:rgba(0,0,0,0.25);
}

header h1{
font-size:48px;
}

header p{
font-size:22px;
margin-top:10px;
}

.hero{
display:flex;
justify-content:space-between;
align-items:center;
padding:50px;
flex-wrap:wrap;
}

.profile{
background:white;
color:#003366;
padding:30px;
width:320px;
border-radius:20px;
box-shadow:0 10px 25px rgba(0,0,0,.3);
}

.profile h2{
text-align:center;
margin-bottom:20px;
}

.profile p{
font-size:22px;
margin:15px 0;
font-weight:bold;
}

.about{
width:60%;
min-width:320px;
padding:25px;
}

.about h2{
font-size:40px;
margin-bottom:20px;
}

.about p{
font-size:20px;
line-height:1.8;
text-align:justify;
}

.section-title{
text-align:center;
font-size:42px;
margin-top:30px;
margin-bottom:30px;
}

.services{

display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:25px;
padding:30px 50px;

}

.card{

background:white;
color:#003366;
padding:25px;
border-radius:20px;
box-shadow:0 8px 20px rgba(0,0,0,.25);
transition:.3s;

}

.card:hover{

transform:translateY(-10px);

}

.card h3{

margin-bottom:15px;
color:#0059b3;

}

.card p{

line-height:1.6;

}

.form{

margin:40px;
background:white;
padding:25px;
border-radius:25px;
color:#003366;

}

.form h2{

text-align:center;
margin-bottom:20px;

}

iframe{

width:100%;
height:900px;
border:none;
border-radius:15px;

}

footer{

text-align:center;
padding:20px;
margin-top:20px;
background:rgba(0,0,0,.25);

}

</style>

</head>

<body>

<header>

<h1>AKHAND PRATAP MAURYA</h1>

<p>Chartered Accountant</p>

</header>

<div class="hero">

<div class="profile">

<h2>Professional Profile</h2>

<p>👤 Name : Akhand Pratap Maurya</p>

<p>🎂 Age : 31 Years</p>

<p>💼 Experience : 2 Years</p>

<p>📈 Profession : Chartered Accountant</p>

</div>

<div class="about">

<h2>About</h2>

<p>

Akhand Pratap Maurya is a dedicated Chartered Accountant with two years of professional
experience. He assists individuals, businesses, and organisations in managing their
financial records, tax compliance, and statutory obligations. His objective is to provide
accurate financial guidance, maintain transparency, and help clients make informed financial
decisions while complying with applicable laws and regulations.

</p>

</div>

</div>

<h2 class="section-title">Services Offered</h2>

<div class="services">

<div class="card">
<h3>Income Tax Return (ITR)</h3>
<p>Preparation and filing of income tax returns for salaried individuals, professionals, and businesses.</p>
</div>

<div class="card">
<h3>GST Registration & Returns</h3>
<p>GST registration, monthly and annual GST return filing, and GST compliance services.</p>
</div>

<div class="card">
<h3>Accounting & Bookkeeping</h3>
<p>Maintaining accurate financial records, ledgers, balance sheets, and profit & loss accounts.</p>
</div>

<div class="card">
<h3>Business Registration</h3>
<p>Registration of proprietorships, partnerships, LLPs, and companies.</p>
</div>

<div class="card">
<h3>Financial Planning</h3>
<p>Professional advice on budgeting, investments, tax planning, and financial management.</p>
</div>

<div class="card">
<h3>Audit Services</h3>
<p>Internal audits, statutory audits, tax audits, and financial reporting support.</p>
</div>

<div class="card">
<h3>TDS Compliance</h3>
<p>TDS calculation, return filing, corrections, and compliance assistance.</p>
</div>

<div class="card">
<h3>Business Consultancy</h3>
<p>Helping businesses improve financial performance and comply with legal requirements.</p>
</div>

</div>

<div class="form">

<h2>Client Registration / Contact Form</h2>

<iframe
src="https://docs.google.com/forms/d/e/1FAIpQLSduw_9CGU_50zlQY3jtxH3zfPwlH-473j60vavZk4VDDRM0aA/viewform?embedded=true">
Loading...
</iframe>

</div>

<footer>

<h3>AKHAND PRATAP MAURYA</h3>

<p>Chartered Accountant</p>

<p>Professional Financial & Tax Consultancy</p>

</footer>

</body>

</html>
"""
@app.route('/google9cb04e0ef11d059f.html')
def google_verification():
    return send_from_directory('.', 'google9cb04e0ef11d059f.html')
if __name__ == "__main__":
    app.run(debug=True)