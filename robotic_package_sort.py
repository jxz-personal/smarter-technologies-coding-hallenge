def sort(width, height, length, mass):
    """
    Sorts packages based on dimensions and mass.
    
    Criteria:
    - Bulky: Volume >= 1,000,000 cm³ OR any dimension >= 150 cm.
    - Heavy: Mass >= 20 kg.
    
    Returns:
    - STANDARD: Neither bulky nor heavy.
    - SPECIAL: Either bulky or heavy (but not both).
    - REJECTED: Both bulky and heavy.
    """
    
    # Calculate volume
    volume = width * height * length
    
    # Determine attributes
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20
    
    # Logic for dispatching
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    
    return "STANDARD"