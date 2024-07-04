from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/task_1.html')
def task_1():

    images = ['static/images/image.png',
              'static/images/tiger.jpg',
              'static/images/naam_tamilar_flag.jpg']
    
    return render_template('task_1.html', images=images)

@app.route('/task_2.html')
def task_2():
    return render_template('task_2.html', the_title='Tiger in Myth and Legend')

@app.route('/task_3.html')
def task_3():
    return render_template('task_3.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
