package exercise2;

public class App {

	public static void main(String[] args) {
		Employee kent = new Employee(50);
		JobItemFactory factory = new JobItemFactory();
		JobItem j1 = factory.createJobItem(5, 0, true, kent);
		JobItem j2 = factory.createJobItem(15, 10, false, null);
		int total = j1.getTotalPrice() + j2.getTotalPrice();
	}

}
