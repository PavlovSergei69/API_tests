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