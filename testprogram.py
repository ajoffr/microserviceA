import json
import time
import os

# Paths to JSON files
input_file = "request.json"
output_file = "response.json"



def send_request(streak, action):
    with open(input_file, "w") as file:
        json.dump({"streak": streak, "action": action}, file)


def receive_response():
    while not os.path.exists(output_file):
        time.sleep(1)
    with open(output_file, "r") as file:
        response = json.load(file)
    os.remove(output_file)
    return response


# saving a high score
print("Sending streak 10 with action 0 (save high score)...")
send_request(10, 0)
time.sleep(2)

# retrieving the high score
print("Sending action 1 (get high score)...")
send_request(0, 1)
response = receive_response()
print("High score received:", response["high_score"])
