from flask import Flask,render_template,url_for,flash,redirect
app = Flask(__name__)
from forms import RegistrationForm,LoginForm

app.config['SECRET_KEY'] ='618b6378964230b69c683c9ebb934d56'

posts = [
   {
      'shop_image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-OEDz-MZJP6pXChi6G8EzfXRH76E-jmx-0Q&usqp=CAU',
      'shop_name':'mohan medicals',
      'role':'labour',
      'person_required':7,
      'address':'opposite to CA school',
      'district':'tirupur',
      'state':'tamilnadu',
      'salary_per_month':10000,
      'working_hours':9,
      'working_time':'9AM - 6PM',
      'gender':'both male and female',
      'contact_no':9988776655
   },

   {
      'shop_image':'https://b.zmtcdn.com/data/reviews_photos/805/1659de5d4db9333e608e98578c75c805_1626096320.jpg',
      'shop_name':'Junior kuppanna',
      'role':'labour',
      'person_required':5,
      'address':'opposite to old bus stand',
      'district':'palladam',
      'state':'tamilnadu',
      'salary_per_month':13000,
      'working_hours':10,
      'working_time':'9AM - 7PM',
      'gender':'Male',
      'contact_no':9876654790
   },

   {
      'shop_image':'https://lh3.googleusercontent.com/p/AF1QipNz8zyDtjWnvP_NQzji3FXY4DE01n6h676dZiI1=w1080-h608-p-no-v0',
      'shop_name':'RVS fancy',
      'role':'labour',
      'person_required':2,
      'address':'munikapam church,near nallur',
      'district':'Erode',
      'state':'tamilnadu',
      'salary_per_month':8000,
      'working_hours':8,
      'working_time':'9AM - 5PM',
      'gender':'female',
      'contact_no':9876654790
   },
   {
      'shop_image':'https://media-cdn.tripadvisor.com/media/photo-s/16/f5/0e/f6/fresh-juice-everyday.jpg',
      'shop_name':'Green fresh juice',
      'role':'labour',
      'person_required':2,
      'address':'munus church,near kulathur',
      'district':'Salem',
      'state':'tamilnadu',
      'salary_per_month':4000,
      'working_hours':5,
      'working_time':'12AM - 5PM',
      'gender':'Male',
      'contact_no':9876655790
   }
]
@app.route("/home")
@app.route("/")
def home():
  return render_template('home.html', job = posts)

@app.route("/about")
def about():
  return render_template('about.html',title = 'about')
    
@app.route("/register",methods=['GET','POST'])
def register():
  form=RegistrationForm()
  if form.validate_on_submit():
     flash(f'Account created for {form.username.data}!','success')
     return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)
  
@app.route("/login",methods=['GET','POST'])
def login():
  form=LoginForm()
  return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True,port = 8080)

