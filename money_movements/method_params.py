from drf_yasg import openapi


date_time_start = openapi.Parameter(
    'date_time_start', 
    openapi.IN_QUERY, 
    'Date and time start money movement', 
    type=openapi.TYPE_STRING
)

date_time_end = openapi.Parameter(
    'date_time_end',
    openapi.IN_QUERY,
    'Date and time end money money movement',
    type=openapi.TYPE_STRING
)

status = openapi.Parameter(
    'status',
    openapi.IN_QUERY,
    'Identifier of status in database',
    type = openapi.TYPE_INTEGER
)

type = openapi.Parameter(
    'type',
    openapi.IN_QUERY,
    'Identifier of type in database',
    type = openapi.TYPE_INTEGER
)

category = openapi.Parameter(
    'category',
    openapi.IN_QUERY,
    'Identifier of category in database',
    type = openapi.TYPE_INTEGER
)

subcategory = openapi.Parameter(
    'subcategory',
    openapi.IN_QUERY,
    'Identifier of subcategory in database',
    type = openapi.TYPE_INTEGER
)

LIST_PARAMS = [date_time_start, date_time_end, status, type, category, subcategory]