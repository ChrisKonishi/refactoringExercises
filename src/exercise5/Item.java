package exercise5;

public class Item {

	public int getPrice() {
		// TODO Auto-generated method stub
		return 0;
	}

	public int getTax() {
		// TODO Auto-generated method stub
		return 0;
	}

	public boolean isOnSale() {
		// TODO Auto-generated method stub
		return false;
	}

	public float getSaleDiscount() {
		// TODO Auto-generated method stub
		return 0;
	}

	public getNetPrice(){
		float price = getPrice() + getTax();
		if (isOnSale()){
			price = price - getSaleDiscount() * price;
		}
		return price;
	
	}

	//...
}
