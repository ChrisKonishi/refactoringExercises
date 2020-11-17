package exercicio2;

public abstract class LaborJobItem extends JobItem{

	public LaborJobItem(int quantity, int unitPrice, Employee employee) {
        super(quantity, unitPrice, employee)

	}

    public int getUnitPrice(){
        return getEmployee().getRate();
    }
}