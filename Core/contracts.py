LIST_RESOURCE_SCHEME = {
    'type':'object',
    'properties':{
        'id':{'type':'number'},
        'name':{'type':'string'},
        'year':{'type':'number'},
        'color':{'type':'string'},
        'pantone_value':{'type':'string'}
    },
    'requiered':['id', 'name', 'year', 'color','pantone_value']
}

#договоренность между двуями сторонами, что должно приходить в ответе
USER_DATA_SHEME = {
    'type':'object',
    #характеристики
    'properties':{
        'id':{'type':'number'},
        'email':{'type':'string'},
        'first_name':{'type':'string'},
        'last_name':{'type':'string'},
        'avatar':{'type':'string'}
    },
    #Обязательные параметры
    'requierd':['id', 'email','first_name','last_name', 'avatar']
}

