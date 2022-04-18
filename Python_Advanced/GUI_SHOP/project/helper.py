import json


from project_.paths import Paths


class Helper(Paths):

    def __init__(self):
        super().__init__()
    @staticmethod
    def delete_product_in_DB(win, name):
        found=False
        with open(Paths.PATH_TO_PRODUCTS_DB, "r+") as product:
            result_2 = []
            for every in product:
                if every != "\n":
                    cur_dict_item = json.loads(every.strip())
                    if cur_dict_item["name"] == name:
                        found= True
                        pass
                        # result_2.append(json.dumps(cur_dict_item) + "\n")
                    else:
                        result_2.append(every)
            product.seek(0)
            product.truncate()
            product.writelines(result_2)
        if found:
            return True
        else:
            return False

    @staticmethod
    def list_package(list_):
        result=""
        if len(list_)<=5:
            result=", ".join([str(x) for x in list_])
        elif len(list_)>5 and len(list_)<=10:
            result=f"{list_[:5]}\n" \
                   f"{list_[5:]}"
        elif len(list_) > 10 and len(list_)<=15:
            result = f"{list_[:5]}\n" \
                     f"{list_[5:10]}\n" \
                     f"{list_[10:]}"

        elif len(list_) > 15:
            result = f"{list_[:5]}\n" \
                     f"{list_[5:10]}\n" \
                     f"{list_[10:15]}\n" \
                     f"{list_[15:]}"
        return result










