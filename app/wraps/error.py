from flask import abort


def robust(actual_do):
    def add_robust(*args, **kwargs):
        try:
            return actual_do(*args, **kwargs)
        except Exception as e:
            try:
                data = e.data['messages']
            except:
                data = e.data
            try:
                code = e.code
            except:
                code = 422
            abort(code, data)

    return add_robust
