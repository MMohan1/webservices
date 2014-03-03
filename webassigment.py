import requests
from bottle import route, run, template,get,post,delete,request 
p_dict={}
store_info=[]

@post('/patient')
def add_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    pa_phone = request.POST['phone']
    store_info = ' '.join([p_name,p_gender,p_age,p_address,pa_phone])
    p_dict.update({p_id:store_info})
    return p_dict

@get('/patient_show/<p_id>')
def show_patient(p_id):
    if p_id not in p_dict.keys():
        return 'This is not a correct patient id'
    else:
        return p_dict[p_id]


@put('/patient_update')
def patient_update():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    pa_phone = request.POST['phone']
    store_info = ' '.join([p_name,p_gender,p_age,p_address,pa_phone])
    p_dict.update({p_id:store_info})
    return p_dict

@delete('/patient_delete/<p_id>')
def delete_patient(p_id):
    if p_id not in p_dict.keys():
        return 'This is not a correct patient id'
    else:
	p_dict.pop(p_id)
	return p_dict

run(host='localhost',port=8080)
