package exercise1;

public class Account {

	// ...

	private int daysOverdrawn;
	private boolean isPremium;
	private final double BASE_OVERDRAFT_FEE = 4.5
	private final double PREMIUM_BASE_OVERDRAFT_FEE = 10.0;
	private final double OVERDRAFT_RATE = 1.75;
	private final double PREMIUM_OVERDRAFT_RATE = 0.85;
	private final double PREMIUM_DAYS_TOLERANCE = 7;
	
	public double bankCharge() {
		double result;
		if (isPremium) {
			result = PREMIUM_BASE_OVERDRAFT_FEE;
			if (daysOverdrawn > PREMIUM_DAYS_TOLERANCE)
				result += (daysOverdrawn - PREMIUM_DAYS_TOLERANCE) * PREMIUM_OVERDRAFT_RATE;
			return result;
	    }
	    else{
			result = BASE_OVERDRAFT_FEE;
			return result + daysOverdrawn * OVERDRAFT_RATE;
		}
	}

	public boolean isPremium() {
		return isPremium;
	}
}