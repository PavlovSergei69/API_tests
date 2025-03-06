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

#ДОПОЛНИТЕЛЬНО. Для условия, что мы проверям все.
# SCHEMA = {
#     "type": "object",
#     "properties": {
#         "page": {"type": "integer"},
#         "per_page": {"type": "integer"},
#         "total": {"type": "integer"},
#         "total_pages": {"type": "integer"},
#         "data": {
#             "type": "array",
#             "items": {
#                 "type": "object",
#                 "properties": {
#                     "id": {"type": "integer"},
#                     "email": {"type": "string"},
#                     "first_name": {"type": "string"},
#                     "last_name": {"type": "string"},
#                     "avatar": {"type": "string"}
#                 },
#                 "required": ["id", "email", "first_name", "last_name", "avatar"]
#             }
#         }
#     },
#     "required": ["page", "per_page", "total", "total_pages", "data"]
# }