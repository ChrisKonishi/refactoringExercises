package exercise4;

import java.util.Set;

public class Person {

	private Set courses;

	public Person(){
		courses = new HashSet();
	}

	public Set getCourses() {
		return courses;
	}

	public void addCourse(Course arg){
		courses.add(arg);
	}

	public void removeCourse(Course arg){
		courses.remove(arg);
	}

	public int getNumberCourses(){
		return courses.size();
	}

	public int getNumberAdvancedCourses(){
		Iterator iter = courses.iterator();
		int count = 0;
		while (iter.hasNext()) {
			Course each = (Course) iter.next();
			if (each.isAdvanced()) {
				count++;
			}
		}
		return count;
	}
}
