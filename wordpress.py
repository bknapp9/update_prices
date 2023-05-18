from woocommerce import API
from read import Read
from wordpress_2 import AmericanEagle

read = Read()
final_prices_american_normal = read.read_american_normal()
final_prices_american_express = read.read_american_express()
final_prices_canadian = read.read_canadian()
final_prices_american_normal = [str(x) for x in final_prices_american_normal]
final_prices_american_express = [str(x) for x in final_prices_american_express]

wcapi = API(
    url="https://kilates.cl",
    consumer_key="ck_1794b6609b07ff78763447bc510792c56220f934",
    consumer_secret="cs_c7316944dab50202b18b40e3da5787083739cb85",
    wp_api=True,
    version="wc/v3",
    query_string_auth=False
)


def update_prices():
    # American Eagle: 1,2,3,4. Canadian Maple Leaf: 5,6,7,8.
    tries = 3
    x = 0
    for i in range(tries):
        if x == 1:
            pass
        else:
            try:

                data = {
                    "update":
                        [

                            {
                                "id": 7382,
                                "regular_price": final_prices_canadian[0]},
                            {
                                "id": 8024,
                                "regular_price": final_prices_canadian[1]},
                            {
                                "id": 8030,
                                "regular_price": final_prices_canadian[2]},
                            {
                                "id": 9286,
                                "regular_price": final_prices_canadian[3]}

                            ]
                }

                x += 1
                wcapi.put("products/batch", data).json()
                american_eagle = AmericanEagle()
                american_eagle.update()

            except:
                if i < tries - 1:
                    continue
                else:
                    raise
                break


if __name__ == '__main__':
    update_prices()
