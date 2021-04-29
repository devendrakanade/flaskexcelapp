from flask import Flask,render_template,request
import pandas as pd

app=Flask("My_Excel")
@app.route('/',methods=['GET','POST'])
def myform():
    return render_template('index.html')

@app.route('/output',methods=['GET','POST'])
def output():
    data = int(request.form.get("x"))
    dataset = pd.read_excel('Employee_sal.xlsx')
    Name = dataset['Name']
    dataset['Salary'] = dataset['Salary'] + dataset['Salary']*(data/100)
    filename="Out_file.xlsx"
    dataset.to_excel(filename)

    return "Data is Now Updated to Out_file.xlsx Check it out"
app.run(port=1234,debug=True)
