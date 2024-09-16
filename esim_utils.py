def sort_esims_by_prices(esims):
    sorted_esims = sorted(esims, key=lambda esim: esim["price"])
    return sorted_esims
