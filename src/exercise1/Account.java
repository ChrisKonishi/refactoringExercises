package exercise1;

public class Account {

	// ...

	private int daysOverdrawn;

	public double overdraftCharge() {
		if (isPremium()) {
			double result = 10;
			if (daysOverdrawn > 7) {
				result += (daysOverdrawn - 7) * 0.85;
			}
			return result;
	    }
	    else {
	    	return daysOverdrawn * 1.75;
	    }
	}
	  
	public double bankCharge() {
		double result = 4.5;
		if (daysOverdrawn > 0) {
			result += overdraftCharge();
	    }
	   return result;
	}

	public boolean isPremium() {
		// TODO Auto-generated method stub
		return false;
	}
}