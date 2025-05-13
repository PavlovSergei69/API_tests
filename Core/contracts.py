LIST_RESOURCE_SCHEME = {
    "type":"object",
    "properties": {
        "id": {
            "type":"number"
        },
        "name": {
            "type":"string"
        },
        "year": {
            "type":"number"
        },
        "color": {
            "type":"string"
        },
        "pantone_value": {
            "type":"string"
        }
    },
    "required":["id", "name", "year", "color","pantone_value"],
    "additionalProperties": False
}

#договоренность между двумя сторонами, что должно приходить в ответе
USER_DATA_SHEME = {
    "type":"object",
    #характеристики
    "properties": {
        "id": {
            "type":"number"
        },
        "email": {
            "type":"string"
        },
        "first_name": {
            "type":"string"
        },
        "last_name": {
            "type":"string"
        },
        "avatar": {
            "type":"string"
        }
    },
    #Обязательные параметры
    "required":["id", "email","first_name","last_name", "avatar"],
    "additionalProperties": False
}

