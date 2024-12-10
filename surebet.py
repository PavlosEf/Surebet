def calculate_arbitrage(bankroll, odds):
    """
    Calculate surebet stakes, profit, and arbitrage percentage.

    Args:
        bankroll (float): Total money to bet.
        odds (list of float): List of odds for each outcome.

    Returns:
        dict: A dictionary containing stakes, potential profit, and arbitrage percentage.
    """
    # Calculate total probability
    total_probability = sum(1 / odd for odd in odds)

    if total_probability >= 1:
        return {"error": "This is not a surebet."}

    # Calculate stakes for each outcome
    stakes = [(bankroll / (odd * total_probability)) for odd in odds]

    # Calculate guaranteed profit
    profits = [stake * odd - bankroll for stake, odd in zip(stakes, odds)]
    guaranteed_profit = min(profits)

    # Calculate arbitrage percentage
    arbitrage_percentage = (1 - total_probability) * 100

    return {
        "stakes": [round(stake, 2) for stake in stakes],
        "profit": round(guaranteed_profit, 2),
        "arbitrage_percentage": round(arbitrage_percentage, 2),
    }


def get_user_input():
    """
    Gather user inputs for bankroll, number of outcomes, and odds.

    Returns:
        tuple: Bankroll (float), odds (list of float).
    """
    # Get bankroll
    bankroll = float(input("Enter the total bankroll: "))

    # Select number of outcomes
    print("Select the number of outcomes (2 to 10):")
    num_outcomes = int(input("Enter your choice: "))
    if num_outcomes < 2 or num_outcomes > 10:
        raise ValueError("Number of outcomes must be between 2 and 10.")

    # Get odds for each outcome
    odds = []
    for i in range(num_outcomes):
        odd = float(input(f"Enter odds for outcome {i + 1}: "))
        if odd <= 0:
            raise ValueError("Odds must be greater than 0.")
        odds.append(odd)

    return bankroll, odds


def main():
    """
    Main function to run the surebet calculator.
    """
    try:
        # Get user input
        bankroll, odds = get_user_input()

        # Calculate surebet
        result = calculate_arbitrage(bankroll, odds)

        if "error" in result:
            print(result["error"])
        else:
            print("\nResults:")
            for i, stake in enumerate(result["stakes"], start=1):
                print(f"Stake on Outcome {i}: ${stake}")
            print(f"Guaranteed Profit: ${result['profit']}")
            print(f"Arbitrage Percentage: {result['arbitrage_percentage']}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
