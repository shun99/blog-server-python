from flask import abort


def robust(actual_do):
    def add_robust(*args, **kwargs):
        try:
            return actual_do(*args, **kwargs)
        except Exception as e:
            params = e.args
            abort(e.args[1] | 422, params)

    return add_robust
