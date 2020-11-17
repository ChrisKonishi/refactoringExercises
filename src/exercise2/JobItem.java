package exercise2;

public class JobItem {

	private int quantity;
	private int unitPrice;
	private Employee employee;
	private boolean isLabor;

	public JobItem(int quantity, int unitPrice, Employee employee) {
		this.quantity = quantity;
		this.unitPrice = unitPrice;
		this.employee = employee;
	}

	public int getTotalPrice() {
		return quantity * getUnitPrice();
	}

	public int getQuantity() {
		return quantity;
	}

	public int getUnitPrice(){
		return unitPrice;
	}

	public Employee getEmployee() {
		return employee;
	}

}
