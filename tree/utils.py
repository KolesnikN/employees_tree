from django.http import JsonResponse

lsb='id'

def json_data_tree(queryset):
    li = {'q': []}
    for emp in queryset:
        li['q'].append({'id': emp.id, 'nm': emp.name, 'pos': emp.position,
                        'dt': emp.emp_date, 'sl': emp.salary,
                        'lev': emp.level, 'leaf': emp.is_leaf_node()})

    return JsonResponse(li)

def last_sort_by(sort_by=''):
    global lsb
    if sort_by:
        lsb = sort_by
    return lsb