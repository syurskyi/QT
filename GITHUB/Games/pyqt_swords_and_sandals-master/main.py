import sys
from PyQt5 import QtWidgets
from gui import Ui_MainWindow
from random import randint

def start_game(game_data, ui):
    ui.light_attack_button.clicked.connect(game_data.light_attack)
    ui.heavy_attack_button.clicked.connect(game_data.heavy_attack)
    ui.block_button.clicked.connect(game_data.block)
    ui.dodge_button.clicked.connect(game_data.dodge)
    ui.sleep_button.clicked.connect(game_data.sleep)
    ui.taunt_button.clicked.connect(game_data.taunt)


class GameData:
    def init_game_state(self):
        self.round_number = 1

        # First player is being chosen by dice roll
        self.current_player = randint(1, 2)

        self.players_health = [100, 100]
        self.players_health_regen = [1,1]

        self.players_stamina = [100, 100, 100]
        self.players_stamina_regen = [2,2]

        self.players_resistances = [0, 0]
        self.players_regen_modifiers = [1, 1]

        self.players_cooldowns = [0, 0]

        self.game_actions_data = ["The battle has started!",
                                  "Player %d has the first move!" % self.current_player]


    def __init__(self, ui_reference):
        self.init_game_state()

        self.stamina_cost_light = 15
        self.stamina_cost_high = 35
        self.stamina_cost_block = 25
        self.stamina_cost_dodge = 45

        self.ui = ui_reference

        self.taunt_messages = ["Oof! That fiery insult will continue to hurt player's %d feelings for %d turns!",
                               "Damn! Player's %d butthurt will last for %d turns!",
                               "In spite of recent revelations about his mother, player %d will regenerate slowly for %d turns!"]

        self.sleep_messages = ["Player %d has taken a rest for a moment of %d turns.",
                               "Player %d got some of his beauty sleep and will continue to regenerate faster for %d turns!",
                               "Played %d is now full of energy and will regenerate faster for %d turns!"]

        self.light_attack_messages = ["Player %d attacks for %d damage!",
                                      "Player %d swings his sword and deals %d damage!",
                                      "Playes %d slashes his opponent for %d damage!"]

        self.heavy_attack_messages = ["A fine thrust! Played %d impales his opponent for %d damage!",
                                      "A masterful blow by player %d takes %d life points from his enemy!",
                                      "This wound will never fully heal! Player %d strikes for %d damage!"]

        self.block_messages = ["Player %d raises his guard and awaits the attack.",
                               "Player's %d body is ready.",
                               "Player %d is ready to parry!"]

        self.dodge_messages = ["Player %d lowers his guard and prepares to dodge.",
                               "Player %d prepares his feet for the dance with death.",
                               "Player %d prepares to leap as soon as the attack comes."]

        self.victory_messages = ["Omae wa mou shindeiru! Player %d impales his enemy with his bare fist after %d rounds of fierce duel!",
                                "Player %d achieves victory as he beheads his opponent and dances on his corpse after %d round of fighting!",
                                "Player %d brutally desecrates his opponent's corpse after %d of bloody ravage!"]


    def restart(self):
        self.game_won()
        self.init_game_state()
        start_game(self, self.ui)

        self.ui.player1_action_icon.clear()
        self.ui.player2_action_icon.clear()
        self.update_ui()


    def update_ui(self):
        self.ui.round_counter.setText("ROUND %d" % self.round_number)
        self.ui.player_indicator.setText("Player %d" % self.current_player)
        self.ui.player1_hp.setValue(self.players_health[0])
        self.ui.player2_hp.setValue(self.players_health[1])
        self.ui.player1_stamina.setText("%d/%d AP" % (self.players_stamina[0], self.players_stamina[2]))
        self.ui.player2_stamina.setText("%d/%d AP" % (self.players_stamina[1], self.players_stamina[2]))
        self.ui.game_actions_informer.setText("\n".join(self.game_actions_data))
        self.game_actions_data = []


    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1


    def regenerate_players_health_and_stamina(self):
        for i in range(0, 2):
            self.players_health[i] = self.players_health[i] + (self.players_health_regen[i] * self.players_regen_modifiers[i])
            if self.players_health[i] > 100:
                self.players_health[i] = 100
            self.players_stamina[i] = self.players_stamina[i] + (
                        self.players_stamina_regen[i] * self.players_regen_modifiers[i])
            if self.players_stamina[i] > 100:
                self.players_stamina[i] = 100

            # If player regen effects cooldown, decrease them  by one
            if self.players_cooldowns[i] > 0:
                self.players_cooldowns[i] -= 1

                # If player's regen effects cooldown is equal to zero, effect has worn off
                # Thus it is set to 0 again
                if self.players_cooldowns[i] == 0 and self.players_regen_modifiers[i] != 0:
                    self.players_regen_modifiers[i] = 0
                    self.game_actions_data.append("Player's %d regeneration effects has worn out." % (i + 1))
                else:
                    self.game_actions_data.append(
                        "Player's %d regeneration effects will continue for next %d rounds." % (
                        (i + 1), self.players_cooldowns[i]))



    def next_round(self):
        # Increment round counter and switch player
        # or end game if one of the player has HP lesser or equal to 0
        if self.players_health[0] <= 0 or self.players_health[1] <= 0:
            self.update_ui()
            self.game_won()
        else:
            self.regenerate_players_health_and_stamina()
            self.round_number = self.round_number + 1
            self.switch_player()
            self.update_ui()


    def decrease_attacked_player_health(self, stamina_cost, min_dmg, max_dmg, heavy=False):
        attacked_player = self.current_player % 2

        # Calculate dealt damage by getting random damage value and decreasing it by percentage of player dmg reduction
        base_dmg = randint(min_dmg, max_dmg)
        dealt_dmg = base_dmg - int(self.players_resistances[attacked_player] * base_dmg)

        # If player had dmg reduction effect, set it as zero
        if self.players_resistances[attacked_player] != 0:
            self.players_resistances[attacked_player] = 0

        self.players_health[attacked_player] = self.players_health[attacked_player] - dealt_dmg
        if self.players_health[attacked_player] < 0:
            self.players_health[attacked_player] = 0

        self.players_stamina[self.current_player - 1] = self.players_stamina[self.current_player - 1] - stamina_cost

        if heavy:
            self.game_actions_data.append(self.heavy_attack_messages[randint(0, 2)] % (self.current_player, dealt_dmg))
        else:
            self.game_actions_data.append(self.light_attack_messages[randint(0, 2)] % (self.current_player, dealt_dmg))

        self.next_round()


    def display_attack_icon(self, heavy):
        if self.current_player == 1:
            self.ui.player2_action_icon.setPixmap(self.ui.attack2_icons[heavy])
        else:
            self.ui.player1_action_icon.setPixmap(self.ui.attack1_icons[heavy])


    def display_action_icon(self, action_id):
        # 0 for block, 1 for dodge, 2 for taunt, 3 for sleep
        if self.current_player == 1:
            self.ui.player1_action_icon.setPixmap(self.ui.action_icons[action_id])
        else:
            self.ui.player2_action_icon.setPixmap(self.ui.action_icons[action_id])


    def light_attack(self):
        # Calculate and save dealt damage if the attacking player has enough stamina to perform the attack
        if self.players_stamina[self.current_player - 1] - self.stamina_cost_light >= 0:
            self.decrease_attacked_player_health(self.stamina_cost_light, 5, 20, False)
            self.display_attack_icon(0)
        # If player doesn't have enough stamina, action will not be performed
        else:
            pass


    def heavy_attack(self):
        # Calculate and save dealt damage if the attacking player has enough stamina to perform the attack
        if self.players_stamina[self.current_player - 1] - self.stamina_cost_high >= 0:
            self.decrease_attacked_player_health(self.stamina_cost_high, 25, 40, True)
            self.display_attack_icon(1)
        # If player doesn't have enough stamina, action will not be performed
        else:
            pass


    def block(self):
        if self.players_stamina[self.current_player - 1] - self.stamina_cost_block >= 0:
            self.players_resistances[self.current_player - 1] = 0.4

            self.players_stamina[self.current_player - 1] = self.players_stamina[self.current_player - 1] - self.stamina_cost_block

            self.game_actions_data.append(self.block_messages[randint(0, 2)] % self.current_player)

            self.display_action_icon(0)
            self.next_round()
        # If player doesn't have enough stamina, action will not be performed
        else:
            pass


    def dodge(self):
        if self.players_stamina[self.current_player - 1] - self.stamina_cost_dodge >= 0:
            self.players_resistances[self.current_player - 1] = 0.8

            self.players_stamina[self.current_player - 1] = self.players_stamina[self.current_player - 1] - self.stamina_cost_dodge

            self.game_actions_data.append(self.dodge_messages[randint(0, 2)] % self.current_player)

            self.display_action_icon(1)
            self.next_round()
        # If player doesn't have enough stamina, action will not be performed
        else:
            pass


    def taunt(self):
        if self.players_regen_modifiers[self.current_player % 2] > 0:
            self.players_regen_modifiers[self.current_player % 2] = 0.5
        else:
            self.players_regen_modifiers[self.current_player % 2] = 0

        self.players_cooldowns[self.current_player % 2] = 4
        self.game_actions_data.append(self.taunt_messages[randint(0, 2)] % ((self.current_player % 2) + 1, self.players_cooldowns[self.current_player % 2]))

        self.display_action_icon(2)
        self.next_round()


    def sleep(self):
        self.players_regen_modifiers[self.current_player - 1] = 2
        if self.players_regen_modifiers[self.current_player - 1] < 0:
            self.players_regen_modifiers[self.current_player - 1] = 0
        else:
            self.players_regen_modifiers[self.current_player - 1] = 2

        self.players_cooldowns[self.current_player - 1] = 4
        self.game_actions_data.append(self.sleep_messages[randint(0, 2)] % (self.current_player, self.players_cooldowns[self.current_player - 1]))

        self.display_action_icon(3)
        self.next_round()


    def game_won(self):
        self.ui.light_attack_button.disconnect()
        self.ui.heavy_attack_button.disconnect()
        self.ui.dodge_button.disconnect()
        self.ui.taunt_button.disconnect()
        self.ui.sleep_button.disconnect()
        self.ui.block_button.disconnect()

        self.ui.round_counter.setText("GAME OVER!")
        self.ui.game_actions_informer.setText((self.victory_messages[randint(0, 2)] % (self.current_player, self.round_number)))


# Main function
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Rowu Efforutu")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(750, 790)

    # Initiate game data
    game_data = GameData(ui)

    # Call update ui method of GameData class to provide GUI with initial player's state
    game_data.update_ui()

    # Connect GUI buttons to their receiver methods in GameData class
    ui.restart_button.clicked.connect(game_data.restart)
    start_game(game_data, ui)

    # Setup graphics
    ui.background_image.setPixmap(ui.sprite_background)
    ui.player1_sprite.setPixmap(ui.sprite1)
    ui.player2_sprite.setPixmap(ui.sprite2)

    # Set main window title
    MainWindow.setWindowTitle("Rowu Efforutu")
    MainWindow.show()

    sys.exit(app.exec_())