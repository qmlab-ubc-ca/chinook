from chinook import atomic_mass, electron_configs


def test_atomic_mass_table():
    assert atomic_mass.get_mass_from_number(6) == 12.0107
    assert atomic_mass.get_el_from_number(6) == "C"
    assert atomic_mass.get_num_from_el("C") == 6


def test_electron_configuration_table():
    assert electron_configs.get_con(electron_configs.filename, 6) == "1s22s22p2"
