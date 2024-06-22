from .game import GameBoard, GameCheckerStatus, GameInterface, GameControls
import pygame

__version__ = "0.2.0"


def start(b_pos=[(2,0), (4, 0), (6, 0), (8, 0), (3, 1), (5, 1), (7, 1), (9, 1), (2, 2), (4, 2), (6, 2), (8, 2)], 
          w_pos=[(3, 7), (5, 7), (7, 7), (9, 7), (2, 6), (4, 6), (6, 6), (8, 6), (3, 5), (5, 5), (7, 5), (9, 5)], 
          b_types=["man"] * 12, 
          w_types=["man"] * 12,
          b_capt_pos=[],
          w_capt_pos=[],
          b_capt_types=[],
          w_capt_types=[]):
    
    pygame.init()
    pygame.display.set_caption("Checkers - Advanced Coding Project")

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000

    """Initializing Classes"""
    black_checkers = GameCheckerStatus(b_pos, b_types, b_capt_pos, b_capt_types)
    white_checkers = GameCheckerStatus(w_pos, w_types, w_capt_pos, w_capt_types)
    gb = GameBoard(black_checkers, white_checkers, SCREEN_WIDTH, SCREEN_HEIGHT, 0.65)
    gc = GameControls(gb.get_square_space(), black_checkers, white_checkers)
    gb.post_init(game_controls=gc)

    """Initializing Default GUI Settings"""
    screen = pygame.display.set_mode(gb.get_board_size())
    clock = pygame.time.Clock()
    running = True
    

    while running:
        gb.render_game_env(screen)
        gc.render_selection(screen)
        gb.render_winner(screen)

        """Initialize variables in outer while loop"""
        selection = gc.return_selection()
        p2_cords = gc.get_player_2_cords()
        p1_cords = gc.get_player_1_cords()
        current_player = gc.get_current_player()
        valid_options = gc.return_authorized_positions()
        life_cycle_hook = gc.get_life_cycle_hook()
        select_cord = gc.select_cord


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_cord = (event.pos[0] // gb.get_square_size(), event.pos[1] // gb.get_square_size())
                gc.select_cord = clicked_cord

                """ ---------- UNCOMMENT TO DEBUG ---------- """
                print("\n\n")
                print("<----- DEBUG STATEMENTS ----->")
                print("\n\n")
                print(f"Black piece positions: {black_checkers.pos}")
                print(f"Black piece types: {black_checkers.types}")
                print(f"Black has captured(pos): {black_checkers.capt_pos}")
                print(f"Black has captured(type){black_checkers.capt_types}")
                print("\n")
                print(f"White piece positions: {white_checkers.pos}")
                print(f"White piece types: {white_checkers.types}")
                print(f"White has captured(pos): {white_checkers.capt_pos}")
                print(f"White has captured(type){white_checkers.capt_types}")
                print("\n")
                print(f"Selection coordinates (previous): {select_cord}")
                print(f"Selection coordinates (current): {gc.select_cord}")
                print(f"Valid Moves{valid_options}")
                print("\n\n")
                print("<----- DEBUG STATEMENTS ----->")
                """ ---------- UNCOMMENT TO DEBUG ---------- """

                """Check if its is player 1's turn to select"""
                if current_player == "p1":
                    if clicked_cord in p1_cords:
                        gc.lch["p1"]["selected"] = True
                        gc.lch["p2"]["moved"] = False

                """Check if player 1 has selected a piece and if player can move"""
                if life_cycle_hook["p1"]["selected"]:
                    if gc.select_cord in  valid_options:
                        """Initialize possible capture positions"""
                        r_d =  (select_cord[0] + 1,  select_cord[1] + 1)
                        l_d =  (select_cord[0] - 1,  select_cord[1] + 1)
                        r_t =  (select_cord[0] + 1,  select_cord[1] - 1)
                        l_t =  (select_cord[0] - 1,  select_cord[1] - 1)

                        r_d_2x = (select_cord[0] + 2,  select_cord[1] + 2)
                        l_d_2x = (select_cord[0] - 2,  select_cord[1] + 2)
                        r_t_2x = (select_cord[0] + 2,  select_cord[1] - 2)
                        l_t_2x = (select_cord[0] - 2,  select_cord[1] - 2)


                        """Check if player 1 can capture player 2's checkers"""
                        if gc.select_cord[0] == black_checkers.pos[selection][0] + 2 or  gc.select_cord[0] == black_checkers.pos[selection][0] - 2:
                            for white_checker in white_checkers.pos:
                                """Search white checkers list for the piece to be captured"""
                                if ((white_checker == r_d and gc.select_cord == r_d_2x) or (white_checker == l_d and gc.select_cord == l_d_2x) or (white_checker == r_t and gc.select_cord == r_t_2x) or (white_checker == l_t and gc.select_cord == l_t_2x)):
                                    white_checker_index = white_checkers.pos.index(white_checker)
                                    black_checkers.capt_pos.append(white_checkers.pos.pop(white_checker_index)) # Add white piece position to list of captured black pieces
                                    black_checkers.capt_types.append(white_checkers.types.pop(white_checker_index))  # Add white piece type to list of captured black pieces
                                                        
                        black_checkers.pos[selection] = clicked_cord
                        """Check if black piece is able to become a king"""
                        if black_checkers.pos[selection][1] == 7.0:
                            black_checkers.types[selection] = "king"
                        gc.set_current_player("p2")
                        gc.lch["p1"]["moved"] = True
                        gc.lch["p1"]["selected"] = False

                """Check if it's player 2's turn"""
                if current_player == "p2":
                    if clicked_cord in p2_cords:
                        gc.lch["p2"]["selected"] = True
                        gc.lch["p1"]["moved"] = False

                if life_cycle_hook["p2"]["selected"]:
                    if gc.select_cord in valid_options:
                        """Initialize possible capture positions"""
                        r_d = (select_cord[0] + 1,  select_cord[1] + 1)
                        l_d = (select_cord[0] - 1,  select_cord[1] + 1)
                        r_t = (select_cord[0] + 1,  select_cord[1] - 1)
                        l_t = (select_cord[0] - 1,  select_cord[1] - 1)

                        r_d_2x = (select_cord[0] + 2,  select_cord[1] + 2)
                        l_d_2x = (select_cord[0] - 2,  select_cord[1] + 2)
                        r_t_2x = (select_cord[0] + 2,  select_cord[1] - 2)
                        l_t_2x = (select_cord[0] - 2,  select_cord[1] - 2)

                        """Check if p2(white) can capture p1(black)'s pieces checkers"""
                        if gc.select_cord[0] == white_checkers.pos[selection][0] + 2 or  gc.select_cord[0] == white_checkers.pos[selection][0] - 2:
                            for black_checker in black_checkers.pos:
                                """Search black checkers list for the piece to be captured"""
                                if ((black_checker == r_d and gc.select_cord == r_d_2x) or (black_checker == l_d and gc.select_cord == l_d_2x) or (black_checker == r_t and gc.select_cord == r_t_2x) or (black_checker == l_t and gc.select_cord == l_t_2x)):
                                    black_checker_index = black_checkers.pos.index(black_checker)
                                    white_checkers.capt_pos.append(black_checkers.pos.pop(black_checker_index)) # Add black piece position to list of captured black pieces
                                    white_checkers.capt_types.append(black_checkers.types.pop(black_checker_index))  # Add black piece type to list of captured black pieces

                                    
                        white_checkers.pos[selection] = clicked_cord
                        """Check if white piece can become a king"""
                        if white_checkers.pos[selection][1] == 0:
                            white_checkers.types[selection] = "king"
                        gc.set_current_player("p1")
                        gc.lch["p2"]["moved"] = True
                        gc.lch["p2"]["selected"] = False
                
            gc.eval_winner()
            if event.type == pygame.QUIT:

                running = False
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    """Update JSON with game data"""
    g_i.update_record(black_checkers, white_checkers)


g_i = GameInterface(start)

def main():
    g_i.configure_game()



