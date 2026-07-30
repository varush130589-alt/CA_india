# =====================================================
# AKHAND PRATAP MAURYA - CA WEBSITE
# Flask Website
# =====================================================


# Import Flask and required functions
from flask import Flask, send_from_directory
import os


# Create Flask application
app = Flask(__name__)



# =====================================================
# COMMON DESIGN FOR SERVICE PAGES
# (Defined first so all pages can use it)
# =====================================================


def service_page(title, content):

    return f"""

<!DOCTYPE html>

<html>

<head>

<title>{title}</title>


<style>

body{{

background:#e6f2ff;
font-family:Arial, sans-serif;
padding:40px;

}}


.box{{

background:white;
color:#003366;
padding:40px;
border-radius:25px;
max-width:900px;
margin:auto;
box-shadow:0px 5px 20px gray;

}}


h1{{

text-align:center;
color:#003366;

}}


h2{{

margin-top:30px;

}}


li{{

margin:10px;

}}


</style>


</head>


<body>


<div class="box">


<h1>
{title}
</h1>


<p>

{content}

</p>


<h2>
Client Enquiry
</h2>


<p>
For professional consultation, contact Akhand Pratap Maurya.
</p>


<!-- Google Form can be added here later -->


</div>


</body>


</html>

"""



# =====================================================
# HOME PAGE
# =====================================================


@app.route("/")
def home():

    return """

<!DOCTYPE html>

<html>

<head>

<title>
AKHAND PRATAP MAURYA | Chartered Accountant
</title>


<style>

*{

margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial;

}


body{

background:linear-gradient(135deg,#003366,#3399ff);
color:white;

}



header{

text-align:center;
padding:40px;
background:rgba(0,0,0,0.3);

}



header h1{

font-size:45px;

}



.about{

padding:40px;
text-align:center;

}



.about p{

font-size:20px;
line-height:1.8;

}



.services{

display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:25px;
padding:40px;

}



.card{

background:white;
color:#003366;
padding:30px;
border-radius:20px;
text-align:center;
transition:0.3s;

}



.card:hover{

transform:translateY(-10px);

}



a{

text-decoration:none;

}


</style>


</head>


<body>


<header>

<h1>
AKHAND PRATAP MAURYA
</h1>

<p>
Chartered Accountant
</p>

</header>



<div class="about">

<h2>
Professional Financial Services
</h2>


<p>

Providing expert assistance in Income Tax,
GST, Accounting, Audit and Financial Consultancy.

</p>


</div>



<h2 style="text-align:center;">
Services Offered
</h2>


<div class="services">


<a href="/itr">

<div class="card">

<h2>
Income Tax Return (ITR)
</h2>

<p>
Click to learn more
</p>

</div>

</a>



<a href="/gst">

<div class="card">

<h2>
GST Services
</h2>

<p>
Click to learn more
</p>

</div>

</a>



<a href="/accounting">

<div class="card">

<h2>
Accounting & Bookkeeping
</h2>

<p>
Click to learn more
</p>

</div>

</a>



<a href="/audit">

<div class="card">

<h2>
Audit Services
</h2>

<p>
Click to learn more
</p>

</div>

</a>


</div>


</body>

</html>

"""
# =====================================================
# SERVICE PAGES
# =====================================================


# Income Tax Return Page

@app.route("/itr")
def itr():

    return service_page(

        "Income Tax Return (ITR)",

        """
        <h2>What is Income Tax Return (ITR)?</h2>

        Income Tax Return is a form used by individuals
        and businesses to declare their income,
        deductions and taxes paid to the government.

        <br><br>

        <h2>Why is ITR important?</h2>

        <ul>

        <li>Acts as proof of income</li>

        <li>Helpful for loans and financial applications</li>

        <li>Maintains tax compliance</li>

        <li>Helps in financial planning</li>

        </ul>


        <br>

        <h2>Services Provided</h2>

        <ul>

        <li>ITR preparation</li>

        <li>Tax calculation</li>

        <li>Tax filing assistance</li>

        <li>Tax planning</li>

        </ul>

        """

    )





# GST Services Page

@app.route("/gst")
def gst():

    return service_page(

        "GST Services",

        """

        <h2>What is GST?</h2>

        Goods and Services Tax (GST) is an indirect tax
        applied on goods and services in India.

        <br><br>


        <h2>GST Services Offered</h2>

        <ul>

        <li>GST Registration</li>

        <li>GST Return Filing</li>

        <li>GST Compliance</li>

        <li>GST Consultation</li>

        </ul>

        """

    )





# Accounting Page

@app.route("/accounting")
def accounting():

    return service_page(

        "Accounting & Bookkeeping",

        """

        <h2>About Accounting Services</h2>


        Accounting helps businesses maintain accurate
        records of their financial transactions.


        <br><br>


        <h2>Services Included</h2>


        <ul>

        <li>Bookkeeping</li>

        <li>Balance Sheet Preparation</li>

        <li>Profit and Loss Statements</li>

        <li>Financial Reports</li>

        </ul>


        """

    )





# Audit Page

@app.route("/audit")
def audit():

    return service_page(

        "Audit Services",

        """

        <h2>What is Audit?</h2>


        Audit is the examination of financial records
        to ensure accuracy and transparency.


        <br><br>


        <h2>Audit Services</h2>


        <ul>

        <li>Internal Audit</li>

        <li>Financial Audit</li>

        <li>Tax Audit</li>

        <li>Compliance Checking</li>


        </ul>


        """

    )
# =====================================================
# GOOGLE SEARCH CONSOLE VERIFICATION
# =====================================================

# This route allows Google to verify website ownership.
# Keep the verification HTML file in the same folder as app.py.


@app.route('/google9cb04e0ef11d059f.html')
def google_verification():

    return send_from_directory(
        '.',
        'google9cb04e0ef11d059f.html'
    )



# =====================================================
# RUN FLASK WEBSITE
# =====================================================


if __name__ == "__main__":

    # Render automatically provides a PORT number.
    # This makes the website work online.

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
    #end