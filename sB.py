class CryptoStaking:
    def __init__(self, amount, duration_years, apy):
        self.amount = amount
        self.duration_years = duration_years
        self.apy = apy / 100  # Convert APY percentage to decimal

    def calculate_rewards(self):
        """
        Calculate rewards earned from crypto staking.
        """
        principal = self.amount
        duration_in_years = self.duration_years
        apy = self.apy

        # Calculate future value using compound interest formula
        future_value = principal * (1 + apy) ** duration_in_years

        # Calculate rewards (future value minus principal)
        rewards = future_value - principal

        return rewards

# Example usage:
if __name__ == "__main__":
    # Initialize CryptoStaking object with parameters
    staking = CryptoStaking(amount=1000, duration_years=1, apy=5)

    # Calculate rewards
    rewards = staking.calculate_rewards()

    # Print rewards earned
    print("Rewards earned from staking:", round(rewards, 2), "crypto")
