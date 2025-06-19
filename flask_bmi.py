from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML 表單樣板
html_form = '''
<h2>BMI 計算機</h2>
<form method="post">
    身高（公分）：<input type="text" name="height"><br><br>
    體重（公斤）：<input type="text" name="weight"><br><br>
    <input type="submit" value="計算 BMI">
</form>
{% if bmi %}
    <hr>
    <h3>你的 BMI 是：{{ bmi }}</h3>
    <p>狀態判斷：{{ status }}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    status = ""
    if request.method == "POST":
        height = float(request.form["height"]) / 100  # 公分轉公尺
        weight = float(request.form["weight"])
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            status = "體重過輕"
        elif bmi < 24:
            status = "正常範圍"
        elif bmi < 27:
            status = "稍微過重"
        else:
            status = "肥胖"

    return render_template_string(html_form, bmi=bmi, status=status)

if __name__ == "__main__":
    app.run(debug=True)
