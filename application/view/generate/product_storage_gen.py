from application.bll.product_storage_controller import get_all_product_storages, create_product_storages


def view_product_storages():
    product_storages = get_all_product_storages()
    print("*"*10,"\nAll Product Storages\n"+"*"*10,"\n")
    for storage in product_storages:
        print(storage)


def add_product_storages(product_storages):
    #product_storages = {
     #   'product_stored': '',
      #  'product_min_limit': '',
       # 'product_max_limit': ''
    #}
    create_product_storages(product_storages)


def test_add_product_storages():
    product_storages = {
        'product_stored': '',
        'product_min_limit': '',
        'products_max_limit': '',
        'Storage_idstorage': ''
    }
    add_product_storages(product_storages)


if __name__ == '__main__':
    test_add_product_storages()
    #view_product_storages()
