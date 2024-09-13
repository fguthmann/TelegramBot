def filter_esims_by_criteria(esims, min_days, min_gb):
    filtered_esims = []

    for esim in esims:
        if esim["days"] >= min_days and esim["gb"] >= min_gb:
            filtered_esims.append(esim)

    sorted_esims_by_prices = sort_esims_by_prices(filtered_esims)
    return sorted_esims_by_prices


def sort_esims_by_prices(esims):
    # Sort the filtered eSIMs by price in ascending order
    sorted_esims = sorted(esims, key=lambda esim: esim["price"])
    return sorted_esims
