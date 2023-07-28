from flask import Flask, render_template_string, request
import random
import string

app = Flask(__name__)

facts_list = [
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar. 2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor. Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor. Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        password = generate_password(length)
    else:
        password = None

    random_fact = random.choice(facts_list)
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Password Generator</title>
        </head>
        <body>
            <h1>Generate a random password</h1>
            <form method="POST">
                <label for="length">Password Length:</label>
                <input type="number" id="length" name="length" value="12" min="1" max="32">
                <input type="submit" value="Generate">
            </form>

            {% if password %}
                <h2>Generated Password:</h2>
                <p>{{ password }}</p>
            {% endif %}

            <h2>Random Fact:</h2>
            <p>{{ random_fact }}</p>
        </body>
        </html>
    """, password=password, random_fact=random_fact)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    app.run(debug=True, port=5001)

