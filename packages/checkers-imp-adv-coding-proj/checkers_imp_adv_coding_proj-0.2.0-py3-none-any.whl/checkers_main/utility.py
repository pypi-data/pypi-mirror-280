from PIL import Image
from pygame import image, transform, Surface
from typing import Tuple, List, Dict
import json
import pkg_resources
import os
import sys


class ImageHandler:
    """Class for handling game image loading and cropping"""
    def __init__(self):
        self.checkers_img_path = pkg_resources.resource_filename('checkers_main', 'static/images/checkers.png')
        try:
             self.checkers_img = Image.open(self.checkers_img_path)
        except Exception:
             self.checkers_img = Image.open(resource_path("static/images/checkers.png"))
        self._size : Tuple[int]
        self._size_small: Tuple[int]
    
    def get_black_checker(self, size="normal") -> Surface:
        """Retuns a black checker image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((64, 0, 96, 32))), self._size)
    
    def get_white_checker(self, size="normal") -> Surface:
        """Retuns a white checker image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((96, 0, 128, 32))), self._size)
    
    def get_black_king(self, size="normal") -> Surface:
        """Retuns a black king image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((0, 0, 32, 32))), self._size)
    
    def get_white_king(self, size="normal") -> Surface:
        """Retuns a white king image as a pygame surface"""
        if size == "small":
            return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self._size_small)
        return transform.scale(self.pil_to_surface(self.checkers_img.crop((32, 0, 64, 32))), self._size)
    
    def pil_to_surface(self, pil_image):
        """Convert a PILLOW image to a Pygame surface."""
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()
        surface = image.fromstring(data, size, mode)
        return surface

class ManHandler:
     
    def _eval_men(self, cord: Tuple[int | float]) -> List[Tuple[int | float]]:
        """Checks and validates all possible moves for a given man piece"""
        possible_positions: List[Tuple[int | float]] = []
        if self._current_player == "p1":
                # Initiliaze possible positions
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if 2 <= cord[0] <= 9 and cord[1] <= 7:
                    # Check if position at 1 right and 1 down is valid
                    if (r_d not in self._player_2_cords) and (r_d not in self._player_1_cords) and (2 <= cord[0] + 1 <= 9) and (0 <= cord[1] + 1 <= 7):
                        possible_positions.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if (l_d not in self._player_2_cords) and (l_d not in self._player_1_cords) and (2 <= cord[0] - 1 <= 9) and (0 <= cord[1] + 1 <= 7):
                         possible_positions.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if (r_d_2x not in self._player_1_cords) and (r_d_2x not in self._player_2_cords) and (r_d not in self._player_1_cords) and (2 <= cord[0] + 2 <= 9) and (0 <= cord[1] + 2 <= 7) and (r_d in self._player_2_cords):
                         possible_positions.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if (l_d_2x not in self._player_1_cords) and  (l_d_2x not in self._player_2_cords) and (l_d not in self._player_1_cords) and (2 <= cord[0] - 2 <= 9) and (0 <= cord[1] + 2 <= 7) and (l_d in self._player_2_cords):
                        possible_positions.append(l_d_2x)
        
        
        if self._current_player == "p2":
                # Initiliaze possible positions
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if cord[0] <= 9 and cord[0] >= 2 and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self._player_2_cords) and (r_t not in self._player_1_cords) and (2 <= (cord[0] + 1) <= 9):
                        possible_positions.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self._player_2_cords) and (l_t not in self._player_1_cords) and (2 <= (cord[0] - 1) <= 9):
                            possible_positions.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self._player_2_cords) and  (r_t_2x not in self._player_1_cords) and (r_t not in self._player_2_cords) and (2 <= cord[0] + 2 <= 9) and (r_t in self._player_1_cords):
                            possible_positions.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self._player_2_cords) and (l_t_2x not in self._player_1_cords) and (l_t not in self._player_2_cords) and (2 <= cord[0] - 2 <= 9) and (l_t in self._player_1_cords):
                        possible_positions.append(l_t_2x)
        return possible_positions
    

class KingHandler(ManHandler):
    def __init__(self) -> None:
         super().__init__()
     
    def _eval_king(self, cord):
        """Checks and validates all possible moves for a given king piece"""
        possible_positions = self._eval_men(cord)
        
        if self._current_player == "p1":
                # Initiliaze possible positions
                r_t = (cord[0] + 1, cord[1] - 1)
                l_t = (cord[0] - 1, cord[1] - 1)
                r_t_2x = (cord[0] + 2, cord[1] - 2)
                l_t_2x = (cord[0] - 2, cord[1] - 2)
                if (cord[0] <= 9) and (cord[0] >= 2) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 up is valid
                    if (r_t not in self._player_2_cords) and (r_t not in self._player_1_cords) and (2 <= (cord[0] + 1) <= 9):
                        possible_positions.append(r_t)
                    # Check if position at 1 left and 1 up is valid
                    if (l_t not in self._player_2_cords) and (l_t not in self._player_1_cords) and (2 <= (cord[0] - 1) <= 9):
                            possible_positions.append(l_t)
                    # Check if position at 2 right and 2 up is valid
                    if (r_t_2x not in self._player_2_cords) and  (r_t_2x not in self._player_1_cords) and (r_t not in self._player_1_cords) and (2 <= cord[0] + 2 <= 9) and (r_t in self._player_2_cords):
                            possible_positions.append(r_t_2x)
                    # Check if position at 2 left and 2 up is valid
                    if (l_t_2x not in self._player_2_cords) and (l_t_2x not in self._player_1_cords) and (l_t not in self._player_1_cords) and (2 <= cord[0] - 2 <= 9) and (l_t in self._player_2_cords):
                        possible_positions.append(l_t_2x)

        if self._current_player == "p2":
                # Initiliaze possible positions
                r_d = (cord[0] + 1, cord[1] + 1)
                l_d = (cord[0] - 1, cord[1] + 1)
                r_d_2x = (cord[0] + 2, cord[1] + 2)
                l_d_2x = (cord[0] - 2, cord[1] + 2)
                if (2 <= cord[0] <= 9) and (cord[1] <= 7):
                    # Check if position at 1 right and 1 down is valid
                    if r_d not in self._player_2_cords and r_d not in self._player_1_cords and 2 <= cord[0] + 1 <= 9:
                        possible_positions.append(r_d)
                    # Check if position at 1 left and 1 down is valid
                    if l_d not in self._player_2_cords and l_d not in self._player_1_cords and 2 <= cord[0] - 1 <= 9:
                         possible_positions.append(l_d)
                    # Check if position at 2 right and 2 down is valid
                    if r_d_2x not in self._player_1_cords and r_d_2x not in self._player_2_cords and r_d not in self._player_2_cords and 2 <= cord[0] + 2 <= 9 and r_d in self._player_1_cords:
                         possible_positions.append(r_d_2x)
                    # Check if position at 2 left and 2 down is valid
                    if l_d_2x not in self._player_1_cords and  l_d_2x not in self._player_2_cords and l_d not in self._player_2_cords and 2 <= cord[0] - 2 <= 9 and l_d in self._player_1_cords:
                        possible_positions.append(l_d_2x)
        return possible_positions

class RecordHandler:
    """Class which handles json game data"""
    def __init__(self) -> None:
        """Initiliazes GameRecord variables"""
        self._file_path: str = "game_record.json"
    

    def update_record(self,b_c, w_c) -> None:
        """Will update the game record json file with the most recent game data"""
        data: Dict[Dict[List[Tuple[int | float] | str]]]
        data = {
            "pos": {
                "black_pos": b_c.pos,
                "white_pos": w_c.pos
            },
            "types": {
                "black_types": b_c.types,
                "white_types": w_c.types
            },
            "capt_pos": {
                "b_capt_pos": b_c.capt_pos,
                "w_capt_pos": w_c.capt_pos
            },
            "capt_types": {
                "b_capt_types": b_c.capt_types,
                "w_capt_types": w_c.capt_types
            }
            
        }
        with open(self._file_path, "w") as f:
            json.dump(data, f,  indent=1)

    def _read_record(self) -> Dict | None:
        """Returns previous game data or none"""
        try:
            with open(self._file_path, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return None
        
    def _check_record(self) -> True | False:
        """Returns true if previous game data exists"""
        if self._read_record():
            return True
        return False
    
        
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for development and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

