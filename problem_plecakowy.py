import random
import tkinter as tk
from tkinter import messagebox

# --- Parametry algorytmu ---
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.2
POPULATION_SIZE = 50
MAX_GENERATIONS = 100

# --- Reprezentacja przedmiotów ---
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# --- Fitness funkcja ---
def fitness(chromosome, items, max_weight):
    total_weight = 0
    total_value = 0
    for gene, item in zip(chromosome, items):
        if gene == 1:
            total_weight += item.weight
            total_value += item.value
    if total_weight > max_weight:
        return 0  # osobnik niedozwolony
    return total_value

# --- Inicjalizacja populacji ---
def generate_population(size, item_count):
    return [[random.randint(0, 1) for _ in range(item_count)] for _ in range(size)]

# --- Selekcja ruletkowa ---
def roulette_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choice(population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return individual

# --- Krzyżowanie ---
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_PROB:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

# --- Mutacja ---
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_PROB:
            chromosome[i] = 1 - chromosome[i]

# --- Główna funkcja GA ---
def genetic_algorithm(items, max_weight):
    population = generate_population(POPULATION_SIZE, len(items))
    best_solution = None
    best_fitness = 0

    for generation in range(MAX_GENERATIONS):
        fitnesses = [fitness(ind, items, max_weight) for ind in population]

        # znajdź najlepszego osobnika
        for ind, fit in zip(population, fitnesses):
            if fit > best_fitness:
                best_fitness = fit
                best_solution = ind

        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = roulette_selection(population, fitnesses)
            parent2 = roulette_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population[:POPULATION_SIZE]

    return best_solution, best_fitness

# --- GUI ---
class KnapsackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorytm Genetyczny - Problem Plecakowy")

        self.items = []

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Wartość:").grid(row=0, column=0)
        tk.Label(self.input_frame, text="Waga:").grid(row=0, column=1)

        self.value_entry = tk.Entry(self.input_frame)
        self.weight_entry = tk.Entry(self.input_frame)
        self.value_entry.grid(row=1, column=0)
        self.weight_entry.grid(row=1, column=1)

        tk.Button(self.input_frame, text="Dodaj przedmiot", command=self.add_item).grid(row=1, column=2, padx=5)
        tk.Button(self.input_frame, text="Usuń zaznaczony", command=self.remove_item).grid(row=1, column=3, padx=5)

        self.items_listbox = tk.Listbox(root, width=60)
        self.items_listbox.pack(pady=5)

        self.max_weight_label = tk.Label(root, text="Maksymalna waga plecaka:")
        self.max_weight_label.pack()
        self.max_weight_entry = tk.Entry(root)
        self.max_weight_entry.pack()

        tk.Button(root, text="Rozwiąż", command=self.solve).pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_item(self):
        try:
            value = int(self.value_entry.get())
            weight = int(self.weight_entry.get())
            self.items.append(Item(value, weight))
            self.items_listbox.insert(tk.END, f"Wartość: {value}, Waga: {weight}")
            self.value_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawne liczby całkowite.")

    def remove_item(self):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.items.pop(index)
            self.items_listbox.delete(index)
        else:
            messagebox.showinfo("Informacja", "Zaznacz przedmiot do usunięcia.")

    def solve(self):
        try:
            max_weight = int(self.max_weight_entry.get())
            solution, total_value = genetic_algorithm(self.items, max_weight)
            selected_items = [f"{i+1}" for i, bit in enumerate(solution) if bit == 1]
            result_text = f"Wybrane przedmioty: {', '.join(selected_items)}\nŁączna wartość: {total_value}"
            self.result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawną maksymalną wagę.")


if __name__ == '__main__':
    root = tk.Tk()
    app = KnapsackApp(root)
    root.mainloop()
