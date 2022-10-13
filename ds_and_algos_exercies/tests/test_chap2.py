from ds_and_algos_exercies import chap2 as c2

def test_constructed_flower_instance_serves_inputs_alright():
    """Ensure that Flower instance when initialized have 
    instance members served the appropriate values
    """
    flower = c2.Flower("Hibiscus", 40, 400.10)
    assert flower.get_name() == "Hibiscus"
    assert flower.get_price() == 400.10
    assert flower.get_petal() == 40

def test_update_on_flower_instance_name_changes_previous_value():
    """Ensure that Flower instance previous name is changed
    when a new name is set
    """
    flower = c2.Flower("Hibiscus", 40, 400.10)
    assert flower.get_name() == "Hibiscus"

    # set new name
    flower.set_name("Rose")

    # Ensure flower name is no longer old name
    assert flower.get_name() != "Hibiscus"

    # Ensure flower name now holds new name
    assert flower.get_name() == "Rose"

def test_update_on_flower_instance_price_changes_previous_value():
    """Ensure that Flower instance previous price is changed
    when a new price is set
    """
    flower = c2.Flower("Hibiscus", 10, 40.3)
    assert flower.get_price() == 40.3

    # set new price
    flower.set_price(200)

    # Ensure flower price is no longer old price
    assert flower.get_price() != 40.3

    # Ensure flower price now holds new price
    assert flower.get_price() == 200

def test_update_on_flower_instance_petal_changes_previous_value():
    """Ensure that Flower instance previous petal is changed
    when a new petal is set
    """
    flower = c2.Flower("Hibiscus", 1, 2.10)
    assert flower.get_petal() == 1

    # set new price
    flower.set_petal(2)

    # Ensure flower price is no longer old price
    assert flower.get_petal() != 1

    # Ensure flower price now holds new price
    assert flower.get_petal() == 2
