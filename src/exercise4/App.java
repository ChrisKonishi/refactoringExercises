package exercise4;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

import org.junit.Assert;


public class App {

	public static void main(String[] args) {
		// Client code
		Person kent = new Person();
		kent.add(new Course("MC426", false));
		kent.add(new Course("MC646", true));
		Assert.assertEquals(2, kent.getNumberCourses());
		Course machinelearning = new Course("MC886", true);
		kent.add(machinelearning);
		kent.add(new Course("MC536", false));
		Assert.assertEquals(4, kent.getNumberCourses());
		kent.remove(machinelearning);
		Assert.assertEquals(3, kent.getNumberCourses());


		System.out.print("Advanced courses: " + kent.getNumberAdvancedCourses());
	}

}