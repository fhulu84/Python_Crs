import random

def play(p1, p2):
  move1 = p1["moves"][-1]
  move2 = p2["moves"][-1]

  if move1 == 'rock':
    if move2 == 'scissors':
      p1['score'] += 1
    elif move2 == 'paper':
      p2['score'] += 1
  elif move1 == 'scissors':
    if move2 == 'rock':
      p2['score'] += 1
    elif move2 == 'paper':
      p1['score'] += 1
  elif move1 == 'paper':
    if move2 == 'rock':
      p2['score'] += 1
    elif move2 == 'scissors':
      p1['score'] += 1
  

player1 = {
  "moves": [],
  "score": 0
}

player2 = {
  "moves": [],
  "score": 0
}

moves = ['rock', 'paper', 'scissors']

for p in range(1, 6):
  # SET MOVES
  player1["moves"].append(random.choice(moves))
  player2["moves"].append(random.choice(moves))
  #PLAY
  play(player1, player2)

print(f'GAME SCORE: {player1["score"]} - {player2["score"]}')
if player1["score"] > player2["score"]:
  print('PLAYER1 won the game')
elif player1["score"] < player2["score"]:
  print('PLAYER2 won the game')
else:
  print('No winner')

print()
print(f'Player1: {player1}')
print(f'Player2: {player2}')
