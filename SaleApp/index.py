from flask import Flask, render_template, request
import dao

app = Flask(__name__)



@app.route("/")
def index():
    q =request.args.get("q")
    print(q)
    cates = dao.load_categories()
    return render_template("index.html", cates =cates, prods=dao.load_products(q=q, cate_id=cate_id))

if __name__=="__main__":
    app.run(debug=True)