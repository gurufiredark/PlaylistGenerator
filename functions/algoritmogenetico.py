import random


def fitness_function(individual, playlists):
    
    #Função que calcula o fitness de um indivíduo da população.
    #O fitness é calculado como a média ponderada da distância de cada música
    #em relação às playlists desejadas, considerando os atributos 'danceability',
    #'energy' e 'valence'.
    
    total_fitness = 0

    for playlist in playlists:
        playlist_fitness = 0
        for song in individual:
            song_fitness = 0
            for atributo in ['danceability', 'energy', 'valence']:
                playlist_atributo = playlist[atributo]
                song_atributo = song.getAtributo(atributo)
                song_fitness += abs(playlist_atributo - song_atributo)
            playlist_fitness += song_fitness
        total_fitness += (1 / playlist_fitness)

    return total_fitness

def create_individual(songs):

    #Função que cria um indivíduo da população, ou seja, uma combinação de músicas.
    return random.sample(songs, len(songs))


def crossover(individual1, individual2):
    # Escolhe um ponto de corte aleatório para a troca de material genético
    divisao_de_corte= random.randint(0, len(individual1) - 1)
    
    # Realiza a troca de material genético entre os indivíduos
    new_individual1 = individual1[:divisao_de_corte] + individual2[divisao_de_corte:]
    new_individual2 = individual2[:divisao_de_corte] + individual1[divisao_de_corte:]
    
    return new_individual1, new_individual2

def mutate(individual, mutation_rate):
    # Percorre cada música no indivíduo
    for i in range(len(individual)):
        # Escolhe aleatoriamente se vai ocorrer uma mutação nesta música
        if random.random() < mutation_rate:
            # Escolhe aleatoriamente um atributo para mutar (danceability, energy ou valence)
            atributo = random.choice(['danceability', 'energy', 'valence'])
            # Adiciona um valor aleatório pequeno (-0.05 a 0.05) ao atributo mutado
            valor_aux=individual[i].getAtributo(atributo)+random.uniform(-0.05, 0.05)
            individual[i].setAtributo(atributo, valor_aux)
            # Garante que o atributo mutado permaneça no intervalo [0, 1]
            individual[i].setAtributo(atributo, max(0, min(1, individual[i].getAtributo(atributo))))
    
    return individual

def select_parents_roulette(population, playlist):
    fitnesses = [fitness_function(individual, [playlist]) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    parent1 = random.choices(population, weights=probabilities)[0]
    parent2 = random.choices(population, weights=probabilities)[0]
    return parent1, parent2