import random

def main():
    print("🌊 Welcome to the Underwater Treasure Hunt! 🌊")
    print("=" * 50)
    print("You are a deep-sea diver searching for underwater treasures.")
    print("Your goal: Reach 20 points to win!")
    print("• Oysters are worth 1 point each")
    print("• Pearls are worth 5 points each")
    print("But beware of sharks! Use the 'look' command to check for shark activity before exploring.")
    print("Following the look command's recommendation will guarantee no shark encounters!")
    print("Octopi are smart creatures with different moods - they might help or hinder you!")
    print("=" * 50)
    print()

    # Game variables
    oysters = 0
    pearls = 0
    score = 0
    game_over = False
    # Track look command recommendation
    last_recommendation = None
    safe_action = None

    # Main game loop
    while not game_over:
        print(f"\n🐚 Oysters: {oysters} | 💎 Pearls: {pearls} | 🎯 Score: {score}")
        print("\nWhat would you like to do?")
        print("1. 'dive' - Dive deeper to search for treasures")
        print("2. 'swim' - Swim around to search for treasures")
        print("3. 'look' - Look around to check for sharks")
        print("4. 'surface' - Come up for air and check your collection")
        print("5. 'quit' - End the game")

        choice = input("\nEnter your choice: ").lower().strip()

        if choice == "dive":
            print("\n🤿 You dive deeper into the ocean...")

            # Check if this action follows the safe recommendation
            is_safe_action = (safe_action == "dive")

            # Random chance of finding treasure, encountering danger, or finding nothing
            # If following recommendation, eliminate shark encounter possibility
            if is_safe_action:
                outcome = random.randint(1, 8)  # No shark encounters (9-10 range eliminated)
                if outcome > 6:  # Adjust nothing range to 7-8
                    outcome = 9  # Map to nothing
            else:
                outcome = random.randint(1, 10)

            if outcome <= 6:  # 60% chance to find treasure
                # Random chance of finding oyster (70%) or pearl (30%)
                treasure_type = random.randint(1, 10)
                if treasure_type <= 7:  # 70% chance for oyster
                    oysters += 1
                    score += 1
                    print(f"🐚 Success! You found an oyster! (Total: {oysters}) +1 point")
                else:  # 30% chance for pearl
                    pearls += 1
                    score += 5
                    print(f"💎 Amazing! You found a beautiful pearl! (Total: {pearls}) +5 points")

                # Check if player won
                if score >= 20:
                    print(f"\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
                    print(f"You reached {score} points and won the game!")
                    print(f"Final collection: {oysters} oyster(s) and {pearls} pearl(s)!")
                    print("You are a master deep-sea treasure hunter!")
                    game_over = True
                    continue

            elif outcome <= 8:  # 20% chance for shark encounter
                if is_safe_action:
                    print("🌊 You search around but find nothing this time.")
                    print("✅ Following the recommendation kept you safe from sharks!")
                else:
                    print("🦈 Oh no! A small shark spotted you!")
                    print("You quickly swim away, but your diving session is over.")
                    game_over = True
            else:  # 20% chance to find nothing
                print("🌊 You search around but find nothing this time.")

            # Reset safe action after use
            if is_safe_action:
                safe_action = None
                last_recommendation = None

        elif choice == "swim":
            print("\n🏊 You swim gracefully through the water...")

            # Check if this action follows the safe recommendation
            is_safe_action = (safe_action == "swim")

            # Random chance of finding treasure, encountering danger, or finding nothing
            # Swimming doesn't have shark encounters, so no modification needed
            outcome = random.randint(1, 10)

            if outcome <= 4:  # 40% chance to find treasure
                # Random chance of finding pearl (70%) or oyster (30%)
                treasure_type = random.randint(1, 10)
                if treasure_type <= 7:  # 70% chance for pearl
                    pearls += 1
                    score += 5
                    print(f"💎 Amazing! You found a beautiful pearl! (Total: {pearls}) +5 points")
                else:  # 30% chance for oyster
                    oysters += 1
                    score += 1
                    print(f"🐚 Success! You found an oyster! (Total: {oysters}) +1 point")

                # Check if player won
                if score >= 20:
                    print(f"\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
                    print(f"You reached {score} points and won the game!")
                    print(f"Final collection: {oysters} oyster(s) and {pearls} pearl(s)!")
                    print("You are a master deep-sea treasure hunter!")
                    game_over = True
                    continue

            elif outcome <= 6:  # 20% chance for octopus encounter
                print("🐙 A curious octopus approaches!")

                # Octopus has different moods - 50/50 chance
                octopus_mood = random.randint(1, 2)

                if octopus_mood == 1:  # Mischievous mood - tries to steal oyster
                    if oysters > 0:
                        oysters -= 1
                        score -= 1
                        print("The octopus is feeling mischievous and snatches one of your oysters!")
                        print(f"🐚 You now have {oysters} oyster(s) left. -1 point")
                    else:
                        print("The octopus looks around for oysters but you don't have any.")
                        print("It swims away disappointed.")
                else:  # Generous mood - gives pearl
                    pearls += 1
                    score += 5
                    print("The octopus is in a generous mood and presents you with a beautiful pearl!")
                    print(f"💎 You now have {pearls} pearl(s)! +5 points")

                    # Check if player won
                    if score >= 20:
                        print(f"\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
                        print(f"You reached {score} points and won the game!")
                        print(f"Final collection: {oysters} oyster(s) and {pearls} pearl(s)!")
                        print("You are a master deep-sea treasure hunter!")
                        game_over = True
                        continue

            else:  # 40% chance to find nothing
                print("🌊 You swim around but don't find any treasures this time.")

            # Reset safe action after use (swimming doesn't have shark encounters but we still track it)
            if is_safe_action:
                safe_action = None
                last_recommendation = None

        elif choice == "look":
            print("\n👁️ You carefully scan the surrounding waters...")

            # Generate random shark activity levels for diving and swimming areas
            dive_shark_activity = random.randint(1, 10)
            swim_shark_activity = random.randint(1, 10)

            # Determine danger levels (higher numbers = more dangerous)
            dive_danger = "High" if dive_shark_activity >= 7 else "Moderate" if dive_shark_activity >= 4 else "Low"
            swim_danger = "High" if swim_shark_activity >= 7 else "Moderate" if swim_shark_activity >= 4 else "Low"

            print(f"🦈 Shark Activity Report:")
            print(f"  Deep waters (diving): {dive_danger} risk")
            print(f"  Surface waters (swimming): {swim_danger} risk")

            # Give strategic advice and track recommendation
            if dive_shark_activity < swim_shark_activity:
                last_recommendation = "dive"
                safe_action = "dive"
                print("\n💡 Recommendation: Diving appears safer right now!")
                print("🛡️  Following this recommendation will guarantee no shark encounters!")
            elif swim_shark_activity < dive_shark_activity:
                last_recommendation = "swim"
                safe_action = "swim"
                print("\n💡 Recommendation: Swimming appears safer right now!")
                print("🛡️  Following this recommendation will guarantee no shark encounters!")
            else:
                last_recommendation = "either"
                safe_action = None
                print("\n💡 Both areas seem equally risky. Choose carefully!")

            # Add some flavor text
            if dive_danger == "High" and swim_danger == "High":
                print("⚠️  The waters are particularly dangerous today...")
            elif dive_danger == "Low" and swim_danger == "Low":
                print("🌊 The waters seem calm and peaceful.")

        elif choice == "surface":
            print("\n🌅 You swim to the surface and check your collection...")

            if score >= 20:
                print("\n🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print(f"You successfully collected {oysters} oyster(s) and {pearls} pearl(s)!")
                print(f"Final Score: {score} points")
                print("You are a master deep-sea treasure hunter!")
                game_over = True
            else:
                points_needed = 20 - score
                print(f"Current Score: {score} points")
                print(f"You need {points_needed} more points to win!")
                print("Keep exploring the ocean depths!")

        elif choice == "quit":
            print("\n👋 Thanks for playing!")
            print(f"Final collection: {oysters} oyster(s), {pearls} pearl(s)")
            print(f"Final score: {score} points")
            game_over = True

        else:
            print("\n❌ Invalid choice. Please try again.")

    # Final message
    if score >= 20:
        print("\n🏆 You completed your underwater adventure successfully!")
    else:
        print("\n🌊 Better luck next time, brave diver!")

if __name__ == "__main__":
    main()
