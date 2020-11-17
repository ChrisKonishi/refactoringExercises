package exercise2;

public class JobItemFactory{

    public createJobItem(int quantity, int unitPrice, boolean isLabor, Employee employee){
        if (isLabor){
            return new LaborJobItem(quantity, unitPrice, employee);
        }
        else if (isLabor == false){
            return new JobItem(quantity, unitPrice, employee);
        }
    }
}