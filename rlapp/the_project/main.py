from flask import Flask, render_template, request

import pandas as pd
import csv
import copy 


from get_dict import get_dict
from get_R_Q import initial_R
from get_R_Q import initial_Q
from get_result import get_result




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if(request.method=='POST'):
        csv_file_got = request.form['the_csv_file']
        # with open(csv_file_got) as file:
        #     csv_file_got = csv.reader(file)

        start_got = request.form['START']
        end_got = request.form['END']
        R,Q_init, res, final_Q = find_nodes(csv_file_got, start_got, end_got)
        res_x = str(res)


        res_fin = res_x.replace('{', '')
        res_fin = res_x.replace('], [', '; ')
        res_fin = res_fin.replace(',', ' to ')
        res_fin = res_fin.replace(']', '')
        #res_fin = res_fin.replace('{', ' to ')
        start_got_str = '{' + end_got + ':'
        res_fin = res_fin.replace(start_got_str, '')
        res_fin = res_fin.replace('[', '')
        res_fin = res_fin.replace('}', '')
        
        # res_fin = res_fin.replace(',', ' to ')

            
            
    return render_template('datafile.html', data_R =R, data_Q = Q_init, data_res = res_fin, data_final_Q = final_Q)
            
def find_nodes(csv_file, start_node, end_node):
    data = pd.read_csv(csv_file)
    graph = get_dict(data)

    A = graph["A"]
    Z = graph["Z"]
    weight = graph["weight"]
    A_Z_dict = graph["A_Z_dict"]
    start = int(start_node)
    end =[int(end_node)]

   

    R = initial_R(A,Z,weight,A_Z_dict)
    Q_init = initial_Q(R)
    Q = copy.deepcopy(Q_init)

    # print("The WEIGHT-TABLE from a NODE A TO NODE B	:	")
    # print(R)
    # print("The Q-TABLE after initialisation		:	")
    # print(Q)

    alpha = 0.7 # learning rate
    epsilon = 0.1 #greedy policy
    n_episodes = 900


    # print("The final Q table	:	")


    # time0 = time.time()
    result = get_result(R,Q,alpha,epsilon,n_episodes,start,end)
    # print("time is:",time.time() - time0)

    # print(result["ends_find"])
    # print(result["cost"])
    # print(result["routes_number"])
    # print(result["all_routes"])

    return R, Q_init, result["all_routes"], result["final_Q"]



if __name__ == "__main__":
    app.run(debug=True)