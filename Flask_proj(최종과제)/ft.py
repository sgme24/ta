from datetime import datetime
from flask import Flask, render_template, request , redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'simple_key'
titles=[]
times=[]
@app.route('/')
def index():
    return render_template('list.html', titles=titles, times=times)
@app.route('/write', methods=['POST'])
def add():
    
    title=request.form.get('title')
    if title:
        titles.append(title)
        times.append(datetime.now().strftime('%Y-%m-%d %H:%M'))
        flash(f"'{title}' 공지사항이 성공적으로 등록되었습니다")
    else:
        flash('내용을 입력하세요')
    return redirect(url_for('index'))
@app.route('/delete/<int:index>')
def delete(index):
    if 0<=index<len(titles):
        ok=titles[index]
        titles.pop(index)
        times.pop(index)
        flash(f"'{ok}' 게시글이 삭제되었습니다.")
    return redirect(url_for('index'))
@app.route('/write')
def write():
    return render_template('write.html')
if __name__ == '__main__':
    app.run(debug=True)