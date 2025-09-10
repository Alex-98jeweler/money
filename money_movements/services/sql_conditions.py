from datetime import datetime
from django.db.models import Q


def prepare_money_movements_conditions(request_params: dict):
    date_time_start = request_params.get('date_time_start')
    date_time_end = request_params.get('date_time_end')
    status = request_params.get('status')
    type_ = request_params.get('type')
    category = request_params.get('category')
    subcategory = request_params.get('subcategory')
    q = Q()
    if date_time_start:
        date_time_start = datetime.fromisoformat(date_time_start)
        q &= Q(date_time__gte=date_time_start)
    if date_time_end:
        date_time_end = datetime.fromisoformat(date_time_end)
        q &= Q(date_time__lte=date_time_end)
    if status:
        q &= Q(status_id=status)
    if type_: 
        q &= Q(type=type_)
    if category:
        q &= Q(category=category)
    if subcategory:
        q &= Q(subcategory=subcategory)
    return q