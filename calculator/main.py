from calculator.train_gen import gen_train
import random

# Configs so I can easily change like settings later
train_data_amnt = 100 # At 1k it can't seem to get 100% accuracy, besides at 100 amnt it still outputs the right thing
bias = round(random.uniform(0, 1), 2)
train_data = gen_train(train_data_amnt)
learn_rate = 0.000001 # Lowk wanna make this like uhh change constantly like at first high learn rate then over time lower and lower just to get it to perfection but for now ts good
target_acu = 100
# Give the neurons a random starting weight cuz yea
weights = []
for i in range(4):
    weights.append(round(random.uniform(0, 1), 2))

# Target net: 6 Input, 4 hidden, 6 output
# Currently its just one neuron tho: Inputs -> [NEURON] -> Output
def ai_wannabe():
    def neuron():
        """
        This is one neuron,
        It returns prediction + bias
        Prediction = Σ(inputᵢ × weightᵢ)
        Basically add all the corresponding input * weights together.
        """
        prediction = 0
        for input_num in range(len(inputs)):
            prediction += float(inputs[input_num]) * float(weights[input_num])
        return prediction + bias
    epoch = 0
    while True:
        epoch += 1
        correct = 0
        for example in range(len(train_data)):
            inputs = train_data[example].split(" = ")[0].split(",")
            target = float(train_data[example].split(" = ")[1])
            prediction = neuron()
            loss = target - prediction

            for i in range(len(weights)):
                weights[i] += loss * float(inputs[i]) * learn_rate
                # Change the weights based on lost times inputs times learn rate, why? Idk
                # Actually ik now so heres a docstring
                """
                Suppose you have
                
                Target = 50
                Prediction = 40
                Loss = Target - Prediction so 10
                So the neuron has to bump its thing up thats all it knows make it higher, 
                Different weights affect the prediction by different amounts depending on input.
                Thus:
                Loss x Input x Learn Rate
                determines how much to add to the weights.
                So say you have these configs
                
                Input = 10, 10, 20, 10
                Target = -10
                Prediction = -20
                Loss = 10
                Learn Rate = 0.000001
                weights = 0.5, 0.3, 0.7, 0.2
                
                let x = Num to be added to weights
                
                x = Loss * Input * Learn Rate
                x = 10 * 10, 10, 20, 10 * 0.000001
                x = 0.0001, 0.0001, 0.0002, 0.0001
                
                so weights = 0.5, 0.3, 0.7, 0.2 + 0.0001, 0.0001, 0.0002, 0.0001
                weights = 0.5001, 0.3001, 0.7002, 0.2001
                """
            prediction = neuron()
            loss = target - prediction
        for example in range(len(train_data)):
            inputs = train_data[example].split(" = ")[0].split(",")
            target = float(train_data[example].split(" = ")[1])

            prediction = neuron()

            if round(prediction) == target:
                correct += 1
        accuracy = correct / len(train_data) * 100
        print(f"\nEpoch {epoch}")
        print(f"Loss: {loss}")
        print(f"Accuracy: {accuracy:.2f}%")
        if accuracy >= target_acu:
            break
    while True:

        inputs = input("Enter 4 numbers with 2 digits, separate with coma: ").split(",")
        if inputs == "exit":
            break
        prediction = neuron()
        prediction = round(prediction)

        print(f"Prediction: {prediction}")
        print(f"Expected:  {(int(inputs[0]) + int(inputs[1])) - (int(inputs[2]) + int(inputs[3]))}")
        print(f"Operation done: ({int(inputs[0])} + {int(inputs[1])}) - ({int(inputs[2])} + {int(inputs[3])})")


ai_wannabe()

