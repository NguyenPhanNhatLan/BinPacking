from utils.input_handler import load_items_from_excel
from services.container_loader import create_container
from services.packer_service import OptimizerService

def main():
    items = load_items_from_excel('/Users/nhatlan/Downloads/TestData.xlsx')
    container = create_container(length=200, width=200, height=250, max_weight=1000)

    config = {
        "algorithm": "ga",
        "population_size": 50,
        "generations": 100,
        "mutation_rate": 0.1,
        "crossover_rate": 0.8,
        "selection_size": 3
    }

    optimizer = OptimizerService(algorithm=config['algorithm'])
    best_solution = optimizer.run(items= items, container= container, config=config)
    # In kết quả
    print("===> BEST SOLUTION:")
    print(best_solution)
if __name__ == "__main__":
    main()