
# Dungeon Adventure Game

Welcome to the Dungeon Adventure! This is a simple text-based adventure game where your quest is to find the legendary treasure in the mystical dungeon. Your choices will determine whether you succeed in your quest or meet an untimely end.

## How to Play

1. **Run the Game:**
   To start the game, simply run the script in your Python environment.

```bash
python dungeon_adventure.py
```

2. **Make Your Choices:**
   The game will present you with a series of choices. Type your choice and press Enter to continue. Be careful with your decisions, as they will determine your fate!

## Game Walkthrough

1. **Starting the Game:**
   - You begin at the entrance of the dungeon with two paths: a dark corridor on the left and a mysterious staircase on the right.
   - Type `left` or `right` to choose your path.

2. **Dark Corridor Path:**
   - If you choose the left path, you will venture into the dark corridor.
   - You will encounter a fork in the path with growls and a faint glow to the left and a draft to the right.
   - Type `left` or `right` to choose your direction.

   - If you choose the left at the fork:
     - You encounter a pack of hungry wolves guarding a chest. Unfortunately, this leads to a Game Over.
   - If you choose the right at the fork:
     - You find a secret room with a healing potion and a map to the treasure room.

3. **Room with Three Doors:**
   - You will then reach a room with three doors: one marked with a dragon symbol, one with a wizard symbol, and one with a rogue symbol.
   - Type `dragon`, `wizard`, or `rogue` to choose a door.

   - **Dragon Door:**
     - You enter a room with a sleeping dragon guarding the treasure. You must decide to `sneak` past it or `attack` it.
     - If you sneak, you successfully grab the treasure and win!
     - If you attack, the dragon wakes up and breathes fire, resulting in a Game Over.

   - **Wizard Door:**
     - You encounter a wise old wizard who challenges you to a riddle: "What has keys but can't open locks?"
     - Type your answer and press Enter.
     - If you answer `piano`, the wizard is impressed and opens a secret passage to the treasure room. You win!
     - Any other answer leads to a Game Over.

   - **Rogue Door:**
     - You enter a room filled with traps. You must decide to `jump` over the traps or `crawl` under them.
     - If you jump, you skillfully navigate the traps and reach the treasure room, resulting in a win!
     - If you crawl, you trigger a trap and fall into a pit, leading to a Game Over.

4. **Mysterious Staircase Path:**
   - If you choose the right path, you climb the mysterious staircase and find a magical portal.
   - Stepping through the portal leads you directly to the treasure room. Congratulations, you win!


- This game was created as a fun and simple text-based adventure project.
- Inspired by classic text-based adventure games and the desire to create an interactive story.

Enjoy your adventure!

![CaptureTreasure](https://github.com/user-attachments/assets/7aaa7447-75c8-4396-8f4a-2fc813bf2cf3)
