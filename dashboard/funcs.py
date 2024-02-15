from django.core.paginator import (Paginator, 
                                   EmptyPage, 
                                   PageNotAnInteger)


def search_with_fields(request):
    result = {}
    for key, value in request.GET.items():
        if value:
            if key == 'name':
                key = 'product__name__icontains'
            elif key == 'created_at_start':
                key = 'created_at__gte'
            elif key == 'created_at_end':
                key = 'created_at__lte'
            
            result[key] = value

    return result


def filter_product(request):
    result={}
    for key,value in request.GET.items():
        if value:
            if key=='name':
                key='name__icontains'
            elif key=='quantity_min':
                key='quantity__gte'
            elif key=='quantity_max':
                key='quantity__lte'
            elif key=='price_min':
                key='price__gte'
            elif key=='price_max':
                key='price__lte'
            result[key]=value
    return result


def pagenator_page(queryset, num, page):
    paginator = Paginator(queryset, num)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return queryset