from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/student_life')
def student_life():
    return render_template('student_life.html')

@app.route('/parent_resources')
def parent_resources():
    return render_template('parent_resources.html')

@app.route('/staff_directory')
def staff_directory():
    return render_template('staff_directory.html')

@app.route('/alumni')
def alumni():
    return render_template('alumni.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/support_us')
def support_us():
    return render_template('support_us.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

if __name__ == '__main__':
    app.run(debug=True)
