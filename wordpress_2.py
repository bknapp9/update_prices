from woocommerce import API
from read import Read

read = Read()
final_prices_american_normal = read.read_american_normal()
final_prices_american_express = read.read_american_express()
final_prices_canadian = read.read_canadian()
final_prices_american_normal = [str(x) for x in final_prices_american_normal]
final_prices_american_express = [str(x) for x in final_prices_american_express]


class AmericanEagle():
    def update(self):
        tries = 3
        x = 0
        for i in range(tries):
            if x == 1:
                i += 1
            else:
                try:
                    wcapi = API(
                        url="https://kilates.cl",
                        consumer_key="ck_1794b6609b07ff78763447bc510792c56220f934",
                        consumer_secret="cs_c7316944dab50202b18b40e3da5787083739cb85",
                        wp_api=True,
                        version="wc/v3",
                        query_string_auth=False
                    )

                    product_ids = [11167, 11161, 11185, 11187, 11166, 11162, 11184, 11186]
                    for product_id in product_ids:
                        product = wcapi.get(f"products/{product_id}").json()

                    product_variations = [
                                {"product_id": 7397, "variation_id": 11167, "regular_price": final_prices_american_normal[0]},
                                {"product_id": 8041, "variation_id": 11161, "regular_price": final_prices_american_normal[1]},
                                {"product_id": 8035, "variation_id": 11185, "regular_price": final_prices_american_normal[2]},
                                {"product_id": 9283, "variation_id": 11187, "regular_price": final_prices_american_normal[3]},
                                {"product_id": 7397, "variation_id": 11166, "regular_price": final_prices_american_express[0]},
                                {"product_id": 8041, "variation_id": 11162, "regular_price": final_prices_american_express[1]},
                                {"product_id": 8035, "variation_id": 11184, "regular_price": final_prices_american_express[2]},
                                {"product_id": 9283, "variation_id": 11186, "regular_price": final_prices_american_express[3]}
                                    ]

                    for product_variation in product_variations:
                        product_id = product_variation["product_id"]
                        variation_id = product_variation["variation_id"]
                        regular_price = product_variation["regular_price"]

                        variation = wcapi.get(f"products/{product_id}/variations/{variation_id}").json()

                        if "out_stock_threshold" in variation:
                            del variation["out_stock_threshold"]
                        if "low_stock_amount" in variation:
                            del variation["low_stock_amount"]

                        variation["regular_price"] = regular_price

                        print(wcapi.put(f"products/{product_id}/variations/{variation_id}", variation).json())
                    x += 1

                except:
                    if i < tries - 1:
                        continue
                    else:
                        raise
                    break
    """
    product_id = 8041
    variation_id = 11161
    
    variation = wcapi.get(f"products/{product_id}/variations/{variation_id}").json()
    
    variation["regular_price"] = "10.99"
    
    if "out_stock_threshold" in variation:
        del variation["out_stock_threshold"]
    
    print(wcapi.put(f"products/{product_id}/variations/{variation_id}", variation).json())
    """