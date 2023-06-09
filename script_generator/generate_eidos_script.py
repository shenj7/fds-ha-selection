from script_generator import initialize_script
from script_generator import add_population
from script_generator import finish_simulation
from script_generator import add_mutation_effect


def generate_eidos_script(filename, seed, mutation_rate, recombination_rate, selection_coefficient, dominance_coefficient,
                          left_limit, right_limit, population_size, genome_size, output_location):
    """
    Generates eidos script with random sections of
    balancing selection and neutral selection

    Args:
        filename (str): file to write to
        seed (int): seed for randomizer
        mutation_rate (float): mutation rate
    """
    popname = "p1"
    mut1 = "m1"
    mut2 = "m2"
    with open(f"./{filename}", "w+") as script:
        script.write(initialize_script(seed, mutation_rate,
                                       recombination_rate, selection_coefficient, dominance_coefficient,
                                       left_limit, right_limit, genome_size))
        script.write(add_population(popname, population_size))  # how do we want to deal with population names
        script.write(add_mutation_effect(mut1, popname))
        script.write(add_mutation_effect(mut2, popname))
        script.write(finish_simulation(output_location, popname))
