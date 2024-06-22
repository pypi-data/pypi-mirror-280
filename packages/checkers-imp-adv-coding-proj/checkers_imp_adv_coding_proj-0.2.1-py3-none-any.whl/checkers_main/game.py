from pygame import draw, font, Surface
from typing import List, Tuple, Dict
from checkers_main.utility import ImageHandler, KingHandler, RecordHandler
import time
import pkg_resources


font.init()




class GameBoard(ImageHandler):
    """Class to handle game board functionality"""
    def __init__(self, b_c, w_c, w, h, diff=1) -> None:
        super().__init__()
        self._width: int = w * diff
        self._height: int = h * diff
        self._colors: Dict[str]= {"bg": "#ffe4ba",
                         "square": "#e3ae5c",
                         "border": "black"}
        self._squares: int = 64
        self._bc: GameCheckerStatus = b_c
        self._wc: GameCheckerStatus = w_c
        self.font_init()
        # Overwrite Parent attributes
        self._size = self.get_square_space()
        self._size_small =  (self._size[0] // 2, self._size[1] // 2)
        

    def post_init(self, game_controls):
        self.__gc = game_controls
    
    def font_init(self):
        self.gs_font = font.SysFont('timesnewroman', int(self.get_square_size() * 0.9))
        self.w_font = font.SysFont('timesnewroman', int(self.get_square_size() * 0.9))

    def get_squares(self):
        return self._squares   

    def get_board_size(self) -> Tuple[int]:
        """Getter which returns size of game board"""
        return (self._width, self._height)
        
    def get_bg_color(self) -> str:
        """Getter which returns background color from colors dictionary"""
        return self._colors["bg"]
    
    def get_square_color(self):
        """Getter which returns the square color from colors dictionary"""
        return self._colors["square"]

    def get_border_color(self):
        """Getter which returns the border color from colors dictionary"""
        return self._colors["border"]

    def get_square_space(self) -> Tuple[int]:
        """Getter which returns the width and height of the board squares in a tuple"""
        return (self.get_square_size(), self.get_square_size())
    
    def get_square_size(self):
        """Getter which returns the width of the board squares"""
        return (self._width // 10)

    
    def render_game_env(self, surface): 
        """Renders 32 squares squares, 9 vertical and 9 horizontal lines onto the screen
        (excecutes render_pieces(), render_game_status() and render_captures() functions)
        
        The render_game_env() method utilises the modular congruence of n in range modulo 4 to
        evenly draw columns accross rows on the grid
        """
        surface.fill(self.get_bg_color())
        n: int = 0
        mod: int = 4
        while n < self._squares // 2:
            y: int = n // mod
            x: int = n % mod # n ≅ x(mod 4)
            diff: int = x * (self.get_square_size() * 2) # diff = (0 -> 200 -> 400 -> 600)
            if y % 2 != 0:
                """Draw gray square when y =(1 -> 3 -> 5 -> 7)"""
                pos_size: List[Tuple] = [((self._width * 0.9 - diff), (y * self.get_square_size())), self.get_square_space()]
                draw.rect(surface, self.get_square_color(), pos_size)
            else:
                """Draw gray square when y = (0 -> 2 -> 4 -> 6)"""
                pos_size: List[Tuple] = [((self._width * 0.8 - diff), (y * self.get_square_size())), self.get_square_space()]
                draw.rect(surface, self.get_square_color(), pos_size)
            n += 1
    
        self.render_borders(surface)

        self.render_pieces(surface)

        self.render_game_status(surface)

        self.render_captured(surface)

    def render_borders(self, surface) -> None:
        n = 0
        while n < 9:
            """Initialize render positions"""
            hor_start: Tuple[int] = (self._width * 0.2, n * self.get_square_size())
            hor_end: Tuple[int] = (self._width, n * self.get_square_size())
            vert_start: Tuple[int] = ((self._width * 0.2) + n * self.get_square_size(), 0)
            vert_end: Tuple[int] = ((self._width * 0.2) + n * self.get_square_size(), self._height * 0.8)
            """Draw horizontal border lines"""
            draw.line(surface, self.get_border_color(), hor_start, hor_end)
            """Draw vertical border lines"""
            draw.line(surface, self.get_border_color(), vert_start, vert_end)
            n += 1
        """Draw border for game status view """
        gs_pos_size: List[Tuple[int]] = [(self._height * 0.2, self._height * 0.8),(self._width * 0.8, self._height * 0.2 )]
        capt_pos_size: List[Tuple[int]] = [(0, 0),(self._width * 0.2, self._height * 0.8)]
        draw.rect(surface, self.get_border_color(), gs_pos_size, 3)
        """Draw border for captured men view"""
        draw.rect(surface, self.get_border_color(), capt_pos_size, 3)



    def render_pieces(self, surface) -> None:
        """Renders each piece in CheckStatus.pos object lists, onto the board when called"""
        for i in range(len(self._bc.get_pos())):
            # Check if black piece is a man
            if self._bc.types[i] == "man":
                coord_pos: Tuple[int] = (self._bc.get_pos()[i][0] * self.get_square_size(), self._bc.get_pos()[i][1] * self.get_square_size())
                surface.blit(self.get_black_checker(), coord_pos)
            # Check if black piece is a king
            elif self._bc.types[i] == "king":
                coord_pos: Tuple[int] = (self._bc.get_pos()[i][0] * self.get_square_size(), self._bc.get_pos()[i][1] * self.get_square_size())
                surface.blit(self.get_black_king(), coord_pos)

        for i in range(len(self._wc.get_pos())):
            # Check if white piece is a man 
            if self._wc.types[i] == "man":
                coord_pos: Tuple = (self._wc.get_pos()[i][0] * self.get_square_size(), self._wc.get_pos()[i][1] * self.get_square_size())
                surface.blit(self.get_white_checker(), coord_pos)
        # Check if white piece is a king
            elif self._wc.types[i] == "king":
                coord_pos: Tuple = (self._wc.get_pos()[i][0] * self.get_square_size(), self._wc.get_pos()[i][1] * self.get_square_size())
                surface.blit(self.get_white_king(), coord_pos)


    def render_game_status(self, surface) -> None:
        """Render the game message prompts to players"""
        dest: Tuple[float] = (self._width * 0.23, self._height * 0.85)
        if self.__gc.lch["p2"]["moved"]: # Checks if it is black's turn to select a piece
            surface.blit(self.gs_font.render("Black select a Piece", True, "black"), dest)
        if self.__gc.lch["p1"]["selected"]:# Checks if it is black's turn to move a piece
            surface.blit(self.gs_font.render("Black move a Piece", True, "black"), dest)
        if self.__gc.lch["p1"]["moved"]: # Checks if it is white's turn to select a piece
            surface.blit(self.gs_font.render("White select a Piece", True, "black"), dest)
        if self.__gc.lch["p2"]["selected"]: # Checks if it is white's turn to move a piece
            surface.blit(self.gs_font.render("White move a Piece", True, "black"), dest)

    def render_captured(self, surface) -> None:
        """Renders all captured pieces at the right side of the screen"""
        for i in range(len(self._bc.capt_types)):
            # Check if white piece is a man or king
            x = self._width * 0.01
            y = (self._height * 0.7 - (i * self.get_square_size() // 2))
            if self._bc.capt_types[i] == "man":
                coord_pos: Tuple[int] = (x, y)
                surface.blit(self.get_white_checker("small"), coord_pos)
            elif self._bc.capt_types[i] == "king":
                coord_pos: Tuple[int] = (x, y)
                surface.blit(self.get_white_king("small"), coord_pos)
        
        for i in range(len(self._wc.capt_types)):
            # Check if black piece is a man or king
            x = self._width * 0.1
            y = (self._height * 0.7 - (i * self.get_square_size() // 2))
            if self._wc.capt_types[i] == "man":
                coord_pos: Tuple[int] = (x, y)
                surface.blit(self.get_black_checker("small"), coord_pos)
            elif self._wc.capt_types[i] == "king":
                coord_pos: Tuple[int] = (x, y)
                surface.blit(self.get_black_king("small"), coord_pos)
        
    def render_winner(self, surface) -> None:
        """Renders winning text when life cycle hook detects a winner"""
        dest = (self._width * 0.05, self._height * 0.3)
        if self.__gc.lch["winner"] == "black(p1)":
            surface.blit(self.w_font.render("Black(P1) is the Winner", True, "black"), dest)
        elif self.__gc.lch["winner"] == "white(p2)":
            surface.blit(self.w_font.render("White(P2) is the Winner", True, "black"), dest)


    
class GameInterface(RecordHandler):
    def __init__(self, start) -> None:
        super().__init__()
        self.__start = start

    def configure_game(self):
        # Checks if user has a previously saved game
        if self._check_record():
            new_or_load = input("\nWould you like to load(L) your previous game or start a new game(N)\n").title()
            if new_or_load == "L":
                data: Dict[Dict[List[Tuple[int | float] | str]]]
                data = self._read_record()
                print("\nLoading previous round...")
                self.__start(data["pos"]["black_pos"], 
                    data["pos"]["white_pos"], 
                    data["types"]["black_types"], 
                    data["types"]["white_types"],
                    data["capt_pos"]["b_capt_pos"],
                    data["capt_pos"]["w_capt_pos"],
                    data["capt_types"]["b_capt_types"],
                    data["capt_types"]["w_capt_types"],
                    )
                
            elif new_or_load == "N":
                print("\nStarting new round...")
                self.__start()
            else:
                print(f"'{new_or_load}' is an invalid input, enter either L or N\n")
                time.sleep(1)
        else:
            print("You have no previous games, Starting round...")
            self.__start()

class GameCheckerStatus:
    """Class to handle and record changes in the white and black checker objects"""
    def __init__(self, pos, types, capt_pos, capt_types) -> None:
        """Initilizes checker position, type and captures"""
        self.pos: List[Tuple] = self.convert_to_int(pos)
        self.types: List[str] = types
        
        self.capt_pos: List[Tuple] = capt_pos
        self.capt_types: List[str] = capt_types

    def convert_to_int(self, l_t) -> List[Tuple[int]]:
        """Will convert possible float coordinates into integers upon initialization"""
        return [(int(x),int(y)) for x , y in l_t]


    def get_pos(self):
        """Getter which returns checker positions"""
        return self.pos

class GameControls(KingHandler):
    """Class to control game logic, turn handling and behaviour"""
    def __init__(self,  sqaure_space, black_checkers, white_checkers) -> None:
        super().__init__()
        """Initiliazes default game control settings"""
        self.__square_space: Tuple[float] = sqaure_space
        self.__colors: Dict[str] = {"p1": "#d70000", "p2": "#0229bf", "indicator":"#2db83d"}
        self._current_player: str = "p1"
        self.__players: Dict[GameCheckerStatus] = {"p1": black_checkers, "p2": white_checkers}
        self._player_1_cords: List[Tuple[int]] = self.__players["p1"].get_pos()
        self._player_2_cords: List[Tuple[int]] = self.__players["p2"].get_pos()
        self.__player_1_types: List[str] = self.__players["p1"].types
        self.__player_2_types: List[str] = self.__players["p2"].types
        self.lch: Dict[Dict[bool] | bool | str] = {"p1": {"selected": False,"moved": False}, "p2": {"selected": False, "moved": True}, "winner": False}
        self.select_cord: Tuple[float] = None
        self.current_player_cords: List[Tuple[int]] = self.__players[self._current_player].get_pos()
        self.font: font.Font = font.SysFont('timesnewroman', int(self.__square_space[0] * 0.9))


    def render_selection(self, surface: Surface):
        if self.select_cord:
                """Check if player has selected a black(p1) piece when black is the current player"""
                if self._current_player == "p1":
                    if self.select_cord in self._player_1_cords:
                        self.__render_authorized_positions(surface)
                        pos: Tuple[float, float] = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                        draw.rect(surface, self.__colors[self._current_player], [pos, self.__square_space], 3)
                
                """Check if player has selected a white(p2) piece when white is the current player"""
                if self._current_player == "p2":
                    if self.select_cord in self._player_2_cords:
                        self.__render_authorized_positions(surface)
                        pos: Tuple[float, float] = (self.select_cord[0] * self.__square_space[0], self.select_cord[1] * self.__square_space[0])
                        draw.rect(surface, self.__colors[self._current_player], [pos, self.__square_space], 3)

    def set_current_player(self, player: str):
         """Setter for current player"""
         self._current_player = player

    def get_current_player(self) -> str:
        """Getter for current player"""
        return self._current_player


    def __evaluate_positions(self) -> List[List[Tuple[int | float]]]:
        """Checks for all the possible moves for each piece of the current player"""
        all_possible_positions: List[List[Tuple]] = []
        possible_positions: List[Tuple] = []
        if self._current_player == "p1":
            for i in range(len(self._player_1_cords)):
                # Check if black player(p1) piece is a man
                if self.__player_1_types[i] == "man":
                    possible_positions = self._eval_men(self._player_1_cords[i])
                    all_possible_positions.append(possible_positions)
                # check if black player(p1) piece is a king
                elif self.__player_1_types[i] == "king":
                    possible_positions = self._eval_king(self._player_1_cords[i])
                    all_possible_positions.append(possible_positions)


        elif self._current_player == "p2":
            for i  in range(len(self._player_2_cords)):
                # Check if white player(p2) piece is a man
                if self.__player_2_types[i] == "man":
                    possible_positions = self._eval_men(self._player_2_cords[i])
                    all_possible_positions.append(possible_positions)
                # Check if white player(p2) piece is a king
                elif self.__player_2_types[i] == "king":
                    possible_positions = self._eval_king(self._player_2_cords[i])
                    all_possible_positions.append(possible_positions)
                     
            
        return all_possible_positions
    

    def return_selection(self) -> int | None:
        """Return the click selection index if it is current_player_cords list"""
        # Checks if current player is player 1
        if self._current_player == "p1":
            if self.select_cord in self._player_1_cords:
                return self._player_1_cords.index(self.select_cord)
        # Checks if current player is player 2
        elif self._current_player == "p2":
            if self.select_cord in self._player_2_cords:
                return self._player_2_cords.index(self.select_cord)
        return None

    def return_authorized_positions(self) -> List:
         """Returns the player coordinates at the index of the click selection"""
         if self.return_selection() is not None:
              return self.__evaluate_positions()[self.return_selection()]
         return []
    
    def __render_authorized_positions(self, surface: Surface) -> None:
         """Renders a green circle indicator at each position in the valid options list"""
         for cord in self.return_authorized_positions():
              x = (cord[0] * self.__square_space[0]) + self.__square_space[0] / 2
              y = (cord[1] * self.__square_space[0]) + self.__square_space[0] / 2
              draw.circle(surface, self.__colors["indicator"], (x, y), 5)
    
    def eval_winner(self) -> None:
        """Checks for a winning player on every game loop"""
        if not self._player_2_cords:
            self.lch["winner"] = "black(p1)"
        elif not self._player_1_cords:
            self.lch["winner"] = "white(p2)"
    
         

    def get_player_2_cords(self) -> List[Tuple[int | float]]:
        return self._player_2_cords

    def get_player_1_cords(self) -> List[Tuple[int | float]]:
        return self._player_1_cords

    def get_life_cycle_hook(self) -> Dict:
         return self.lch

        



        