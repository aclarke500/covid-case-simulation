from Person import Person
import random  # randint is inclusive
import matplotlib.pyplot as plt


print("Welcome to the COVID-19 simulator, enter some arguments or press d for default: ")
# get user input
infection_constant = input("infection constant: ")
# infection_constant = "d"

if infection_constant == "d":
    # defaults if user does not want to specify values
    infection_constant = 1  # average infected person infects x people per day
    inital_infection_size = 1
    sickness_length = 3  # disease lasts two days
    population_size = 10000
    cycle_length = 100
    immunity_length = 12
    immunity_strength = 75  # between 0 and 100

else:

    # average infected person infects x people per day
    infection_constant = float(infection_constant)
    inital_infection_size = input("inital infection_size: ")
    inital_infection_size = int(inital_infection_size)
    sickness_length = input("sickness length: ")  # disease lasts two days
    sickness_length = int(sickness_length)
    population_size = input("population size: ")
    population_size = int(population_size)
    cycle_length = input("cycle length: ")
    cycle_length = int(cycle_length)
    immunity_length = int(input("length of immunity: "))
    # while not (immunity_strength <= 100 and immunity_strength >= 0) or not immunity_strength:
    immunity_strength = int(input("Immunity strength (integer 0-100)"))


population = []

for i in range(population_size):
    # add new person to population
    p = Person()
    # infect some
    if i < inital_infection_size:
        p.infect()

    population.append(p)


def day_during_virus():
    # count number of infected people
    amount_of_people_infected = 0

    for p in population:

        if p.sick:
            amount_of_people_infected += 1

    # how many people to infect
    amount_to_infect = round(infection_constant * amount_of_people_infected)
    # infect n amount of people
    # print("infect", amount_to_infect)
    for i in range(amount_to_infect):
        # we need to infect someone who isn't sick and isn't immune
        found_valid_choice = False
        # if we can't find a choice in 100 tries, we're not infecting someone
        times_spent_finding_choice = 0

        while (not found_valid_choice) and (times_spent_finding_choice <= 5):
            choice = random.randint(0, len(population)-1)
            times_spent_finding_choice += 1

            # we found not sick person
            if not population[choice].sick:

                found_valid_choice = True
                # if they don't have immunity, infect them
                if not population[choice].immune:
                    population[choice].infect()

                else:
                    immunity_choice = random.randint(0, 100)

                    if immunity_choice > immunity_strength:

                        population[choice].infect()

                # a sick person infects x amount of people, if they are immune we don't re infect them

    # increment sick days and heal people
    for p in population:
        if p.sick:
            p.days_spent_sick += 1
        # after sickness length heal a person
        if p.sick and (p.days_spent_sick > sickness_length):
            p.heal()

        if p.immune:
            # cycle immunity count
            p.day()
            if p.days_since_recovery > immunity_length:
                p.immune = False

    return


def count_infected():
    infected = []

    for i in range(len(population)-1):
        if population[i].sick:
            infected.append(population[i])

    return(len(infected))


def count_immune():
    immune = []
    for i in range(len(population)-1):

        if population[i].immune:
            immune.append(population[i])

    return len(immune)

# cycles through the days and runs the simulation
def cycle(n):
    # amount of people sick at a given day
    sick_count = []
    immune_count = []

    print("Population = ", population_size)
    for i in range(n):

        sick_count.append(count_infected())
        immune_count.append(count_immune())
        day_during_virus()

    for i in range(len(sick_count)):

        print("Day: ", i, " Current infected: ", sick_count[i])

    return [sick_count, immune_count]


# run the simuloation to collect data
data = cycle(cycle_length)

# we will plot the respective days as the x values
days = []

for i in range(cycle_length):
    days.append(i)

x_values = days

# add labels
plt.xlabel("Day")
plt.ylabel("Number of people")

# give each scatter a name for the legend
sick=plt.scatter(x_values, data[0], color='k', s=5)
immune=plt.scatter(x_values, data[1], color='g', s=3)
# append legend
plt.legend((sick, immune),("Sick people", "Immune people"))

plt.title("Cases vs immunity overtime")
# plot
plt.plot(x_values,data[0], color='k')
plt.plot(x_values, data[1], color='g')
plt.show()


