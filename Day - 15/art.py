# ascii_art.py
# Enhanced ASCII art for the Coffee Machine project

coffee_machine_logo = r"""
        ╔════════════════════════════════╗
        ║        ☕  COFFEE MACHINE  ☕ ║
        ╠════════════════════════════════╣
        ║  [1] Espresso     ₹120         ║
        ║  [2] Latte        ₹200         ║
        ║  [3] Cappuccino   ₹250         ║
        ║  [4] Mocha        ₹280         ║
        ║  [5] Cold Brew    ₹220         ║
        ╠════════════════════════════════╣
        ║     ⏺ START   |   ⏹ OFF       ║
        ║     ☰ MENU    |   ⟳ REFILL    ║
        ╚════════════════════════════════╝
                Welcome to BrewBox ☕
"""

# Loading animation frames
loading_ascii = [
    "[=         ] Brewing your drink...",
    "[==        ] Grinding beans...",
    "[====      ] Heating milk...",
    "[======    ] Mixing flavors...",
    "[========  ] Almost ready...",
    "[==========] Done! ☕"
]

# ASCII Art for Drinks
latte_art = r"""
     (( (
      ) ))
   .-""---.
  /       o\
 | o       |
 \       o/
  `-----"`
   ☕ Latte Ready!
"""

espresso_art = r"""
   {   Espresso ☕   }
     \   |   /
      \  |  /
       \ | /
        \|/
"""

cappuccino_art = r"""
    ( (
     ) )
   ........
   |      |]
   \      /
    `----'
  ☕ Cappuccino Ready!
"""

mocha_art = r"""
   ( (
    ) )
  #########
  #       #
  # Mocha #
  #########
   ☕ Enjoy!
"""

coldbrew_art = r"""
   _____
  |     |\
  |     | |
  |_____|/
   || ||
   || ||
   🧊 Cold Brew Ready!
"""

# Map drink name → art
drink_ascii_map = {
    "latte": latte_art,
    "espresso": espresso_art,
    "cappuccino": cappuccino_art,
    "mocha": mocha_art,
    "cold brew": coldbrew_art
}

# ASCII for Start and Off Screen
start_screen = r"""
╔═══════════════════════════════════╗
║       ☕  STARTING MACHINE  ☕   ║
╚═══════════════════════════════════╝
"""

off_screen = r"""
╔═══════════════════════════════════╗
║     ☕  SHUTTING DOWN MACHINE ☕ ║
╚═══════════════════════════════════╝
"""
