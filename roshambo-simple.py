import unittest

verbose = False

class Roshambo(unittest.TestCase):
  #choices = {0: "rock", 1: "paper", 2: "scissors"}
  choices = {0: "rock", 1: "spock", 2: "paper", 3: "lizard",4: "scissors"}
  player_names = {0: "Tie", 1: "Player A", 2: "Player B"}
  num_choices = len(choices.keys())

  def number_to_name(self,number):
    return self.choices[number]
      
  def name_to_number(self,name):
    for number in self.choices.keys():
      if self.choices[number] == name:
        return number

  """
     Parity of two choices. 
     - If both are even or both are odd, the lowest one wins.
     - If one is odd but the other is not, then the highest one wins
     - Tie if both are the same
  """
  def winner(self,player_choice,computer_choice):
    modulo_res = (player_choice - computer_choice) % self.num_choices
    if modulo_res == 0:
      winning_player_index = 0
    elif 1 <= modulo_res <= (self.num_choices / 2):
      winning_player_index = 1 
    else:
    	winning_player_index = 2
    
    return self.player_names[winning_player_index]

  def simulate_game(self,player_choice_str, computer_choice_str):
    if verbose:
      print "Player A chose:" , player_choice_str
      print "Player B chose:" , computer_choice_str
    winning_player = self.winner(self.name_to_number(player_choice_str), self.name_to_number(computer_choice_str))
    if verbose:
      print "Winner:", winning_player
      print "-------------------------------------------------"

    return winning_player

  def test_rules(self):
    self.assertEqual(self.simulate_game('rock', 'rock'), self.player_names[0])
    self.assertEqual(self.simulate_game('rock', 'scissors'), self.player_names[1])
    self.assertEqual(self.simulate_game('rock', 'paper'), self.player_names[2])
    self.assertEqual(self.simulate_game('rock', 'lizard'), self.player_names[1])
    self.assertEqual(self.simulate_game('rock', 'spock'), self.player_names[2])

    self.assertEqual(self.simulate_game('paper', 'paper'), self.player_names[0])
    self.assertEqual(self.simulate_game('paper', 'scissors'), self.player_names[2])
    self.assertEqual(self.simulate_game('paper', 'lizard'), self.player_names[2])
    self.assertEqual(self.simulate_game('paper', 'spock'), self.player_names[1])

    self.assertEqual(self.simulate_game('scissors', 'lizard'), self.player_names[1])
    self.assertEqual(self.simulate_game('scissors', 'spock'), self.player_names[2])
    self.assertEqual(self.simulate_game('scissors', 'scissors'), self.player_names[0])

    self.assertEqual(self.simulate_game('lizard', 'lizard'), self.player_names[0])
    self.assertEqual(self.simulate_game('lizard', 'spock'), self.player_names[1])

    self.assertEqual(self.simulate_game('spock', 'spock'), self.player_names[0])

    """
    TODO: fix winner check
    self.assertEqual(self.simulate_game('rock', 'rock'), self.player_names[0])
    self.assertEqual(self.simulate_game('scissors', 'rock'), self.player_names[1])
    self.assertEqual(self.simulate_game('paper', 'rock'), self.player_names[2])
    self.assertEqual(self.simulate_game('lizard', 'rock'), self.player_names[1])
    self.assertEqual(self.simulate_game('spock', 'rock'), self.player_names[2])

    self.assertEqual(self.simulate_game('paper', 'paper'), self.player_names[0])
    self.assertEqual(self.simulate_game('scissors', 'paper'), self.player_names[2])
    self.assertEqual(self.simulate_game('lizard', 'paper'), self.player_names[2])
    self.assertEqual(self.simulate_game('spock', 'paper'), self.player_names[1])

    self.assertEqual(self.simulate_game('spock', 'scissors'), self.player_names[1])
    self.assertEqual(self.simulate_game('lizard', 'scissors'), self.player_names[2])
    self.assertEqual(self.simulate_game('scissors', 'scissors'), self.player_names[0])

    self.assertEqual(self.simulate_game('spock', 'lizard'), self.player_names[0])
    self.assertEqual(self.simulate_game('lizard', 'lizard'), self.player_names[1])

    self.assertEqual(self.simulate_game('spock', 'spock'), self.player_names[0])
    """

if __name__ == '__main__':
  unittest.main()

"""
for player_val in range(1,num_choices+1):
  for computer_val in range(1,num_choices+1):
    print "Player:", number_to_name(player_val)
    print "Computer:", number_to_name(computer_val)
    winning_player, winning_choice = winner(player_val, computer_val)
    print "Winner:", winning_player, winning_choice
    print "------------------------------------------"
"""
