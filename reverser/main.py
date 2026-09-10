from reverser.train_gen import gen_train
import random

# Configs so I can easily change like settings later
train_data_amnt = 100
bias = round(random.uniform(0, 1), 2)
train_data = gen_train(train_data_amnt)
learn_rate = 0.00001  # Lowk wanna make this like uhh change constantly like at first high learn rate then over time lower and lower just to get it to perfection but for now ts good
target_acu = 100
# Give the neurons a random starting weight cuz yea
hid_weights = []
for neuron in range(6):
    weights = []
    for i in range(6):
        weights.append(random.uniform(-0.1, 0.1))
    hid_weights.append(weights)

out_weights = []
for neuron in range(6):
    weights = []
    for i in range(6):
        weights.append(random.uniform(-0.1, 0.1))
    out_weights.append(weights)

# Network is: 6 Input, 6 hidden, 6 output
# It does practically the same thing as in calculator\main.py but with more weights and neurons.
def ai_wannabe():
    def neuron():
        hid_out = []
        # Create the hidden predictions first (Not final prediction)
        for weight in hid_weights:
            prediction = 0
            for i in range(6):
                prediction += inputs[i] * weight[i]

            hid_out.append(prediction)
        outputs = []
        # Then created actual prediction from that hidden prediction
        for weights in out_weights:
            prediction = 0
            for i in range(6):
                prediction += hid_out[i] * weights[i]
            outputs.append(prediction)
        return hid_out, outputs
    epochs = 0
    while True:
        epochs += 1
        correct = 0
        for example in range(len(train_data)):
            word, target = train_data[example].split(" : ")
            inputs = [ord(char) - ord("A") for char in word]
            target = [ord(char) - ord("A") for char in target]
            hid_out, prediction = neuron()
            loss = [target[i] - prediction[i] for i in range(6)]

            for out_num in range(6):
                for hid_num in range(6):
                    out_weights[out_num][hid_num] += loss[out_num] * hid_out[hid_num] * learn_rate

            hid_loss = []
            for hidden_num in range(6):
                error = 0
                for out_num in range(6):
                    error += loss[out_num] * out_weights[out_num][hidden_num]
                hid_loss.append(error)
            for hid_num in range(6):
                for input_num in range(6):
                    hid_weights[hid_num][input_num] += hid_loss[hid_num] * inputs[input_num] * learn_rate

            hid_out, prediction = neuron()
            loss = [target[i] - prediction[i] for i in range(6)]
        for example in range(len(train_data)):
            word, target = train_data[example].split(" : ")
            inputs = [ord(char) - ord("A") for char in word]
            target = [ord(char) - ord("A") for char in target]
            hid_out, prediction = neuron()

            if all(round(prediction[i]) == target[i] for i in range(6)):
                correct += 1
            accuracy = correct / len(train_data) * 100
        print(f"\nEpoch {epochs}")
        print(f"Loss: {loss}")
        print(f"Accuracy: {accuracy:.2f}%")
        if accuracy >= target_acu:
            break

    while True:
        word = input("Enter a 6-letter word: ").upper()
        if word == "EXIT":
            break
        if len(word) != 6:
            print("Invalid input | WORD MUST BE 6 LETTERS")
            continue
        if any(char.isdigit() for char in word):
            print("Invalid input | INPUT MUST NOT CONTAIN NUMBERS")
            continue

        inputs = [ord(char) - ord("A") for char in word]
        hid_out, prediction = neuron()
        prediction = ''.join(chr(round(value) + ord("A")).lower()for value in prediction)

        print(f"Prediction: {prediction}")
        print(f"Expected: {word[::-1].lower()}")
ai_wannabe()

