from generated.apps import Commonv1Value


def patch_common_value():
    origin_from_dict = Commonv1Value.from_dict

    def new_from_dict(obj: dict):
        temp_obj = obj
        if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float):
            temp_obj = {
                'value': str(obj),
            }
        return origin_from_dict(temp_obj)

    Commonv1Value.from_dict = new_from_dict


