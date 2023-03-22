from classes.Spotify import Spotify
from functions.util import getSongTitlesFromFile, inicializarObjetosSong, printarMusicas, printarMusicasPopulation, removerMusicasRepetidas
from functions.algoritmogenetico import create_individual, crossover, mutate, fitness_function, select_parents_roulette
import random

spotify_manager = Spotify()

file_path = "data/songs.txt"

song_titles = getSongTitlesFromFile(file_path)

songs = inicializarObjetosSong(song_titles, spotify_manager)

# printarMusicas(songs)

# representação cromossomica
# danceability, energy and valence.

playlists = [
    {'nome': 'Feliz', 'danceability': 0.75, 'energy': 0.9, 'valence': 1},
    {'nome': 'Triste', 'danceability': 0.25, 'energy': 0.2, 'valence': 0},
    {'nome': 'Festa', 'danceability': 1, 'energy': 1, 'valence': 0.87525}
]

POPULATION_SIZE = 90 #Testar com tamanho menor
MUTATION_RATE = 0.01
GENERATIONS = 1000 #Testar com menos geracoes

for playlist in playlists:
    population = [create_individual(songs) for i in range(POPULATION_SIZE)]
    # executa o algoritmo genético por um número fixo de gerações
    for generation in range(GENERATIONS):
        
        parent1, parent2 = select_parents_roulette(population, playlist)
        filho1, filho2 = crossover(parent1, parent2)
        filho1 = mutate(filho1, MUTATION_RATE)
        filho2 = mutate(filho2, MUTATION_RATE)

        # adiciona os novos indivíduos à população
        population.extend([filho1, filho2])

        # seleciona os melhores indivíduos para a próxima geração
        population = sorted(population, key=lambda x: fitness_function(
            x, [playlist]), reverse=True)[:POPULATION_SIZE]

        # exibe o melhor indivíduo da geração atual
        # print('Generation {}: Best fitness = {}'.format(generation+1, fitness_function(population[0], playlists)))
    best_individual = max(
        population, key=lambda x: fitness_function(x, [playlist]))
    removerMusicasRepetidas(best_individual)
    print(playlist['nome'])
    printarMusicasPopulation(best_individual)
    print('\n')
    # printarMusicas(population[0])


# for playlist in playlists:
#     population = [create_individual(songs) for i in range(POPULATION_SIZE)]
#     # executa o algoritmo genético por um número fixo de gerações
#     for generation in range(GENERATIONS):
#         # calcula o fitness de cada indivíduo na população
#         fitness_scores = [fitness_function(
#             individual, [playlist]) for individual in population]

#         # seleciona os melhores indivíduos para reprodução
#         parents = random.choices(population, weights=fitness_scores, k=2)

#         # realiza crossover e mutação para gerar novos indivíduos
#         filho1, filho2 = crossover(parents[0], parents[1])
#         filho1 = mutate(filho1, MUTATION_RATE)
#         filho2 = mutate(filho2, MUTATION_RATE)

#         # adiciona os novos indivíduos à população
#         population.extend([filho1, filho2])

#         # seleciona os melhores indivíduos para a próxima geração
#         population = sorted(population, key=lambda x: fitness_function(
#             x, [playlist]), reverse=True)[:POPULATION_SIZE]

#         # exibe o melhor indivíduo da geração atual
#         # print('Generation {}: Best fitness = {}'.format(generation+1, fitness_function(population[0], playlists)))
#     best_individual = max(
#         population, key=lambda x: fitness_function(x, [playlist]))
#     removerMusicasRepetidas(best_individual)
#     print(playlist['nome'])
#     printarMusicasPopulation(best_individual)
#     print('\n')
#     # printarMusicas(population[0])
