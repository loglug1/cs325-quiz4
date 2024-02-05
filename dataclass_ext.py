from dataclasses import dataclass

@dataclass
class Game:
    title : str
    year : int
    genre : str

    def play(self) -> None:
        print(f'Wow! {self.title} is a really cool game!')

def main():
    games = [
        Game('Animal Crossing: Population Growing', 2001, 'Simulation'),
        Game('Minecraft', 2009, 'Sandbox'),
        Game('Super Mario Bros. Wonder', 2023, 'Platformer')
    ]

    print('Here\'s some pretty cool games:')
    for game in games:
        print(game)

    games[0].play()

if __name__=='__main__':
    main()