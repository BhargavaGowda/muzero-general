import muzero

game = muzero.MuZero("connect4")
game.load_model(checkpoint_path="/home/bhargava/MuZero/muzero-general/results/connect4/2020-10-27--12-53-02/model.checkpoint")
result = game.test(render=False,opponent="random",muzero_player=0,num_tests=100)
print(result)