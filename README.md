microservice tracks and updates the high score, using json files to communicate

request instructions:
you can create a json file named request.json to communicate and the file needs
2 parameters
  * streak
      - should be an integer
      - represents the current streak of correct answers
  * action
      - should also be an integer
      - this one determines the behavior of the microservice. 0 = save streak as
        high score if it's greater than the current high score. 1 = request the
        current high score
        
example json request:
{
"streak": 23,
"action": 1
}

json file should be in the same directory as this microservice. this microservice does
requests sequentially so only one request should be present at a time


response instructions:
when the action parameter is set to 1, then the microservice will create a json file 
named response.json and that file will have the current high score. 

steps to receive:
* after sending request with action set to 1, wait for response.json file to appear
* read the high score from the response.json file
* delete the response.json afterward to make sure new responses can be created

example json response file:
{
  "high_score": 25
}

no response.json will be created if action is set to 0
