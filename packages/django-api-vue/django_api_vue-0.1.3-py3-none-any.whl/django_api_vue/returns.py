from django.http import JsonResponse


def base_return(return_data, status=200):
    return JsonResponse(return_data, status=status)


def success_return(data=None, status=200):
    if data is None:
        data = {}
    return_data = {
        "err_msg": "ok",
        "data": data,
    }
    return base_return(return_data, status=status)


def error_return(errmsg, status=500):
    return_data = {
        "err_msg": errmsg,
        "data": None,
    }
    return base_return(return_data, status=status)
