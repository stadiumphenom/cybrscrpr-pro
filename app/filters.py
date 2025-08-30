def filter_results(results, keywords):
    """
    Filters the results based on the presence of any keyword (case-insensitive).
    Returns only results that contain at least one of the keywords.
    """
    filtered = []
    for result in results:
        for keyword in keywords:
            if keyword.lower() in result.lower():
                filtered.append(result)
                break  # Avoid duplicates if multiple keywords match
    return filtered
# Filter + AI classification logic placeholder
