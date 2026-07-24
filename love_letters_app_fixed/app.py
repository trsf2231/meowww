from flask import Flask, render_template, request

app = Flask(__name__)

# سوالات، جواب‌ها و متن نامه‌ها
data = {
    "1": {"q": "Where was our first date?(type in farsi)", "a": "انقلاب", "text": """I was about to write another letter or memory like other letters I had made you but I figured I need something different, so I decided to compare my first impression(date) VS now.
First time I saw you from distance, finally arriving, I didn't know if I should be mad about your delay, nervous about the first meeting or melt or jump from excitement. So I poorly managed it with a "چه عجب!!!" and a tight hug. Your hands were shaking and you were sooo quiet. So different from that freaky and cute mf I knew from chats. So I first thought you're a shy guy. But it didn't take much time for you to get comfortable with me and flirt or eat my gum. And It was good to find out you were the same silly guy. Even sillier. 
But now this silly boy who's my good boy has no shame to lock my hands above my head and hold me down as I whisper in his ears. Now I saw him shy and cute and saw him moaning and begging me for a kiss. I saw him happily laughing with me while dancing in the kitchen with linkin park songs and I saw him crying in my arms. And I'm indescribably happy about how close we got and just… being there for and with each other with no play.
And I absolutely adore every seconds we had since that pretty day in enghelab till now and can't wait to make uncountable memories with you and tell them to our kids.
I'm crazy in love with you. And I'll get even crazier about this so be prepared. 
"""},
    "2": {"q": "What do we say as 'makes sense'?", "a": "males centa", "text": "Good job you pretty boy;b"},
    "3": {"q": "Our anniversary date?(YYYY-MM-DD)", "a": "2025-08-26", "text": "yayyyy"},
    "4": {"q": "Name of the cafe we kissed in for the first time?(type in farsi)", "a": "برف", "text": "this puzzle was my favorite one:)"},
    "5": {"q": "Who's you mother's future bride?(name in small characters)", "a": "tarannom", "text": "smart smart boy"},
    "6": {"q": "What does a good boy call me hmm?", "a": "mommy", "text": "chase me the same way :b"}
}

# Which puzzle template each letter unlocks (letter 1 is a plain text reveal)
PUZZLES = {
    "2": "puzzles/sliding.html",
    "3": "puzzles/sudoku.html",
    "4": "puzzles/jigsaw.html",
    "5": "puzzles/memory.html",
    "6": "puzzles/maze.html",
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/letter/<id>', methods=['GET', 'POST'])
def letter(id):
    if id not in data:
        return "Letter not found", 404

    if request.method == 'POST':
        user_ans = request.form.get('answer', '').strip().lower()
        if user_ans == data[id]["a"].lower():
            if id == "1":
                return render_template('letter.html', text=data[id]["text"])
            else:
                return render_template(PUZZLES[id], id=id, text=data[id]["text"])
        else:
            return render_template('question.html', id=id, question=data[id]["q"], error="Nope. wrong:( ")

    return render_template('question.html', id=id, question=data[id]["q"])


if __name__ == '__main__':
    app.run(debug=True)
