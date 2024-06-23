from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        author_name = request.form.get('author').title()
        book_name = request.form.get('book').title()
        book_rating = int(request.form.get('rating'))
        # print(author_name, book_name, book_rating)
        all_books.append(
                {
                    "title": book_name,
                    "author": author_name,
                    "rating": book_rating
                }
            )
        print(all_books)
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

