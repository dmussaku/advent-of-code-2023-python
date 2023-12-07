from dataclasses import dataclass

@dataclass
class Game:
    game_id: int
    green: int
    red: int
    blue: int
    
    @classmethod
    def new(cls, input_str: str):
        # print(f"Parsing {input_str}")
        game_name, rest = input_str.split(': ')
        game_id = int(game_name.split(' ')[1])
        red = green = blue = 0
        
        for game_match in rest.split('; '):
            for value_color in game_match.split(','):
                val, color = value_color.strip().split(' ')
                val = int(val)
                match color:
                    case 'red':
                        red = max(red, val)
                    case 'green':
                        green = max(green, val)
                    case 'blue':
                        blue = max(blue, val)
                    case _:
                        raise ValueError(f'Unknown color {color}')
        return cls(game_id, green, red, blue)


def run_part_1(input_lines: list[str]):
    games = [Game.new(line) for line in input_lines]
    result = sum(
        game.game_id for game in filter(lambda game: game.red <= 12 and game.green <= 13 and game.blue <= 14, games)
    )
    return result


def run_part_2(input_lines: list[str]):
    games = [Game.new(line) for line in input_lines]
    return sum(
        game.red * game.blue * game.green for game in games
    )