from flask import Flask,render_template,request
import requests
import pickle
import numpy as np
import pandas as pd


sweet_dict =pickle.load(open('sweets1.pkl','rb'))
sweets = pd.DataFrame(sweet_dict)

similarity = pickle.load(open('similarity1.pkl', 'rb'))


app = Flask(__name__)


def fetch_poster(sweet_id):

    url = "http://127.0.0.1:5000/courses/{}".format(sweet_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['course']['url']

    return poster_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['post'])
def rec():

    user_input = request.form.get('user_input')
    sweet_index = sweets[sweets['name'] == user_input].index[0]
    distances = similarity[sweet_index]
    sweet_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    print(sweet_list)
    re =[]
    for j in sweet_list:
     b=False
     for i in j:
        if b==True :
            break
        b = True

        sweet_id = sweets.iloc[i][4]
        print(sweet_id)
        temp=[]
        temp.append(sweets.iloc[i][0])
        temp.append(fetch_poster(sweet_id))
        re.append(temp)

    return render_template('index.html', data=re);


@app.route('/na')
def na():

    n_index = sweets[sweets['region']=='North']
    n_index = n_index['ID'].values
    print(n_index)
    n_list =[]
    for i in n_index:
        sweet_id = sweets.iloc[i][4]
        temp=[]
        temp.append(sweets.iloc[i][0])
        temp.append(fetch_poster(sweet_id))
        n_list.append(temp)

    return render_template('North.html', data=n_list)


@app.route('/wa')
def wa():

    n_index = sweets[sweets['region']=='West']
    n_index = n_index['ID'].values
    print(n_index)
    n_list =[]
    for i in n_index:
        sweet_id = sweets.iloc[i][4]
        temp=[]
        temp.append(sweets.iloc[i][0])
        temp.append(fetch_poster(sweet_id))
        n_list.append(temp)

    return render_template('West.html', data=n_list)


@app.route('/ea')
def ea():

    n_index = sweets[sweets['region']=='East']
    n_index = n_index['ID'].values
    print(n_index)
    n_list =[]
    for i in n_index:
        sweet_id = sweets.iloc[i][4]
        temp=[]
        temp.append(sweets.iloc[i][0])
        temp.append(fetch_poster(sweet_id))
        n_list.append(temp)

    return render_template('East.html', data=n_list)


@app.route('/sa')
def sa():

    n_index = sweets[sweets['region']=='South']
    n_index = n_index['ID'].values
    print(n_index)
    n_list =[]
    for i in n_index:
        sweet_id = sweets.iloc[i][4]
        temp=[]
        temp.append(sweets.iloc[i][0])
        temp.append(fetch_poster(sweet_id))
        n_list.append(temp)

    return render_template('South.html', data=n_list)


if __name__ == '__main__':
    app.run(host="localhost", port=7000, debug=True)
